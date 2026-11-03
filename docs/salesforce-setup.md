# Salesforce Lightning App Setup & Configuration Guide

## Application Overview
- **App Name**: Student Record Manager
- **Developer Name**: `Student_Record_Manager`
- **App Type**: Lightning App (Standard Navigation)
- **Primary Object**: `Student_Record__c` (Student Record)
- **Included Navigation Items**:
  1. `Student Records` (`Student_Record__c` Custom Tab)
  2. `Reports` (Standard Tab)
  3. `Dashboards` (Standard Tab)
- **Target Audience / Profiles**: System Administrator, Academic Registrar, Faculty Advisors, Department HODs.
- **App Description**: A specialized cloud academic records solution built on Salesforce Lightning Experience for college administrators to track student enrolment, department allocation, term progression, and cumulative GPA analytics.

---

## Step 1: Create the Custom Object (`Student_Record__c`)

1. Log into your Salesforce Developer Edition org (`https://login.salesforce.com`).
2. Click the **Setup (Gear Icon)** in the top navigation bar and select **Setup**.
3. Select the **Object Manager** tab at the top of the Setup page.
4. Click **Create** (top right) → select **Custom Object**.
5. Fill in the object definitions:
   - **Label**: `Student Record`
   - **Plural Label**: `Student Records`
   - **Object Name**: `Student_Record`
   - **Description**: *Central repository for student profiles, academic enrolment, term GPA, and active standing.*
   - **Record Name**: `Student Name`
   - **Data Type**: `Text`
6. Under **Optional Features**, check the following boxes:
   - [x] **Allow Reports** (required for academic reporting & dashboard widgets)
   - [x] **Allow Activities** (for scheduling advisory sessions)
   - [x] **Track Field History** (for auditing status and GPA adjustments)
7. Under **Deployment Status**, ensure **Deployed** is selected.
8. Under **Object Creation Options (Available only when first creating the Custom Object)**:
   - [x] Check **Launch New Custom Tab Wizard after saving this custom object**.
9. Click **Save**.

---

## Step 2: Configure the Custom Tab

1. The **New Custom Tab Wizard** will automatically open.
2. Select the tab properties:
   - **Object**: `Student Record`
   - **Tab Style**: Select **Books** (`Custom48: Trophy` or `Custom62: Chalkboard` or `Custom67: Gears`).
   - **Description**: *Tab interface providing direct access to student academic records.*
3. Click **Next**.
4. Set tab visibility: keep **Default On** for all profiles → Click **Next**.
5. Keep default custom app inclusions and click **Save**.

---

## Step 3: Add Custom Fields & Relationships

In **Object Manager** → click **Student Record** → select **Fields & Relationships** → click **New**:

### Field 1: Roll Number
- **Data Type**: `Text`
- **Field Label**: `Roll Number`
- **Length**: `20`
- **Field Name**: `Roll_Number`
- **Required**: Check [x] *Always require a value in this field in order to save a record*
- **Unique**: Check [x] *Do not allow duplicate values* → Select *Treat "ABC" and "abc" as duplicate values (case-insensitive)*
- **External ID**: Check [x] *Set this field as the unique record identifier from an external system*
- Click **Next** → **Next** → **Save & New**.

### Field 2: Email
- **Data Type**: `Email`
- **Field Label**: `Email`
- **Field Name**: `Email`
- **Required**: Check [x] *Always require a value in this field*
- Click **Next** → **Next** → **Save & New**.

### Field 3: Course
- **Data Type**: `Picklist`
- **Field Label**: `Course`
- **Field Name**: `Course`
- Select **Enter values, with each value on its own line**:
  ```text
  Computer Engineering
  Information Technology
  Mechanical Engineering
  Civil Engineering
  Electronics & Telecommunication
  ```
- **Required**: Check [x] *Always require a value in this field*
- Click **Next** → **Next** → **Save & New**.

