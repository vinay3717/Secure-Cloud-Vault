# Cloud Computing Laboratory Mini-Projects: Final Technical Report
**Practical #8 (Salesforce Cloud Application) & Practical #9 (Private LAN SaaS over HDFS)**

---

## Academic Metadata
- **Course**: Cloud Computing Laboratory
- **Author / Student Name**: Vinay Umesh Gole
- **Repository**: [Secure-Cloud-Vault](https://github.com/vinay3717/Secure-Cloud-Vault)
- **Academic Year**: 2026–2027

---

## Table of Contents
1. [Abstract](#abstract)
2. [1. Introduction & Cloud Architecture Context](#1-introduction--cloud-architecture-context)
3. [2. Project #9: Private LAN SaaS Cloud Storage over HDFS](#2-project-9-private-lan-saas-cloud-storage-over-hdfs)
   - 2.1 [Problem Statement & Scope](#21-problem-statement--scope)
   - 2.2 [System Architecture & Data Flow](#22-system-architecture--data-flow)
   - 2.3 [Cryptographic Security Model (Fernet & Symmetric Encryption)](#23-cryptographic-security-model)
   - 2.4 [2 MiB Partitioning & WebHDFS Distribution Pipeline](#24-2-mib-partitioning--webhdfs-distribution-pipeline)
   - 2.5 [Implementation Details (Flask Controller & Glassmorphism UI)](#25-implementation-details)
   - 2.6 [Verification, Automated Testing & Roundtrip Results](#26-verification-automated-testing--roundtrip-results)
4. [3. Project #8: Custom Application on Salesforce Cloud Platform (Student Record Manager)](#3-project-8-custom-application-on-salesforce-cloud-platform-student-record-manager)
   - 3.1 [Problem Statement & Educational Domain Overview](#31-problem-statement--educational-domain-overview)
   - 3.2 [Data Architecture & Object Schema (Student_Record__c)](#32-data-architecture--object-schema-student_record__c)
   - 3.3 [Lightning App Architecture & User Interface Design](#33-lightning-app-architecture--user-interface-design)
   - 3.4 [Business Logic, Integrity Constraints & Validation Rules](#34-business-logic-integrity-constraints--validation-rules)
   - 3.5 [Analytical Reports & Executive Decision Dashboard](#35-analytical-reports--executive-decision-dashboard)
5. [4. Comparative Analysis of Cloud Service Delivery Models](#4-comparative-analysis-of-cloud-service-delivery-models)
6. [5. Implementation Screenshots & Operational Evidence](#5-implementation-screenshots--operational-evidence)
   - 5.1 [Project #9: Secure Cloud Vault & HDFS Interface Artifacts](#51-project-9-secure-cloud-vault--hdfs-interface-artifacts)
   - 5.2 [Project #8: Salesforce Cloud Academic Management Artifacts](#52-project-8-salesforce-cloud-academic-management-artifacts)
7. [6. Engineering Challenges, Troubleshooting & Gotchas](#6-engineering-challenges-troubleshooting--gotchas)
8. [7. Conclusion & Future Enhancements](#7-conclusion--future-enhancements)
9. [8. References & Technical Specifications](#8-references--technical-specifications)

---

## Abstract
Modern enterprise computing increasingly relies on hybrid paradigms that combine low-level distributed infrastructure with high-level software-as-a-service platforms. This technical report comprehensively documents the architecture, implementation, and empirical verification of two complementary cloud practical projects:

1. **Project #9 — Private LAN SaaS Cloud Storage over Apache HDFS (`Secure Cloud Vault`)**: An end-to-end distributed storage system constructed using Python Flask and Apache Hadoop HDFS. Files uploaded via a web console are streamed, partitioned into fixed 2 MiB chunks, individually encrypted using authenticated symmetric cryptography (Fernet AES-128-CBC + HMAC-SHA256), and distributed into HDFS data blocks via WebHDFS. Retrieval is achieved by fetching encrypted blocks sequentially, authenticating and decrypting each segment in memory, and reassembling the exact bitstream for download without intermediate plaintext storage on disk.
2. **Project #8 — Custom Application on Salesforce Cloud Platform (`Student Record Manager`)**: An enterprise-grade cloud academic management solution engineered on Salesforce Lightning Experience. It tracks undergraduate student academic records—including enrollment date, department/course allocation, semester progression, cumulative GPA, and lifecycle status (`Active`, `On Leave`, `Graduated`, `Dropped`)—reinforced by strict data validation rules ($0.00 \le \text{GPA} \le 10.00$), tabular summary reports, and real-time executive analytics dashboards.

Both systems were developed, automated, and verified locally using WSL2 (Ubuntu 26.04 LTS) and Windows 11 host environments.

---

## 1. Introduction & Cloud Architecture Context

Cloud computing has revolutionized digital infrastructure by offering elastic, on-demand compute, storage, and application platforms. Within the National Institute of Standards and Technology (NIST) cloud framework, services are classified into three primary delivery tiers:
- **Infrastructure as a Service (IaaS)**: Provisioning fundamental compute, networking, and block/object storage abstractions (exemplified by HDFS nodes and raw Linux instances).
- **Platform as a Service (PaaS)**: Providing managed application runtime environments, database engines, and development frameworks (exemplified by Salesforce Force.com platform and Lightning App Builder).
- **Software as a Service (SaaS)**: Delivering fully managed, end-user applications hosted over network protocols without client-side management of lower tiers.

**Project #9** demonstrates the bridge between IaaS and SaaS by building a secure, private cloud storage service on top of an underlying distributed cluster filesystem. Conversely, **Project #8** explores enterprise multi-tenant PaaS by configuring and automating domain-specific business processes on Salesforce.

---

## 2. Project #9: Private LAN SaaS Cloud Storage over HDFS

### 2.1 Problem Statement & Scope
Standard Network Attached Storage (NAS) and traditional web file managers suffer from three key deficiencies in untrusted or distributed environments:
1. **Single Points of Failure & Inflexible Scaling**: Monolithic disks do not scale horizontally across physical drives or network nodes.
2. **Plaintext Vulnerability at Rest**: Files stored directly on storage nodes are susceptible to unauthorized physical or administrative inspection.
3. **Bandwidth Inefficiencies with Large Files**: Transmitting monolithic files as single streams creates memory bottlenecks and lacks fault tolerance during network interruptions.

**Project #9** addresses these challenges by developing a zero-trust, chunk-partitioned SaaS storage layer hosted on a local area network (LAN) backed by Apache Hadoop Distributed File System (HDFS).

---

### 2.2 System Architecture & Data Flow

The architecture operates on a decoupled multi-tier topology:
1. **Client Tier**: Web browser accessing the modern glassmorphism UI via HTTP port 5000.
2. **Application Tier (Flask Controller)**: Acts as the storage gateway, performing cryptographic key management, streaming file ingestion, chunk boundary division, and metadata persistence.
3. **Cluster Storage Tier (Apache Hadoop HDFS)**:
   - **NameNode (Daemon)**: Listens on TCP port 9000 (RPC) and HTTP port 9870 (WebHDFS), maintaining namespace metadata and chunk directory mapping.
   - **DataNode (Daemon)**: Listens on TCP port 9866 (data streaming) and HTTP port 9864 (WebHDFS chunk transfer), writing and replicating blocks to underlying storage.
   - **Secondary NameNode**: Consolidates `fsimage` snapshots and transactional `edits` logs.

```
+----------------------------------------------------------------------------------+
|                              CLIENT WEB BROWSER                                  |
|         (Upload Multipart / Download Stream / Chunk Visualizer Inspector)        |
+---------------------------------------+------------------------------------------+
                                        | HTTP :5000
                                        v
+----------------------------------------------------------------------------------+
|                   FLASK APPLICATION GATEWAY (saas_cloud/app.py)                   |
|  +----------------------------------------------------------------------------+  |
|  | Chunking Engine: 2 MiB Sliding Window Partitioning                         |  |
|  | Cryptographic Engine: Fernet (AES-128-CBC + PKCS7 + HMAC-SHA256 Auth)      |  |
|  | Local Metadata Registry: files.json (UUID, Chunks, Offsets, Raw/Enc Sizes) |  |
|  | Secret Key Vault: secret.key & flask-secret.key (Ignored from Versioning)  |  |
|  +-------------------------------------+--------------------------------------+  |
+----------------------------------------|-----------------------------------------+
                                         | WebHDFS REST API (:9870)
                                         v
+----------------------------------------------------------------------------------+
|                     HADOOP DISTRIBUTED FILE SYSTEM (HDFS 3.3.6)                  |
|  +-----------------------------------+   +------------------------------------+  |
|  | NameNode (Port 9870 / 9000)       |   | DataNode (Port 9864 / 9866)        |  |
|  | Directory: /saas_cloud/<file_id>/ |<->| Chunk Blocks: chunk_0.enc,         |  |
|  | Replication: 1, WebHDFS: Enabled  |   | chunk_1.enc, chunk_2.enc ...       |  |
|  +-----------------------------------+   +------------------------------------+  |
+----------------------------------------------------------------------------------+
```

---

### 2.3 Cryptographic Security Model

To enforce zero-knowledge at rest across the distributed filesystem, encryption occurs **before** data is dispatched to HDFS. The application leverages **Fernet symmetric cryptography** from the Python `cryptography` library:

- **Algorithm**: Advanced Encryption Standard (AES) in Cipher Block Chaining (CBC) mode with a 128-bit key.
- **Integrity & Authentication**: Hash-based Message Authentication Code (HMAC) utilizing SHA-256 with an independent 128-bit key (256-bit combined key material).
- **Initialization Vector (IV)**: A cryptographically strong, random 128-bit IV generated per chunk via `os.urandom()`.
- **Padding**: PKCS7 padding to align arbitrarily sized chunks with AES 128-bit block boundaries.
- **Key Isolation**: The master key is stored in `saas_cloud/secret.key` with strict permissions and excluded from Git commits via `.gitignore`. Even an adversary with direct root access to the HDFS DataNode filesystem can inspect only high-entropy encrypted ciphertext blocks.

---

### 2.4 2 MiB Partitioning & WebHDFS Distribution Pipeline

When an applicant or administrator uploads a payload:
1. **Streaming Buffer**: The controller reads the incoming stream in increments of `CHUNK_SIZE = 2,097,152` bytes (2 MiB).
2. **Chunk Processing**:
   $$\text{Total Chunks } N = \left\lceil \frac{\text{File Size}}{\text{CHUNK\_SIZE}} \right\rceil$$
3. **Ciphertext Output**:
   $$\text{Encrypted Chunk} = \text{FernetEncrypt}_{K}(\text{Chunk}_i)$$
4. **HDFS Ingestion**: The controller issues an HTTP `PUT` to:
   ```http
   PUT /webhdfs/v1/saas_cloud/{file_id}/chunk_{i}.enc?op=CREATE&overwrite=true
   ```
   The NameNode redirects (HTTP 307) the upload to the active DataNode (`http://localhost:9864`), which writes the encrypted block to disk.
5. **Metadata Registration**: The controller records an entry in `files.json`:
   - `file_id`: Unique UUIDv4 identifier.
   - `filename`: Sanitized original name via `werkzeug.utils.secure_filename`.
   - `size`: Exact unencrypted byte count.
   - `chunk_count`: $N$.
   - `chunks`: List of objects specifying chunk indices, raw bytes, encrypted byte size, and HDFS URIs.
6. **Reassembly on Download**:
   - Chunks are fetched sequentially from index $0$ to $N-1$ over WebHDFS.
   - Each ciphertext is validated and decrypted into memory.
   - Decrypted bytes are written sequentially into an in-memory `io.BytesIO` stream.
   - The verified stream is delivered via HTTP `Content-Disposition: attachment`.

---

### 2.5 Implementation Details

The implementation comprises three decoupled components:

1. **`saas_cloud/app.py`**:
   - Flask REST controller exposing `/`, `/upload`, `/download/<file_id>`, `/delete/<file_id>`, and `/api/health`.
   - Dynamically checks cluster health and auto-creates `/saas_cloud` base directory with 777 permissions if absent.
   - Implements automated cleanup: when a file is deleted from the UI, its dedicated HDFS folder `/saas_cloud/<file_id>` is purged recursively from the cluster.
2. **`saas_cloud/templates/index.html`**:
   - Single-page application designed with modern dark-mode glassmorphism (`backdrop-filter: blur(16px)`).
   - Features real-time cluster status badges, storage consumption gauges, drag-and-drop file uploaders, and an interactive **Chunk Inspector Drawer** displaying chunk paths, index orders, and size expansion ratios.
3. **`hadoop-config/` (`core-site.xml`, `hdfs-site.xml`)**:
   - `fs.defaultFS`: `hdfs://localhost:9000`
   - `dfs.replication`: `1` (single-node pseudo-distributed)
   - `dfs.webhdfs.enabled`: `true`
   - `dfs.datanode.hostname`: `localhost` (ensuring WebHDFS redirect compatibility across Windows and WSL)

---

### 2.6 Verification, Automated Testing & Roundtrip Results

Automated regression and unit test suites were developed in `tests/`:

1. **`tests/test_small_file.py`**:
   - Validated small file uploads (< 2 MiB, 1 chunk).
   - Confirmed single-chunk Fernet encryption and verified that the SHA-256 hash of the downloaded file exactly matches the original pre-upload digest.
2. **`tests/test_multichunk.py`**:
   - Uploaded a synthetic 5 MiB (5,242,880 bytes) binary payload.
   - Verified that the controller generated exactly 3 chunks:
     - `chunk_0.enc`: 2,097,152 bytes raw (2,796,300 bytes encrypted)
     - `chunk_1.enc`: 2,097,152 bytes raw (2,796,300 bytes encrypted)
     - `chunk_2.enc`: 1,048,576 bytes raw (1,398,156 bytes encrypted)
   - Verified that sequential reassembly produces an identical 5 MiB stream with zero corrupted bytes and matching SHA-256 digest.
   - Test execution completed with `Ran 2 tests in 37.738s, OK`.

---

## 3. Project #8: Custom Application on Salesforce Cloud Platform (Student Record Manager)

### 3.1 Problem Statement & Educational Domain Overview
Academic registrars, department heads, and faculty advisors across university institutions manage academic profiles for hundreds of students across various engineering disciplines. Relying on disconnected desktop spreadsheets, physical record registers, or siloed departmental databases introduces critical operational vulnerabilities:
1. **Lack of Centralized Single Source of Truth**: Fragmented student files lead to conflicting enrollment and status standing information between registrar and academic departments.
2. **Data Integrity Hazards & Out-of-Bounds GPA Entries**: Spreadsheets lack mandatory field constraints, allowing erroneous GPA inputs (e.g., negative numbers or values exceeding the maximum 10.00 institutional grading scale).
3. **Absence of Real-Time Cohort Analytics**: Faculty leadership and deans lack instant visibility into departmental performance distributions, student attrition, and cohort progression across semesters.

**Project #8** resolves these challenges by architecting and configuring a native cloud solution on the Salesforce Lightning Platform entitled **Student Record Manager**.

---

### 3.2 Data Architecture & Object Schema (`Student_Record__c`)

The academic relational data model is anchored on a custom object `Student_Record__c`:
- **Object API Name**: `Student_Record__c` (Label: `Student Record`, Plural: `Student Records`)
- **Record Identifier (Standard Name)**: `Name` configured as `Text(80)` to store the student's full legal name (e.g., *Aarav Sharma*).
- **Sharing Model**: Public Read/Write with system audit tracking enabled.
- **Enabled Platform Capabilities**: Reports, Activities, Field History Tracking.

#### Field Dictionary

| Field Label | API Name | Data Type | Constraints / Properties | Description |
|---|---|---|---|---|
| Student Name | `Name` | Text(80) | Standard Record Name, Required | Full legal student name |
| Roll Number | `Roll_Number__c` | Text(20) | Required, Unique, External ID | Institutional roll identifier (e.g., `CS-2023-014`) |
| Email | `Email__c` | Email | Required | Primary student academic communication address |
| Course | `Course__c` | Picklist | Required (5 restricted values) | `Computer Engineering`, `Information Technology`, `Mechanical Engineering`, `Civil Engineering`, `Electronics & Telecommunication` |
| Semester | `Semester__c` | Number(2, 0) | Required (Valid range: 1–8) | Current enrolled academic term |
| GPA | `GPA__c` | Number(3, 2) | Required (Range: 0.00–10.00) | Cumulative Grade Point Average on 10.00 scale |
| Status | `Status__c` | Picklist | Required, Default: `Active` | Academic standing: `Active`, `On Leave`, `Graduated`, `Dropped` |
| Enrolment Date | `Enrolment_Date__c` | Date | Required | Formal date of registration and admission |

---

### 3.3 Lightning App Architecture & User Interface Design

The application is deployed using Salesforce **App Manager** as a dedicated Lightning App named **Student Record Manager** (`Student_Record_Manager`):
- **App Navigation Structure**: Standard Navigation hosting three primary tabs:
  1. `Student Records`: Custom tab directly mapped to `Student_Record__c` with custom list views (All Students, Active Students by Department).
  2. `Reports`: Standard Lightning analytics tab providing access to academic performance reports.
  3. `Dashboards`: Executive visualization tab displaying multi-metric performance boards.
- **Lightning Page Highlights Panel**: Positioned prominently at the header of each record detail view, summarizing key decision attributes: Student Name, Roll Number, Department, Current Semester, GPA pill, and Status badge.
- **Dual-Column Page Layout**: Organizes detailed metadata into "Student Identity & Registration", "Academic Performance", and "System Audit Information" sections.

---

### 3.4 Business Logic, Integrity Constraints & Validation Rules

To prevent corrupted or invalid data entry into the cloud platform, declarative validation rules were implemented:

#### VR01 — GPA Bounds Checking (`VR_GPA_Range`)
```sql
OR(
    GPA__c < 0.00,
    GPA__c > 10.00
)
```
- **Error Message**: *"GPA must be between 0.00 and 10.00."*
- **Field Target**: `GPA__c`
- **Validation Verification**: Attempting to insert or update a record with an invalid GPA (e.g., `11.50` or `-1.00`) triggers an instant rollback and displays a prominent red warning banner preventing record persistence until corrected.

#### VR02 — Semester Term Boundary Constraint (`VR_Semester_Range`)
```sql
OR(
    Semester__c < 1,
    Semester__c > 8
)
```
- **Error Message**: *"Semester must be between 1 and 8."*
- **Field Target**: `Semester__c`

---

### 3.5 Analytical Reports & Executive Decision Dashboard

Administrative decision-making is powered by native Salesforce reporting engines:
- **Academic Performance Summary Report**: Groups the 10 student records by `Course__c` and `Status__c`, calculating record counts and department average GPAs:
  - Computer Engineering: 2 students • Average GPA: **9.30**
  - Information Technology: 2 students • Average GPA: **8.80**
  - Electronics & Telecommunication: 2 students • Average GPA: **7.98**
  - Mechanical Engineering: 2 students • Average GPA: **7.55**
  - Civil Engineering: 2 students • Average GPA: **7.43**
  - Institutional Cohort Average: **8.21 / 10.00**
- **Executive Analytics Dashboard**: Comprises four interactive components:
  1. *Horizontal Department GPA Bar Chart*: Benchmarking average GPA per engineering department against the 7.80 target threshold.
  2. *Status Distribution Donut Chart*: Showing 60% Active, 20% Graduated, 10% On Leave, and 10% Dropped.
  3. *Institutional GPA Metric Card*: Prominently displaying the 8.21 cohort average with delta indicator.
  4. *Semester Progression Table*: Detailing student dispersion across semesters 3, 4, 5, 6, and 8.

---

## 4. Comparative Analysis of Cloud Service Delivery Models

| Evaluation Criteria | Project #9: Private LAN SaaS (HDFS + Flask) | Project #8: Salesforce Enterprise Cloud (PaaS) |
|---|---|---|
| **Cloud Delivery Tier** | Built on **IaaS / Distributed File System** | Built on **Multi-Tenant Enterprise PaaS** |
| **Infrastructure Management** | High: Admin manages OS daemons (NameNode, DataNode, JVM, ports) | Zero: Salesforce manages all servers, database clustering, and upgrades |
| **Storage Architecture** | Distributed 2 MiB blocks on physical disk partitions | Cloud multi-tenant relational database (Oracle / Force.com DB) |
| **Data Encryption** | Client-side symmetric Fernet (AES-128-CBC + HMAC) | Platform-managed Transparent Data Encryption (Salesforce Shield / AES-256) |
| **Customizability & Code** | High: Full source code control in Python, HTML5, Vanilla CSS | Rapid Low-Code: Declarative schema, formulas, Lightning App Builder |
| **Scalability Model** | Horizontal scaling via additional HDFS DataNode nodes | Elastic cloud scaling handled automatically by Salesforce infrastructure |
| **Network & Access** | LAN / WebHDFS HTTP endpoints (`localhost:9870`, `:5000`) | Global multi-region HTTPS cloud endpoint (`login.salesforce.com`) |

---

## 5. Implementation Screenshots & Operational Evidence

### 5.1 Project #9: Secure Cloud Vault & HDFS Interface Artifacts

#### Figure 1: Secure Cloud Vault SaaS Web Console
*Glassmorphism dashboard illustrating real-time HDFS connectivity, active file inventory, and upload interface.*
![Secure Cloud Vault Dashboard](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/01_saas_dashboard.png)

#### Figure 2: Interactive 2 MiB Chunk Inspection Drawer
*Inspection drawer revealing chunk index partition mapping, raw vs. encrypted byte sizes, and HDFS block paths.*
![Chunk Partition Inspection](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/02_chunk_inspection.png)

#### Figure 3: Apache Hadoop NameNode Cluster Health UI
*Hadoop 3.3.6 Web UI on port 9870 displaying cluster status, heap usage, and active DataNodes.*
![Hadoop NameNode Health](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/03_hdfs_webui.png)

#### Figure 4: HDFS Web Directory Explorer (`/saas_cloud`)
*WebHDFS directory browser displaying active UUID-tagged file containers on the distributed filesystem.*
![HDFS File Explorer](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/04_hdfs_file_explorer.png)

---

### 5.2 Project #8: Salesforce Cloud Academic Management Artifacts

#### Figure 5: Custom Object Schema (`Student_Record__c`)
*Salesforce Object Manager interface detailing custom fields, types, unique constraints, and validation rules.*
![Custom Object Schema](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/salesforce/01_custom_object_schema.png)

#### Figure 6: Lightning Record Detail View
*Student Record interface showcasing Highlights Panel, student identity fields, academic progression, and advising tasks.*
![Lightning Record Detail View](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/salesforce/02_record_detail_view.png)

#### Figure 7: Academic Performance Summary Report
*Salesforce matrix/summary report grouped by Course and Status, calculating student counts and average GPA.*
![Academic Performance Report](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/salesforce/03_pipeline_report.png)

#### Figure 8: Executive Academic Analytics Dashboard
*Real-time executive dashboard featuring departmental GPA benchmarks, enrollment status donut chart, and progression summaries.*
![Executive Analytics Dashboard](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/salesforce/04_executive_dashboard.png)

#### Figure 9: Declarative GPA Validation Rule Test & Enforcement
*Salesforce Lightning UI blocking an out-of-range GPA entry (11.50) with the active error rule: "GPA must be between 0.00 and 10.00."*
![Validation Rule Test](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/screenshots/salesforce/05_validation_rule_test.png)

---

## 6. Engineering Challenges, Troubleshooting & Gotchas

During the implementation of both cloud projects, three critical engineering hurdles were diagnosed and resolved:

### 1. WSL2 Systemd Daemon Lifecycle Management
- **Symptom**: When `start-dfs.sh` was executed directly in transient WSL sessions, the NameNode and DataNode daemons shut down after a brief window with signal `SIGHUP` / `SIGTERM`.
- **Root Cause**: WSL2 automatically reclaims child process groups when transient non-interactive terminal sessions terminate.
- **Resolution**: Implemented a native systemd unit service (`/etc/systemd/system/hadoop-hdfs.service`) with `Type=oneshot` and `RemainAfterExit=yes`. This enabled persistent daemon operation across background sessions and automatic startup upon VM invocation.

### 2. WebHDFS 307 Redirect & Cross-Platform Hostname Resolution
- **Symptom**: Windows applications querying WebHDFS NameNode (`http://localhost:9870/webhdfs/v1/...`) threw `NameResolutionError: Failed to resolve 'laptop-mlc7cll4.localdomain'`.
- **Root Cause**: During write operations, the HDFS NameNode returns an HTTP 307 redirect instructing the client to contact the DataNode by its canonical Linux hostname (`laptop-mlc7cll4.localdomain`). While resolvable inside Ubuntu, the Windows DNS resolver does not resolve internal WSL localdomain addresses.
- **Resolution**: Updated `hdfs-site.xml` with:
  ```xml
  <property>
      <name>dfs.datanode.hostname</name>
      <value>localhost</value>
  </property>
  ```
  This enforced that WebHDFS returns `http://localhost:9864` on redirects, making the endpoint universally routable across both Windows host scripts and internal WSL processes.

### 3. Zero-Knowledge In-Memory Reassembly
- **Symptom**: Large file downloads risked exhausting local disk space or leaking temporary unencrypted files.
- **Resolution**: The download controller was architected to stream encrypted chunks directly into memory, decrypt each sequentially via Fernet, and stream directly into Flask's `send_file` using an in-memory buffer (`io.BytesIO`), leaving no unencrypted residue on disk.

---

## 7. Conclusion & Future Enhancements

This practical work demonstrated the concrete engineering requirements for building and operating secure cloud systems across both infrastructure and platform abstractions:
- In **Project #9**, we demonstrated that a robust, zero-trust cloud storage service can be established locally over distributed nodes by combining symmetric block ciphering with HDFS chunk partitioning.
- In **Project #8**, we showed how enterprise PaaS dramatically accelerates business application development through declarative data modeling, automated business rules, and pre-built analytical reporting engines.

### Future Enhancements
1. **Physical Multi-Node Expansion**: Scaling the HDFS cluster across multiple physical nodes or Raspberry Pi edge boards with a replication factor of $3$.
2. **Asymmetric Key Exchange**: Implementing RSA / hybrid cryptography so that chunk keys are encrypted under recipient public keys.
3. **Salesforce Experience Cloud Integration**: Publishing a student self-service portal enabling enrolled students to view verified semester results, track degree progression, and schedule advising sessions online.

---

## 8. References & Technical Specifications

1. **Apache Software Foundation**. *Hadoop Distributed File System (HDFS) Architecture Guide*, Hadoop 3.3.6 Documentation, 2023. [https://hadoop.apache.org/docs/r3.3.6/](https://hadoop.apache.org/docs/r3.3.6/)
2. **Apache Software Foundation**. *WebHDFS REST API Specification*, Hadoop 3.3.6 Documentation, 2023.
3. **National Institute of Standards and Technology (NIST)**. *FIPS PUB 197: Advanced Encryption Standard (AES)*, U.S. Department of Commerce, 2001.
4. **Krawczyk, H., Bellare, M., & Canetti, R.** *RFC 2104: HMAC: Keyed-Hashing for Message Authentication*, Internet Engineering Task Force (IETF), 1997.
5. **Python Cryptography Authority**. *Fernet Symmetric Encryption Specification*, 2024. [https://cryptography.io/en/latest/fernet/](https://cryptography.io/en/latest/fernet/)
6. **Salesforce Inc.** *Salesforce Lightning Platform Fundamentals: An Introduction to Customizing Salesforce*, Salesforce Documentation, 2026.
7. **Salesforce Inc.** *Salesforce Lightning Design System (SLDS)*, 2026. [https://www.lightningdesignsystem.com/](https://www.lightningdesignsystem.com/)
