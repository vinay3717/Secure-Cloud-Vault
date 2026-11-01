# Salesforce Custom Object & Field Schema

## Overview
This document specifies the data model and schema for **Project #8 — Custom Application using Salesforce Cloud (Student Inquiry & Records Management)**. 

The application is deployed on Salesforce Lightning Platform to capture prospective student inquiries, manage application lifecycles, track counselor interactions, and power analytical admission reports and dashboards.

---

## 1. Custom Object Definition

| Property | Value |
|---|---|
| **Label** | Student Inquiry |
| **Plural Label** | Student Inquiries |
| **API Name / Object Name** | `Student_Inquiry__c` |
| **Data Type** | Custom Object |
| **Record Name** | `Inquiry_Number` |
| **Record Name Data Type** | Auto Number |
| **Display Format** | `INQ-{YYYY}-{0000}` (e.g., `INQ-2026-0001`) |
| **Starting Number** | 1 |
| **Description** | Tracks student inquiries, academic credentials, target programs, and enrollment progress. |
| **Deployment Status** | Deployed |
| **Sharing Model** | Public Read/Write |

---

## 2. Field Schema Specifications

### 2.1 Standard & Identification Fields

| Field Label | API Name | Data Type | Length / Format | Required | Description |
|---|---|---|---|---|---|
| Inquiry Number | `Name` | Auto Number | `INQ-{YYYY}-{0000}` | Yes | System-generated unique identifier for inquiry |
| Owner | `OwnerId` | Lookup (User/Queue) | 18 chars | Yes | Assigned admissions counselor or queue |
| Created By | `CreatedById` | Lookup (User) | 18 chars | Yes | Audit audit trail: creation user & timestamp |
| Last Modified By | `LastModifiedById` | Lookup (User) | 18 chars | Yes | Audit trail: last modification user & timestamp |

### 2.2 Applicant Personal & Contact Information

| Field Label | API Name | Data Type | Properties | Description |
|---|---|---|---|---|
| First Name | `First_Name__c` | Text(50) | Required | Applicant's legal first name |
| Last Name | `Last_Name__c` | Text(50) | Required | Applicant's legal surname |
| Email Address | `Email__c` | Email | Unique, External ID | Primary communication email |
| Contact Phone | `Phone__c` | Phone | — | Primary mobile or home contact number |
| City | `City__c` | Text(60) | — | Current residential city |
| State/Province | `State__c` | Text(60) | — | Current residential state/province |

### 2.3 Academic Profile & Program Preferences

| Field Label | API Name | Data Type | Picklist Values / Formula | Description |
|---|---|---|---|---|
| Target Degree Program | `Target_Degree__c` | Picklist | `B.Tech Computer Science`<br>`B.Tech AI & Data Science`<br>`B.Tech Cyber Security`<br>`M.Tech Cloud Computing`<br>`MCA` | Prospective academic program |
| Preferred Intake | `Preferred_Intake__c` | Picklist | `Fall 2026`<br>`Spring 2027`<br>`Fall 2027` | Desired academic term for enrollment |
| High School / Prior GPA | `High_School_GPA__c` | Percent(5, 2) | Range: `0.00%` – `100.00%` | Prior qualifying examination percentage |
| Entrance Exam Score | `Entrance_Score__c` | Number(3, 0) | Range: `0` – `100` | Normalized institutional entrance test score |
| Merit Scholarship Eligible | `Scholarship_Eligible__c` | Formula (Checkbox) | `IF(High_School_GPA__c >= 0.85, TRUE, FALSE)` | Evaluates eligibility for merit-based financial aid |

### 2.4 Admission Lifecycle & Counseling

| Field Label | API Name | Data Type | Picklist Values / Properties | Description |
|---|---|---|---|---|
| Inquiry Status | `Inquiry_Status__c` | Picklist | `New`<br>`Contacted`<br>`Counseling Scheduled`<br>`Application Submitted`<br>`Enrolled`<br>`Closed - Lost` | Current stage in the admissions pipeline |
| Application Fee Paid | `Application_Fee_Paid__c` | Checkbox | Default: `FALSE` | Verifies non-refundable application fee payment |
| Next Follow-Up Date | `Follow_Up_Date__c` | Date | — | Scheduled date for counselor follow-up call |
| Counselor Notes | `Counselor_Notes__c` | Long Text Area(2000) | Visible Lines: 5 | Internal qualitative notes from counseling interactions |

---

## 3. Validation Rules

### VR01 — Valid GPA Range
- **Rule Name**: `VR_GPA_Percentage_Range`
- **Formula**:
  ```sql
  OR(High_School_GPA__c < 0.0, High_School_GPA__c > 1.0)
  ```
- **Error Message**: *"High School GPA percentage must be between 0.00% and 100.00%."*

### VR02 — Contact Method Mandatory
- **Rule Name**: `VR_Email_Or_Phone_Required`
- **Formula**:
  ```sql
  AND(ISBLANK(Email__c), ISBLANK(Phone__c))
  ```
- **Error Message**: *"Either an Email Address or a Contact Phone number must be provided."*

---

## 4. Lightning Page Layout Sections

1. **Header**: Inquiry Number, Inquiry Status badge, Target Degree, Scholarship Eligibility.
2. **Student Contact Information**: First Name, Last Name, Email Address, Contact Phone, City, State.
3. **Academic Evaluation**: Target Degree Program, Preferred Intake, High School GPA, Entrance Exam Score, Scholarship Eligible (Read-only Formula).
4. **Admissions Workflow & Counseling**: Inquiry Status, Application Fee Paid, Next Follow-Up Date, Counselor Notes.
5. **System Information**: Created By, Last Modified By, Owner.