### Field 4: Semester
- **Data Type**: `Number`
- **Field Label**: `Semester`
- **Length**: `2`, **Decimal Places**: `0`
- **Field Name**: `Semester`
- **Required**: Check [x] *Always require a value in this field*
- Click **Next** → **Next** → **Save & New**.

### Field 5: GPA
- **Data Type**: `Number`
- **Field Label**: `GPA`
- **Length**: `3`, **Decimal Places**: `2`
- **Field Name**: `GPA`
- **Required**: Check [x] *Always require a value in this field*
- Click **Next** → **Next** → **Save & New**.

### Field 6: Status
- **Data Type**: `Picklist`
- **Field Label**: `Status`
- **Field Name**: `Status`
- Select **Enter values, with each value on its own line**:
  ```text
  Active
  On Leave
  Graduated
  Dropped
  ```
- Set default value to **Active**.
- **Required**: Check [x] *Always require a value in this field*
- Click **Next** → **Next** → **Save & New**.

### Field 7: Enrolment Date
- **Data Type**: `Date`
- **Field Label**: `Enrolment Date`
- **Field Name**: `Enrolment_Date`
- **Required**: Check [x] *Always require a value in this field*
- Click **Next** → **Next** → **Save**.

---

## Step 4: Configure the Validation Rule (`VR_GPA_Range`)

1. In **Object Manager** → select **Student Record**.
2. In the left navigation sidebar, scroll down and click **Validation Rules**.
3. Click **New** (top right).
4. Configure the rule parameters:
   - **Rule Name**: `VR_GPA_Range`
   - **Active**: Check [x]
   - **Description**: *Validates that GPA is strictly within the academic range of 0.00 to 10.00.*
   - **Error Condition Formula**:
     ```sql
     OR(
         GPA__c < 0.00,
         GPA__c > 10.00
     )
     ```
   - **Error Message**: `GPA must be between 0.00 and 10.00.`
   - **Error Location**: Select **Field** → `GPA`.
5. Click **Save**.

---

## Step 5: Build the Lightning App ("Student Record Manager")

1. From **Setup**, in the Quick Find search box on the left, type `App Manager` and select **App Manager**.
2. Click **New Lightning App** (top right).
3. **App Details & Branding**:
   - **App Name**: `Student Record Manager`
   - **Developer Name**: `Student_Record_Manager`
   - **Description**: *Academic management console for tracking student registrations, courses, semester progression, and GPA metrics.*
   - **Primary Color Hex**: `#1E88E5` (Salesforce Blue)
   - Click **Next**.
4. **App Options**:
   - **Navigation Style**: Standard Navigation
   - **Supported Form Factors**: Desktop and Phone
   - Click **Next**.
5. **Utility Items (Desktop Only)**:
   - Keep default (none required) → Click **Next**.
6. **Navigation Items**:
   - In the **Available Items** column, select and move the following to **Selected Items**:
     1. `Student Records` (Custom Tab)
     2. `Reports` (Standard Tab)
     3. `Dashboards` (Standard Tab)
   - Click **Next**.
7. **User Profiles**:
   - Select and move **System Administrator** and **Standard User** to **Selected Profiles**.
8. Click **Save & Finish**.

---

## Step 6: Customize the Page Layout

1. In **Object Manager** → **Student Record** → **Page Layouts** → click **Student Record Layout**.
2. Organize the fields into logical sections:
   - **Student Identity & Registration**: `Student Name`, `Roll Number`, `Email`, `Enrolment Date`, `Status`.
   - **Academic Details & Performance**: `Course`, `Semester`, `GPA`.
   - **System Information**: `Owner`, `Created By`, `Last Modified By`.
3. Click **Save**.

---

## Step 7: Launch the Application

1. Click the **App Launcher** (9 dots icon in the top left header).
2. Type `Student Record Manager` and click the application card.
3. The Lightning App opens with the three primary tabs: `Student Records`, `Reports`, and `Dashboards`.
