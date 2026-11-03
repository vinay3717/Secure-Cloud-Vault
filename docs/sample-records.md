# Sample Student Records for Demonstration & Testing

This document contains 10 synthetic student records used to populate the **Student Record Manager** application on Salesforce Lightning Platform.

The dataset covers a diverse distribution of engineering departments, semesters, academic performance metrics (GPA on a 10.0 scale), and lifecycle statuses (`Active`, `On Leave`, `Graduated`, `Dropped`).

---

## 1. Tabular Representation

| Student Name | Roll Number | Email | Course | Semester | GPA | Status | Enrolment Date |
|---|---|---|---|---|---|---|---|
| **Aarav Sharma** | `CS-2023-014` | `aarav.sharma@example.edu` | Computer Engineering | 6 | 8.85 | Active | 2023-08-01 |
| **Priya Patel** | `IT-2023-028` | `priya.patel@example.edu` | Information Technology | 6 | 9.40 | Active | 2023-08-01 |
| **Rohan Deshmukh** | `ME-2022-009` | `rohan.deshmukh@example.edu` | Mechanical Engineering | 8 | 7.65 | Graduated | 2022-08-05 |
| **Ananya Iyer** | `CE-2024-003` | `ananya.iyer@example.edu` | Civil Engineering | 4 | 8.95 | Active | 2024-08-10 |
| **Vikram Singh** | `ET-2023-019` | `vikram.singh@example.edu` | Electronics & Telecommunication | 5 | 6.80 | On Leave | 2023-08-01 |
| **Sneha Reddy** | `CS-2024-042` | `sneha.reddy@example.edu` | Computer Engineering | 4 | 9.75 | Active | 2024-08-10 |
| **Aditya Verma** | `IT-2022-015` | `aditya.verma@example.edu` | Information Technology | 8 | 8.20 | Graduated | 2022-08-05 |
| **Neha Kulkarni** | `ME-2024-011` | `neha.kulkarni@example.edu` | Mechanical Engineering | 3 | 7.45 | Active | 2024-08-10 |
| **Karan Mehta** | `CE-2023-033` | `karan.mehta@example.edu` | Civil Engineering | 5 | 5.90 | Dropped | 2023-08-01 |
| **Tanvi Bose** | `ET-2024-008` | `tanvi.bose@example.edu` | Electronics & Telecommunication | 4 | 9.15 | Active | 2024-08-10 |

---

## 2. Statistical Breakdown

- **Total Records**: 10
- **Status Breakdown**:
  - `Active`: 6 students (60%)
  - `Graduated`: 2 students (20%)
  - `On Leave`: 1 student (10%)
  - `Dropped`: 1 student (10%)
- **Course Distribution**:
  - `Computer Engineering`: 2 students (Avg GPA: 9.30)
  - `Information Technology`: 2 students (Avg GPA: 8.80)
  - `Mechanical Engineering`: 2 students (Avg GPA: 7.55)
  - `Civil Engineering`: 2 students (Avg GPA: 7.43)
  - `Electronics & Telecommunication`: 2 students (Avg GPA: 7.98)
- **Overall Average GPA**: **8.21 / 10.00**
- **GPA Range**: Minimum `5.90` (Karan Mehta), Maximum `9.75` (Sneha Reddy)

---

## 3. CSV Import Format

For automated data upload via Salesforce **Data Import Wizard** or **Salesforce CLI (Data Import)**:

```csv
Name,Roll_Number__c,Email__c,Course__c,Semester__c,GPA__c,Status__c,Enrolment_Date__c
Aarav Sharma,CS-2023-014,aarav.sharma@example.edu,Computer Engineering,6,8.85,Active,2023-08-01
Priya Patel,IT-2023-028,priya.patel@example.edu,Information Technology,6,9.40,Active,2023-08-01
Rohan Deshmukh,ME-2022-009,rohan.deshmukh@example.edu,Mechanical Engineering,8,7.65,Graduated,2022-08-05
Ananya Iyer,CE-2024-003,ananya.iyer@example.edu,Civil Engineering,4,8.95,Active,2024-08-10
Vikram Singh,ET-2023-019,vikram.singh@example.edu,Electronics & Telecommunication,5,6.80,On Leave,2023-08-01
Sneha Reddy,CS-2024-042,sneha.reddy@example.edu,Computer Engineering,4,9.75,Active,2024-08-10
Aditya Verma,IT-2022-015,aditya.verma@example.edu,Information Technology,8,8.20,Graduated,2022-08-05
Neha Kulkarni,ME-2024-011,neha.kulkarni@example.edu,Mechanical Engineering,3,7.45,Active,2024-08-10
Karan Mehta,CE-2023-033,karan.mehta@example.edu,Civil Engineering,5,5.90,Dropped,2023-08-01
Tanvi Bose,ET-2024-008,tanvi.bose@example.edu,Electronics & Telecommunication,4,9.15,Active,2024-08-10
```
