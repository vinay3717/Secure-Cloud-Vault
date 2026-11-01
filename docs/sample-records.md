# Sample Inquiry Records for Salesforce Demo

This file documents the mock dataset created for testing and demonstrating **Project #8 (Salesforce Admissions Cloud Management)**. A companion CSV file ([`sample-records.csv`](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/docs/sample-records.csv)) is available for direct import using the Salesforce Data Import Wizard.

---

## 1. Dataset Breakdown

- **Total Records**: 12
- **Programs Represented**:
  - `B.Tech Computer Science`: 3
  - `B.Tech AI & Data Science`: 3
  - `B.Tech Cyber Security`: 2
  - `M.Tech Cloud Computing`: 2
  - `MCA`: 2
- **Lifecycle Stages**:
  - `New`: 1
  - `Contacted`: 2
  - `Counseling Scheduled`: 2
  - `Application Submitted`: 3
  - `Enrolled`: 3
  - `Closed - Lost`: 1
- **Scholarship Eligible (GPA ≥ 85%)**: 7 out of 12 records qualify automatically via formula calculation.

---

## 2. Records Preview Table

| Name | City, State | Target Degree | Intake | GPA | Score | Status | Fee Paid |
|---|---|---|---|---|---|---|---|
| **Aarav Sharma** | Mumbai, MH | B.Tech Computer Science | Fall 2026 | 92.00% | 94 | Enrolled | Yes |
| **Priya Patel** | Ahmedabad, GJ | B.Tech AI & Data Science | Fall 2026 | 88.00% | 89 | Application Submitted | Yes |
| **Rohan Deshmukh** | Pune, MH | B.Tech Cyber Security | Fall 2026 | 78.00% | 82 | Counseling Scheduled | No |
| **Ananya Iyer** | Bengaluru, KA | M.Tech Cloud Computing | Spring 2027 | 95.00% | 96 | Enrolled | Yes |
| **Vikram Singh** | Jaipur, RJ | MCA | Fall 2026 | 82.00% | 79 | Contacted | No |
| **Sneha Reddy** | Hyderabad, TS | B.Tech Computer Science | Fall 2026 | 91.00% | 91 | Application Submitted | Yes |
| **Aditya Verma** | Delhi, DL | B.Tech AI & Data Science | Spring 2027 | 86.00% | 85 | New | No |
| **Neha Kulkarni** | Nagpur, MH | M.Tech Cloud Computing | Fall 2026 | 89.00% | 88 | Counseling Scheduled | No |
| **Karan Mehta** | Surat, GJ | B.Tech Cyber Security | Fall 2026 | 72.00% | 68 | Closed - Lost | No |
| **Tanvi Bose** | Kolkata, WB | MCA | Fall 2026 | 87.00% | 83 | Enrolled | Yes |
| **Rahul Nair** | Kochi, KL | B.Tech Computer Science | Fall 2026 | 84.00% | 81 | Contacted | No |
| **Diya Choudhary** | Chandigarh, PB | B.Tech AI & Data Science | Fall 2027 | 93.00% | 92 | Application Submitted | Yes |

---

## 3. How to Import Records into Salesforce

1. Go to **Setup** → search for `Data Import Wizard` → Click **Launch Wizard!**.
2. Select **Custom Objects** tab → Choose **Student Inquiries**.
3. Select **Add new records**.
4. In **Where is your data located?**, drag and drop [`docs/sample-records.csv`](file:///c:/Users/Vinay%20Umesh%20Gole/Desktop/CC_Project/docs/sample-records.csv).
5. Click **Next** → verify field mapping:
   - `First_Name__c` ➔ `First Name`
   - `Last_Name__c` ➔ `Last Name`
   - `Email__c` ➔ `Email Address`
   - `Target_Degree__c` ➔ `Target Degree Program`
   - `High_School_GPA__c` ➔ `High School GPA`
   - `Inquiry_Status__c` ➔ `Inquiry Status`
6. Click **Next** → Click **Start Import**.
7. Navigate to the **Student Inquiries** tab in the Admissions Cloud app to verify that all records appear with their calculated auto-numbers (`INQ-2026-0001` through `INQ-2026-0012`).
