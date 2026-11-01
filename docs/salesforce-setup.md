# Salesforce Lightning App Setup & Configuration Guide

## Application Overview
- **App Name**: Admissions Cloud Management
- **Developer Name**: `Admissions_Cloud_Management`
- **Platform**: Salesforce Lightning Experience
- **Primary Object**: `Student_Inquiry__c` (Student Inquiry)
- **App Purpose**: Provides admissions officers and counselors with a consolidated cloud console to manage student leads, evaluate academic eligibility, track application funnels, and visualize admission KPIs via reports and dashboards.

---

## Step 1: Create Custom Object (`Student_Inquiry__c`)

1. Log into your Salesforce Developer Edition org (`https://login.salesforce.com`).
2. Navigate to **Setup** (gear icon in the top right corner) → **Object Manager**.
3. Click **Create** → **Custom Object**.
4. Configure the Object Definition:
   - **Label**: `Student Inquiry`
   - **Plural Label**: `Student Inquiries`
   - **Object Name**: `Student_Inquiry`
   - **Record Name**: `Inquiry Number`
   - **Data Type**: `Auto Number`
   - **Display Format**: `INQ-{YYYY}-{0000}`
   - **Starting Number**: `1`
5. Under **Optional Features**, check:
   - [x] *Allow Reports*
   - [x] *Allow Activities*
   - [x] *Track Field History*
6. Under **Deployment Status**, select **Deployed**.
7. Under **Object Creation Options**, check:
   - [x] *Launch New Custom Tab Wizard after saving this custom object*.
8. Click **Save**.

---

## Step 2: Configure the Custom Tab

1. When the New Custom Tab Wizard opens:
   - **Object**: `Student Inquiry`
   - **Tab Style**: Select **Books**, **Student**, or **Diploma** (e.g., `Custom48: Trophy` or `Custom67: Gears`).
   - **Description**: *Centralized directory for prospective student inquiries.*
2. Click **Next** → keep Tab Visibility as **Default On** for all profiles → Click **Next**.
3. Keep default custom app inclusion and click **Save**.

---

## Step 3: Add Custom Fields & Formulas

In **Object Manager** → select **Student Inquiry** → **Fields & Relationships** → **New**:

1. **First Name**:
   - Data Type: `Text` | Length: `50` | Field Label: `First Name` | Required: `Yes`
2. **Last Name**:
   - Data Type: `Text` | Length: `50` | Field Label: `Last Name` | Required: `Yes`
3. **Email Address**:
   - Data Type: `Email` | Field Label: `Email Address` | Unique: `Yes` | External ID: `Yes`
4. **Phone**:
   - Data Type: `Phone` | Field Label: `Contact Phone`
5. **City & State**:
   - Data Type: `Text(60)` for `City` and `State`
6. **Target Degree Program**:
   - Data Type: `Picklist` | Field Label: `Target Degree Program`
   - Values (Enter values, with each value on its own line):
     - `B.Tech Computer Science`
     - `B.Tech AI & Data Science`
     - `B.Tech Cyber Security`
     - `M.Tech Cloud Computing`
     - `MCA`
7. **Preferred Intake**:
   - Data Type: `Picklist` | Field Label: `Preferred Intake`
   - Values: `Fall 2026`, `Spring 2027`, `Fall 2027`
8. **High School / Prior GPA**:
   - Data Type: `Percent` | Length: `3`, Decimals: `2` | Field Label: `High School GPA`
9. **Entrance Score**:
   - Data Type: `Number` | Length: `3`, Decimals: `0` | Field Label: `Entrance Score`
10. **Merit Scholarship Eligible**:
    - Data Type: `Formula` | Formula Return Type: `Checkbox`
    - Formula:
      ```sql
      IF(High_School_GPA__c >= 0.85, TRUE, FALSE)
      ```
11. **Inquiry Status**:
    - Data Type: `Picklist` | Field Label: `Inquiry Status`
    - Values:
      - `New` (Default)
      - `Contacted`
      - `Counseling Scheduled`
      - `Application Submitted`
      - `Enrolled`
      - `Closed - Lost`
