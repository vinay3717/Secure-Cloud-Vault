# Salesforce Custom Object & Field Schema

## Overview
This document specifies the technical data model and field schema for **Project #8 — Custom Application using Salesforce Cloud (Student Record Manager)**.

The application is deployed on Salesforce Lightning Platform to maintain comprehensive academic records of enrolled undergraduate and postgraduate students, tracking their program enrollment, semester progression, academic performance (GPA), and lifecycle status, reinforced with data validation rules and analytical reporting.

---

## 1. Custom Object Definition

| Property | Specification |
|---|---|
| **Label** | Student Record |
| **Plural Label** | Student Records |
| **Object Name (API Name)** | `Student_Record__c` |
| **Record Name Label** | Student Name |
| **Record Name Data Type** | Text (Length: 80) |
| **Description** | Stores individual student academic profiles, roll numbers, department enrollments, GPA metrics, and active lifecycle standing. |
| **Deployment Status** | Deployed |
| **Sharing Model** | Read/Write (Public Read/Write) |
| **Allow Reports** | Enabled (Yes) |
| **Allow Activities** | Enabled (Yes) |
| **Track Field History** | Enabled (Yes) |

---

## 2. Field Schema Specifications

### 2.1 Standard & Identification Fields

| Field Label | API Name | Data Type | Properties | Description |
|---|---|---|---|---|
| Student Name | `Name` | Text(80) | Required | Full legal name of the student (Standard Record Name). |
| Owner | `OwnerId` | Lookup (User, Group) | System Managed | Faculty advisor, registrar officer, or department admin owning the record. |
| Created By | `CreatedById` | Lookup (User) | System Managed | Audit timestamp and user identity at record initialization. |
| Last Modified By | `LastModifiedById` | Lookup (User) | System Managed | Audit timestamp and user identity of latest modification. |

### 2.2 Academic & Demographic Custom Fields

| Field Label | API Name | Data Type | Length / Decimals | Required / Unique | Description & Picklist Values |
|---|---|---|---|---|---|
| Roll Number | `Roll_Number__c` | Text | 20 | Required, Unique (Case-Insensitive) | Unique institutional identifier (e.g., `CS-2023-014`). Serves as External ID for SIS integration. |
| Email | `Email__c` | Email | 80 | Required | Primary student institutional or personal email address used for academic correspondence. |
| Course | `Course__c` | Picklist | — | Required | Academic degree program / engineering department. <br>Values: <br>• `Computer Engineering`<br>• `Information Technology`<br>• `Mechanical Engineering`<br>• `Civil Engineering`<br>• `Electronics & Telecommunication` |
| Semester | `Semester__c` | Number | 2, 0 | Required | Current academic semester term (Valid range: 1 to 8). |
| GPA | `GPA__c` | Number | 3, 2 | Required | Cumulative Grade Point Average evaluated on a 10.00 scale (Format: `0.00` – `10.00`). |
| Status | `Status__c` | Picklist | — | Required | Current administrative standing of the student.<br>Values:<br>• `Active` (Default)<br>• `On Leave`<br>• `Graduated`<br>• `Dropped` |
| Enrolment Date | `Enrolment_Date__c` | Date | — | Required | Official date of admission and registration into the institution. |

---

## 3. Validation Rules

### VR01 — Cumulative GPA Range Constraint
- **Rule Name**: `VR_GPA_Range`
- **Active**: True
- **Description**: Ensures entered Grade Point Average conforms to the institutional 10.00 scale. Rejects values below 0.00 or above 10.00.
- **Error Condition Formula**:
  ```sql
  OR(
      GPA__c < 0.00,
      GPA__c > 10.00
  )
  ```
- **Error Message**: *"GPA must be between 0.00 and 10.00."*
- **Error Display Location**: Field: `GPA__c`

### VR02 — Semester Term Boundary Constraint
- **Rule Name**: `VR_Semester_Range`
- **Active**: True
- **Description**: Restricts valid academic terms between Semester 1 and Semester 8.
- **Error Condition Formula**:
  ```sql
  OR(
      Semester__c < 1,
      Semester__c > 8
  )
  ```
- **Error Message**: *"Semester must be between 1 and 8."*
- **Error Display Location**: Field: `Semester__c`

---

## 4. Lightning Page Layout Architecture

1. **Header Highlights Panel**:
   - `Name` (Student Name)
   - `Roll_Number__c`
   - `Course__c`
   - `GPA__c`
   - `Status__c`
2. **Student Identity & Enrolment Details**:
   - Left Column: `Name`, `Roll_Number__c`, `Email__c`
   - Right Column: `Enrolment_Date__c`, `Status__c`
3. **Academic Performance & Progression**:
   - Left Column: `Course__c`, `Semester__c`
   - Right Column: `GPA__c`
4. **System Audit Information**:
   - Created By, Last Modified By, Record Owner