12. **Application Fee Paid**:
    - Data Type: `Checkbox` | Default: `Unchecked`
13. **Follow-Up Date**:
    - Data Type: `Date` | Field Label: `Next Follow-Up Date`
14. **Counselor Notes**:
    - Data Type: `Long Text Area` | Length: `2000` | Visible Lines: `5`

---

## Step 4: Create the Lightning Application

1. In **Setup**, enter `App Manager` in the Quick Find box and select **App Manager**.
2. Click **New Lightning App**.
3. **App Details & Branding**:
   - **App Name**: `Admissions Cloud Management`
   - **Developer Name**: `Admissions_Cloud_Management`
   - **Description**: *Admissions inquiry tracking, applicant evaluation, and enrollment dashboard.*
   - **Primary Color Hex Value**: `#6366F1` (Indigo accent)
4. Click **Next** → **App Options**: Standard navigation, Desktop and phone support.
5. Click **Next** → **Utility Items**: Add `Recent Items` and `Notes` (optional).
6. **Navigation Items**:
   - Move the following to **Selected Items**:
     1. `Home`
     2. `Student Inquiries`
     3. `Reports`
     4. `Dashboards`
7. **User Profiles**: Assign to `System Administrator` (and relevant Counselor profiles).
8. Click **Save & Finish**.

---

## Step 5: Configure Lightning Record Page & Path

1. Open the **App Launcher** (9-dot icon on top left) → select **Admissions Cloud Management**.
2. Click on the **Student Inquiries** tab → Click **New** to create a dummy record.
3. On the record page, click the **Setup** gear icon → select **Edit Page** to open the **Lightning App Builder**.
4. Drag and drop the **Path** component above the record detail.
   - Configure Path on `Inquiry_Status__c` so counselors can click through stages:
     `New` ➔ `Contacted` ➔ `Counseling Scheduled` ➔ `Application Submitted` ➔ `Enrolled`.
5. Add a **Highlights Panel** at the top with key metrics (Status, Program, Scholarship eligibility).
6. Click **Save** and **Activate** (Assign as Org Default for Desktop & Phone).

---

## Step 6: Create Analytical Reports

### Report 1: Admissions Pipeline by Status & Program
1. Go to **Reports** tab → Click **New Report**.
2. Choose Report Type: **Student Inquiries** → Click **Start Report**.
3. **Grouping**:
   - Group Rows by: `Inquiry Status`
   - Group Columns by: `Target Degree Program`
4. **Columns**: Add `First Name`, `Last Name`, `High School GPA`, `Entrance Score`, `Scholarship Eligible`.
5. Add Chart: Toggle **Chart On** → Select **Stacked Column Chart** or **Donut Chart**.
6. Click **Save & Run** → Name: `Admissions Pipeline by Status`.

### Report 2: Merit Scholarship Candidates
1. Go to **Reports** tab → Click **New Report** (Report Type: `Student Inquiries`).
2. Add Filter: `Scholarship Eligible EQUALS True`.
3. Columns: `Inquiry Number`, `Full Name`, `Target Degree`, `High School GPA`, `Email`.
4. Click **Save & Run** → Name: `Merit Scholarship Eligible Inquiries`.

---

## Step 7: Build the Executive Admissions Dashboard

1. Navigate to the **Dashboards** tab → Click **New Dashboard**.
2. **Dashboard Name**: `Admissions Operations Executive Dashboard`.
3. Add Components:
   - **Component 1 (Pipeline Funnel)**: Source Report: *Admissions Pipeline by Status* | Display as: **Funnel Chart** showing count across inquiry stages.
   - **Component 2 (Program Demand)**: Source Report: *Admissions Pipeline by Status* | Display as: **Donut Chart** categorized by *Target Degree Program*.
   - **Component 3 (Enrolled KPI Metric)**: Source Report: *Admissions Pipeline by Status* | Filter: `Status = Enrolled` | Display as: **Metric Gauge** (Target: 50 enrolled).
   - **Component 4 (Scholarship Qualified Table)**: Source Report: *Merit Scholarship Eligible Inquiries* | Display as: **Lightning Lightning Table**.
4. Click **Save** and **Done**.
