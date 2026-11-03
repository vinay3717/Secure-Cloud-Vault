import os
from playwright.sync_api import sync_playwright

output_dir = os.path.abspath("screenshots/salesforce")
os.makedirs(output_dir, exist_ok=True)

# Common SLDS Styling & Header helper
def get_slds_base():
    return """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/design-system/2.22.1/styles/salesforce-lightning-design-system.min.css" />
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #b0c4df;
            margin: 0;
            padding: 0;
            color: #181818;
            -webkit-font-smoothing: antialiased;
        }
        .global-header {
            background-color: #ffffff;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 16px;
            border-bottom: 1px solid #dddbda;
            box-shadow: 0 2px 4px rgba(0,0,0,0.07);
        }
        .global-header .logo-area {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .app-launcher {
            width: 24px;
            height: 24px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3px;
            cursor: pointer;
        }
        .app-launcher div {
            background: #706e6b;
            border-radius: 2px;
        }
        .cloud-logo {
            font-size: 16px;
            font-weight: 700;
            color: #0176d3;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .search-box {
            background: #f3f3f3;
            border: 1px solid #c9c7c5;
            border-radius: 4px;
            padding: 6px 14px;
            width: 380px;
            font-size: 13px;
            color: #706e6b;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .user-profile {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #65cae4;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 13px;
        }
        .nav-bar {
            background: #0176d3;
            height: 44px;
            display: flex;
            align-items: center;
            padding: 0 20px;
            gap: 24px;
            color: white;
            font-size: 14px;
            font-weight: 500;
        }
        .nav-item {
            padding: 10px 12px;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .nav-item.active {
            border-bottom: 3px solid #ffffff;
            font-weight: 700;
        }
        .main-container {
            padding: 16px 20px 24px 20px;
        }
        .card {
            background: white;
            border-radius: 6px;
            border: 1px solid #dddbda;
            box-shadow: 0 2px 2px rgba(0,0,0,0.05);
            overflow: hidden;
        }
        .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }
        .badge-active { background: #e0f5ea; color: #0b8043; border: 1px solid #a8dab5; }
        .badge-graduated { background: #e8f0fe; color: #1a73e8; border: 1px solid #aecbfa; }
        .badge-leave { background: #fef7e0; color: #b06000; border: 1px solid #fdd663; }
        .badge-dropped { background: #fce8e6; color: #c5221f; border: 1px solid #f6aea9; }
    </style>
    """

def generate_report_screenshot(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Salesforce Report</title>
        {get_slds_base()}
    </head>
    <body>
        <div class="global-header">
            <div class="logo-area">
                <div class="app-launcher"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                <div class="cloud-logo">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0176d3"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>
                    Student Record Manager
                </div>
            </div>
            <div class="search-box">🔍 Search Student Records, Reports, Dashboards...</div>
            <div class="user-profile">
                <span style="font-size: 13px; color: #444;">Vinay Gole (Admin)</span>
                <div class="avatar">VG</div>
            </div>
        </div>
        <div class="nav-bar">
            <div class="nav-item">Student Records</div>
            <div class="nav-item active">Reports ▼</div>
            <div class="nav-item">Dashboards</div>
        </div>

        <div class="main-container">
            <div class="card" style="padding: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div>
                        <div style="font-size: 12px; color: #706e6b; text-transform: uppercase; font-weight: 700;">Report: Student Academic Records</div>
                        <h1 style="font-size: 20px; font-weight: 700; margin: 4px 0 0 0; color: #0176d3;">Academic Performance & GPA Summary by Course</h1>
                        <p style="font-size: 13px; color: #706e6b; margin: 4px 0 0 0;">Grouped by Course & Status • Evaluated on 10.00 Scale • Total 10 Enrolled Records</p>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <button style="background: white; border: 1px solid #c9c7c5; padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600;">Export</button>
                        <button style="background: #0176d3; color: white; border: none; padding: 6px 16px; border-radius: 4px; font-size: 13px; font-weight: 600;">Edit Report</button>
                    </div>
                </div>

                <!-- KPI Summary ribbon -->
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 20px;">
                    <div style="background: #f8f9fa; border: 1px solid #e5e5e5; padding: 14px; border-radius: 6px;">
                        <div style="font-size: 11px; color: #706e6b; font-weight: 700; text-transform: uppercase;">Total Students</div>
                        <div style="font-size: 26px; font-weight: 800; color: #181818; margin-top: 4px;">10</div>
                    </div>
                    <div style="background: #f8f9fa; border: 1px solid #e5e5e5; padding: 14px; border-radius: 6px;">
                        <div style="font-size: 11px; color: #706e6b; font-weight: 700; text-transform: uppercase;">Institutional Average GPA</div>
                        <div style="font-size: 26px; font-weight: 800; color: #0b8043; margin-top: 4px;">8.21 <span style="font-size: 14px; font-weight: 500; color: #706e6b;">/ 10.00</span></div>
                    </div>
                    <div style="background: #f8f9fa; border: 1px solid #e5e5e5; padding: 14px; border-radius: 6px;">
                        <div style="font-size: 11px; color: #706e6b; font-weight: 700; text-transform: uppercase;">Highest Recorded GPA</div>
                        <div style="font-size: 26px; font-weight: 800; color: #0176d3; margin-top: 4px;">9.75 <span style="font-size: 13px; color: #706e6b; font-weight: normal;">(Sneha Reddy)</span></div>
                    </div>
                    <div style="background: #f8f9fa; border: 1px solid #e5e5e5; padding: 14px; border-radius: 6px;">
                        <div style="font-size: 11px; color: #706e6b; font-weight: 700; text-transform: uppercase;">Active Rate</div>
                        <div style="font-size: 26px; font-weight: 800; color: #1a73e8; margin-top: 4px;">60% <span style="font-size: 13px; color: #706e6b; font-weight: normal;">(6 Active)</span></div>
                    </div>
                </div>

                <!-- Report Summary Table -->
                <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
                    <thead>
                        <tr style="background: #fafaf9; border-bottom: 2px solid #dddbda; text-align: left; color: #514f4d;">
                            <th style="padding: 10px 12px;">STUDENT NAME</th>
                            <th style="padding: 10px 12px;">ROLL NUMBER</th>
                            <th style="padding: 10px 12px;">EMAIL</th>
                            <th style="padding: 10px 12px;">COURSE</th>
                            <th style="padding: 10px 12px;">SEMESTER</th>
                            <th style="padding: 10px 12px;">GPA</th>
                            <th style="padding: 10px 12px;">STATUS</th>
                            <th style="padding: 10px 12px;">ENROLMENT DATE</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Group 1: Computer Engineering -->
                        <tr style="background: #f3f2f2; font-weight: 700; border-top: 1px solid #dddbda;">
                            <td colspan="5" style="padding: 8px 12px; color: #0176d3;">Course: Computer Engineering (2 Records)</td>
                            <td style="padding: 8px 12px; color: #0b8043;">Avg: 9.30</td>
                            <td colspan="2"></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Sneha Reddy</td>
                            <td style="padding: 9px 12px;">CS-2024-042</td>
                            <td style="padding: 9px 12px;">sneha.reddy@example.edu</td>
                            <td style="padding: 9px 12px;">Computer Engineering</td>
                            <td style="padding: 9px 12px;">Semester 4</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #0b8043;">9.75</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-active">Active</span></td>
                            <td style="padding: 9px 12px;">2024-08-10</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Aarav Sharma</td>
                            <td style="padding: 9px 12px;">CS-2023-014</td>
                            <td style="padding: 9px 12px;">aarav.sharma@example.edu</td>
                            <td style="padding: 9px 12px;">Computer Engineering</td>
                            <td style="padding: 9px 12px;">Semester 6</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #0b8043;">8.85</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-active">Active</span></td>
                            <td style="padding: 9px 12px;">2023-08-01</td>
                        </tr>

                        <!-- Group 2: Information Technology -->
                        <tr style="background: #f3f2f2; font-weight: 700; border-top: 1px solid #dddbda;">
                            <td colspan="5" style="padding: 8px 12px; color: #0176d3;">Course: Information Technology (2 Records)</td>
                            <td style="padding: 8px 12px; color: #0b8043;">Avg: 8.80</td>
                            <td colspan="2"></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Priya Patel</td>
                            <td style="padding: 9px 12px;">IT-2023-028</td>
                            <td style="padding: 9px 12px;">priya.patel@example.edu</td>
                            <td style="padding: 9px 12px;">Information Technology</td>
                            <td style="padding: 9px 12px;">Semester 6</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #0b8043;">9.40</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-active">Active</span></td>
                            <td style="padding: 9px 12px;">2023-08-01</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Aditya Verma</td>
                            <td style="padding: 9px 12px;">IT-2022-015</td>
                            <td style="padding: 9px 12px;">aditya.verma@example.edu</td>
                            <td style="padding: 9px 12px;">Information Technology</td>
                            <td style="padding: 9px 12px;">Semester 8</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #0b8043;">8.20</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-graduated">Graduated</span></td>
                            <td style="padding: 9px 12px;">2022-08-05</td>
                        </tr>

                        <!-- Group 3: Electronics & Telecommunication -->
                        <tr style="background: #f3f2f2; font-weight: 700; border-top: 1px solid #dddbda;">
                            <td colspan="5" style="padding: 8px 12px; color: #0176d3;">Course: Electronics & Telecommunication (2 Records)</td>
                            <td style="padding: 8px 12px; color: #0b8043;">Avg: 7.98</td>
                            <td colspan="2"></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Tanvi Bose</td>
                            <td style="padding: 9px 12px;">ET-2024-008</td>
                            <td style="padding: 9px 12px;">tanvi.bose@example.edu</td>
                            <td style="padding: 9px 12px;">Electronics & Telecommunication</td>
                            <td style="padding: 9px 12px;">Semester 4</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #0b8043;">9.15</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-active">Active</span></td>
                            <td style="padding: 9px 12px;">2024-08-10</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Vikram Singh</td>
                            <td style="padding: 9px 12px;">ET-2023-019</td>
                            <td style="padding: 9px 12px;">vikram.singh@example.edu</td>
                            <td style="padding: 9px 12px;">Electronics & Telecommunication</td>
                            <td style="padding: 9px 12px;">Semester 5</td>
                            <td style="padding: 9px 12px; font-weight: 700;">6.80</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-leave">On Leave</span></td>
                            <td style="padding: 9px 12px;">2023-08-01</td>
                        </tr>

                        <!-- Group 4: Mechanical Engineering -->
                        <tr style="background: #f3f2f2; font-weight: 700; border-top: 1px solid #dddbda;">
                            <td colspan="5" style="padding: 8px 12px; color: #0176d3;">Course: Mechanical Engineering (2 Records)</td>
                            <td style="padding: 8px 12px; color: #0b8043;">Avg: 7.55</td>
                            <td colspan="2"></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Rohan Deshmukh</td>
                            <td style="padding: 9px 12px;">ME-2022-009</td>
                            <td style="padding: 9px 12px;">rohan.deshmukh@example.edu</td>
                            <td style="padding: 9px 12px;">Mechanical Engineering</td>
                            <td style="padding: 9px 12px;">Semester 8</td>
                            <td style="padding: 9px 12px; font-weight: 700;">7.65</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-graduated">Graduated</span></td>
                            <td style="padding: 9px 12px;">2022-08-05</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Neha Kulkarni</td>
                            <td style="padding: 9px 12px;">ME-2024-011</td>
                            <td style="padding: 9px 12px;">neha.kulkarni@example.edu</td>
                            <td style="padding: 9px 12px;">Mechanical Engineering</td>
                            <td style="padding: 9px 12px;">Semester 3</td>
                            <td style="padding: 9px 12px; font-weight: 700;">7.45</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-active">Active</span></td>
                            <td style="padding: 9px 12px;">2024-08-10</td>
                        </tr>

                        <!-- Group 5: Civil Engineering -->
                        <tr style="background: #f3f2f2; font-weight: 700; border-top: 1px solid #dddbda;">
                            <td colspan="5" style="padding: 8px 12px; color: #0176d3;">Course: Civil Engineering (2 Records)</td>
                            <td style="padding: 8px 12px; color: #0b8043;">Avg: 7.43</td>
                            <td colspan="2"></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Ananya Iyer</td>
                            <td style="padding: 9px 12px;">CE-2024-003</td>
                            <td style="padding: 9px 12px;">ananya.iyer@example.edu</td>
                            <td style="padding: 9px 12px;">Civil Engineering</td>
                            <td style="padding: 9px 12px;">Semester 4</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #0b8043;">8.95</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-active">Active</span></td>
                            <td style="padding: 9px 12px;">2024-08-10</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #dddbda;">
                            <td style="padding: 9px 12px; font-weight: 600;">Karan Mehta</td>
                            <td style="padding: 9px 12px;">CE-2023-033</td>
                            <td style="padding: 9px 12px;">karan.mehta@example.edu</td>
                            <td style="padding: 9px 12px;">Civil Engineering</td>
                            <td style="padding: 9px 12px;">Semester 5</td>
                            <td style="padding: 9px 12px; font-weight: 700; color: #c5221f;">5.90</td>
                            <td style="padding: 9px 12px;"><span class="badge badge-dropped">Dropped</span></td>
                            <td style="padding: 9px 12px;">2023-08-01</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1280, "height": 840})
    page.set_content(html)
    page.wait_for_timeout(500)
    path = os.path.join(output_dir, "03_pipeline_report.png")
    page.screenshot(path=path)
    print("Generated:", path)

def generate_dashboard_screenshot(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Salesforce Dashboard</title>
        {get_slds_base()}
    </head>
    <body>
        <div class="global-header">
            <div class="logo-area">
                <div class="app-launcher"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                <div class="cloud-logo">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0176d3"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>
                    Student Record Manager
                </div>
            </div>
            <div class="search-box">🔍 Search Student Records, Reports, Dashboards...</div>
            <div class="user-profile">
                <span style="font-size: 13px; color: #444;">Vinay Gole (Admin)</span>
                <div class="avatar">VG</div>
            </div>
        </div>
        <div class="nav-bar">
            <div class="nav-item">Student Records</div>
            <div class="nav-item">Reports</div>
            <div class="nav-item active">Dashboards ▼</div>
        </div>

        <div class="main-container">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                <div>
                    <div style="font-size: 12px; color: #514f4d; text-transform: uppercase; font-weight: 700;">Dashboard</div>
                    <h1 style="font-size: 22px; font-weight: 700; margin: 2px 0 0 0; color: #080707;">Student Record Manager — Executive Analytics</h1>
                    <div style="font-size: 12px; color: #706e6b; margin-top: 3px;">As of Today at 08:30 AM • Viewing as Vinay Gole</div>
                </div>
                <div style="display: flex; gap: 8px;">
                    <button style="background: white; border: 1px solid #c9c7c5; padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600;">Refresh</button>
                    <button style="background: #0176d3; color: white; border: none; padding: 6px 16px; border-radius: 4px; font-size: 13px; font-weight: 600;">Edit</button>
                </div>
            </div>

            <!-- Dashboard Grid -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
                <!-- Component 1: Average GPA by Department -->
                <div class="card" style="padding: 16px; grid-column: span 2;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <span style="font-size: 14px; font-weight: 700; color: #080707;">Average GPA by Academic Course</span>
                        <span style="font-size: 12px; color: #0176d3; cursor: pointer;">View Report</span>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 8px;">
                        <div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px;">
                                <span style="font-weight: 600;">Computer Engineering</span>
                                <span style="font-weight: 700; color: #0b8043;">9.30 / 10.00</span>
                            </div>
                            <div style="background: #f1f3f4; height: 16px; border-radius: 4px; overflow: hidden;">
                                <div style="background: #0176d3; width: 93%; height: 100%; border-radius: 4px;"></div>
                            </div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px;">
                                <span style="font-weight: 600;">Information Technology</span>
                                <span style="font-weight: 700; color: #0b8043;">8.80 / 10.00</span>
                            </div>
                            <div style="background: #f1f3f4; height: 16px; border-radius: 4px; overflow: hidden;">
                                <div style="background: #1b96ff; width: 88%; height: 100%; border-radius: 4px;"></div>
                            </div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px;">
                                <span style="font-weight: 600;">Electronics & Telecommunication</span>
                                <span style="font-weight: 700; color: #0b8043;">7.98 / 10.00</span>
                            </div>
                            <div style="background: #f1f3f4; height: 16px; border-radius: 4px; overflow: hidden;">
                                <div style="background: #2e844a; width: 79.8%; height: 100%; border-radius: 4px;"></div>
                            </div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px;">
                                <span style="font-weight: 600;">Mechanical Engineering</span>
                                <span style="font-weight: 700; color: #514f4d;">7.55 / 10.00</span>
                            </div>
                            <div style="background: #f1f3f4; height: 16px; border-radius: 4px; overflow: hidden;">
                                <div style="background: #fe9339; width: 75.5%; height: 100%; border-radius: 4px;"></div>
                            </div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px;">
                                <span style="font-weight: 600;">Civil Engineering</span>
                                <span style="font-weight: 700; color: #514f4d;">7.43 / 10.00</span>
                            </div>
                            <div style="background: #f1f3f4; height: 16px; border-radius: 4px; overflow: hidden;">
                                <div style="background: #8e030f; width: 74.3%; height: 100%; border-radius: 4px;"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Component 2: Key Metric Cards -->
                <div style="display: flex; flex-direction: column; gap: 16px;">
                    <div class="card" style="padding: 18px; text-align: center;">
                        <div style="font-size: 12px; color: #706e6b; font-weight: 700; text-transform: uppercase;">Overall Institutional GPA</div>
                        <div style="font-size: 38px; font-weight: 900; color: #0176d3; margin: 8px 0 4px 0;">8.21</div>
                        <div style="font-size: 12px; color: #0b8043; font-weight: 600;">▲ +0.34 above target threshold (7.80)</div>
                    </div>
                    <div class="card" style="padding: 18px; text-align: center;">
                        <div style="font-size: 12px; color: #706e6b; font-weight: 700; text-transform: uppercase;">Total Active Cohort</div>
                        <div style="font-size: 38px; font-weight: 900; color: #181818; margin: 8px 0 4px 0;">10</div>
                        <div style="font-size: 12px; color: #706e6b;">100% Validation Rule Conformance</div>
                    </div>
                </div>

                <!-- Component 3: Status Distribution Donut -->
                <div class="card" style="padding: 16px;">
                    <div style="font-size: 14px; font-weight: 700; color: #080707; margin-bottom: 12px;">Enrollment Status Breakdown</div>
                    <div style="display: flex; align-items: center; justify-content: center; height: 140px;">
                        <svg width="130" height="130" viewBox="0 0 42 42">
                            <circle cx="21" cy="21" r="15.9" fill="transparent" stroke="#0b8043" stroke-width="6" stroke-dasharray="60 40" stroke-dashoffset="25"></circle>
                            <circle cx="21" cy="21" r="15.9" fill="transparent" stroke="#1a73e8" stroke-width="6" stroke-dasharray="20 80" stroke-dashoffset="-35"></circle>
                            <circle cx="21" cy="21" r="15.9" fill="transparent" stroke="#fdd663" stroke-width="6" stroke-dasharray="10 90" stroke-dashoffset="-55"></circle>
                            <circle cx="21" cy="21" r="15.9" fill="transparent" stroke="#c5221f" stroke-width="6" stroke-dasharray="10 90" stroke-dashoffset="-65"></circle>
                            <g text-anchor="middle">
                                <text x="21" y="22" font-size="6" font-weight="bold" fill="#181818">10</text>
                                <text x="21" y="27" font-size="3" fill="#706e6b">Students</text>
                            </g>
                        </svg>
                    </div>
                    <div style="font-size: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-top: 8px;">
                        <div><span style="color: #0b8043; font-weight: bold;">●</span> Active: <b>6 (60%)</b></div>
                        <div><span style="color: #1a73e8; font-weight: bold;">●</span> Graduated: <b>2 (20%)</b></div>
                        <div><span style="color: #fdd663; font-weight: bold;">●</span> On Leave: <b>1 (10%)</b></div>
                        <div><span style="color: #c5221f; font-weight: bold;">●</span> Dropped: <b>1 (10%)</b></div>
                    </div>
                </div>

                <!-- Component 4: Term Progression Distribution -->
                <div class="card" style="padding: 16px; grid-column: span 2;">
                    <div style="font-size: 14px; font-weight: 700; color: #080707; margin-bottom: 12px;">Semester Progression Overview</div>
                    <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                        <tr style="background: #fafaf9; border-bottom: 1px solid #dddbda; color: #514f4d; text-align: left;">
                            <th style="padding: 6px;">SEMESTER</th>
                            <th style="padding: 6px;">ENROLLED STUDENTS</th>
                            <th style="padding: 6px;">DEPARTMENTS</th>
                            <th style="padding: 6px;">AVERAGE GPA</th>
                            <th style="padding: 6px;">STATUS STANDING</th>
                        </tr>
                        <tr style="border-bottom: 1px solid #f3f2f2;">
                            <td style="padding: 6px; font-weight: 600;">Semester 4</td>
                            <td style="padding: 6px;">3 students</td>
                            <td style="padding: 6px;">CS, CE, ET</td>
                            <td style="padding: 6px; font-weight: 700; color: #0b8043;">9.28</td>
                            <td style="padding: 6px;"><span class="badge badge-active">All Active</span></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #f3f2f2;">
                            <td style="padding: 6px; font-weight: 600;">Semester 6</td>
                            <td style="padding: 6px;">2 students</td>
                            <td style="padding: 6px;">CS, IT</td>
                            <td style="padding: 6px; font-weight: 700; color: #0b8043;">9.12</td>
                            <td style="padding: 6px;"><span class="badge badge-active">All Active</span></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #f3f2f2;">
                            <td style="padding: 6px; font-weight: 600;">Semester 8</td>
                            <td style="padding: 6px;">2 students</td>
                            <td style="padding: 6px;">IT, ME</td>
                            <td style="padding: 6px; font-weight: 700;">7.92</td>
                            <td style="padding: 6px;"><span class="badge badge-graduated">Completed</span></td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1280, "height": 840})
    page.set_content(html)
    page.wait_for_timeout(500)
    path = os.path.join(output_dir, "04_executive_dashboard.png")
    page.screenshot(path=path)
    print("Generated:", path)

def generate_schema_screenshot(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Salesforce Object Manager</title>
        {get_slds_base()}
    </head>
    <body>
        <div class="global-header">
            <div class="logo-area">
                <div class="app-launcher"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                <div class="cloud-logo">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0176d3"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>
                    Setup
                </div>
            </div>
            <div class="search-box">🔍 Quick Find / Object Manager...</div>
            <div class="user-profile">
                <span style="font-size: 13px; color: #444;">Vinay Gole (System Administrator)</span>
                <div class="avatar">VG</div>
            </div>
        </div>
        <div class="nav-bar" style="background: #16325c;">
            <div class="nav-item">Home</div>
            <div class="nav-item active">Object Manager</div>
        </div>

        <div class="main-container">
            <div class="card" style="display: flex; min-height: 580px;">
                <!-- Left Subnav -->
                <div style="width: 240px; border-right: 1px solid #dddbda; background: #fafaf9; padding: 16px 0;">
                    <div style="padding: 0 16px 12px 16px; border-bottom: 1px solid #dddbda;">
                        <div style="font-size: 11px; color: #706e6b; text-transform: uppercase; font-weight: 700;">Custom Object</div>
                        <div style="font-size: 18px; font-weight: 700; color: #080707;">Student Record</div>
                        <div style="font-size: 12px; color: #0176d3; font-family: monospace;">Student_Record__c</div>
                    </div>
                    <div style="display: flex; flex-direction: column; margin-top: 8px;">
                        <div style="padding: 10px 16px; font-size: 13px; color: #514f4d; cursor: pointer;">Details</div>
                        <div style="padding: 10px 16px; font-size: 13px; font-weight: 700; color: #0176d3; background: #ecebea; border-left: 3px solid #0176d3;">Fields & Relationships (7)</div>
                        <div style="padding: 10px 16px; font-size: 13px; color: #514f4d; cursor: pointer;">Page Layouts</div>
                        <div style="padding: 10px 16px; font-size: 13px; color: #514f4d; cursor: pointer;">Lightning Record Pages</div>
                        <div style="padding: 10px 16px; font-size: 13px; color: #514f4d; cursor: pointer;">Buttons, Links, and Actions</div>
                        <div style="padding: 10px 16px; font-size: 13px; color: #514f4d; cursor: pointer;">Validation Rules (1)</div>
                    </div>
                </div>

                <!-- Right Table -->
                <div style="flex: 1; padding: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                        <div>
                            <h2 style="font-size: 18px; font-weight: 700; margin: 0; color: #080707;">Fields & Relationships</h2>
                            <p style="font-size: 12px; color: #706e6b; margin: 2px 0 0 0;">7 Custom Fields • Standard Record Name: Student Name (Text)</p>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button style="background: #0176d3; color: white; border: none; padding: 6px 16px; border-radius: 4px; font-size: 13px; font-weight: 600;">New</button>
                            <button style="background: white; border: 1px solid #c9c7c5; padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600;">Field Dependencies</button>
                        </div>
                    </div>

                    <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
                        <thead>
                            <tr style="background: #fafaf9; border-bottom: 2px solid #dddbda; text-align: left; color: #514f4d;">
                                <th style="padding: 8px 12px;">FIELD LABEL</th>
                                <th style="padding: 8px 12px;">FIELD NAME (API)</th>
                                <th style="padding: 8px 12px;">DATA TYPE</th>
                                <th style="padding: 8px 12px;">CONTROLLING FIELD</th>
                                <th style="padding: 8px 12px;">INDEXED</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Student Name</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Name</td>
                                <td style="padding: 9px 12px;">Text(80)</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px; color: #0b8043;">✓ Standard</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Roll Number</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Roll_Number__c</td>
                                <td style="padding: 9px 12px;">Text(20) (Unique, External ID)</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px; color: #0b8043;">✓ Indexed</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Email</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Email__c</td>
                                <td style="padding: 9px 12px;">Email</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px;">—</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Course</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Course__c</td>
                                <td style="padding: 9px 12px;">Picklist (5 values)</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px;">—</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Semester</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Semester__c</td>
                                <td style="padding: 9px 12px;">Number(2, 0)</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px;">—</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">GPA</td>
                                <td style="padding: 9px 12px; font-family: monospace;">GPA__c</td>
                                <td style="padding: 9px 12px;">Number(3, 2)</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px; color: #0176d3;">VR01 (0.00-10.00)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Status</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Status__c</td>
                                <td style="padding: 9px 12px;">Picklist (Active, On Leave, Graduated, Dropped)</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px;">—</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #dddbda;">
                                <td style="padding: 9px 12px; font-weight: 600; color: #0176d3;">Enrolment Date</td>
                                <td style="padding: 9px 12px; font-family: monospace;">Enrolment_Date__c</td>
                                <td style="padding: 9px 12px;">Date</td>
                                <td style="padding: 9px 12px;">—</td>
                                <td style="padding: 9px 12px;">—</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1280, "height": 840})
    page.set_content(html)
    page.wait_for_timeout(500)
    path = os.path.join(output_dir, "01_custom_object_schema.png")
    page.screenshot(path=path)
    print("Generated:", path)

def generate_record_detail_screenshot(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Salesforce Record Detail</title>
        {get_slds_base()}
    </head>
    <body>
        <div class="global-header">
            <div class="logo-area">
                <div class="app-launcher"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                <div class="cloud-logo">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0176d3"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>
                    Student Record Manager
                </div>
            </div>
            <div class="search-box">🔍 Search Student Records, Reports, Dashboards...</div>
            <div class="user-profile">
                <span style="font-size: 13px; color: #444;">Vinay Gole (Admin)</span>
                <div class="avatar">VG</div>
            </div>
        </div>
        <div class="nav-bar">
            <div class="nav-item active">Student Records ▼</div>
            <div class="nav-item">Reports</div>
            <div class="nav-item">Dashboards</div>
        </div>

        <div class="main-container">
            <!-- Highlights Panel -->
            <div class="card" style="padding: 16px 20px; margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div style="display: flex; gap: 14px; align-items: center;">
                        <div style="background: #e0f5ea; width: 44px; height: 44px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 22px;">
                            🎓
                        </div>
                        <div>
                            <div style="font-size: 12px; color: #706e6b; text-transform: uppercase; font-weight: 700;">Student Record</div>
                            <h1 style="font-size: 22px; font-weight: 800; margin: 2px 0; color: #080707;">Aarav Sharma</h1>
                            <div style="font-size: 12px; color: #0176d3;">Roll: CS-2023-014 • Computer Engineering</div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <button style="background: white; border: 1px solid #c9c7c5; padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600;">Edit</button>
                        <button style="background: white; border: 1px solid #c9c7c5; padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600;">Delete</button>
                        <button style="background: #0176d3; color: white; border: none; padding: 6px 16px; border-radius: 4px; font-size: 13px; font-weight: 600;">Generate Transcript</button>
                    </div>
                </div>

                <!-- Highlights Fields -->
                <div style="display: flex; gap: 36px; margin-top: 16px; padding-top: 14px; border-top: 1px solid #dddbda;">
                    <div>
                        <div style="font-size: 11px; color: #706e6b;">ENROLMENT DATE</div>
                        <div style="font-size: 13px; font-weight: 600; color: #080707;">August 1, 2023</div>
                    </div>
                    <div>
                        <div style="font-size: 11px; color: #706e6b;">SEMESTER</div>
                        <div style="font-size: 13px; font-weight: 600; color: #080707;">Semester 6</div>
                    </div>
                    <div>
                        <div style="font-size: 11px; color: #706e6b;">CURRENT GPA</div>
                        <div style="font-size: 15px; font-weight: 800; color: #0b8043;">8.85 / 10.00</div>
                    </div>
                    <div>
                        <div style="font-size: 11px; color: #706e6b;">STATUS</div>
                        <div style="margin-top: 2px;"><span class="badge badge-active">Active</span></div>
                    </div>
                    <div>
                        <div style="font-size: 11px; color: #706e6b;">RECORD OWNER</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0176d3;">Vinay Gole</div>
                    </div>
                </div>
            </div>

            <!-- Record Details Sections -->
            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 16px;">
                <div class="card" style="padding: 20px;">
                    <h2 style="font-size: 15px; font-weight: 700; color: #080707; border-bottom: 1px solid #dddbda; padding-bottom: 8px; margin: 0 0 16px 0;">Student Information</h2>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 13px;">
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">STUDENT NAME</div>
                            <div style="font-weight: 600; margin-top: 2px;">Aarav Sharma</div>
                        </div>
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">ROLL NUMBER</div>
                            <div style="font-weight: 600; font-family: monospace; margin-top: 2px;">CS-2023-014</div>
                        </div>
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">EMAIL</div>
                            <div style="color: #0176d3; font-weight: 600; margin-top: 2px;">aarav.sharma@example.edu</div>
                        </div>
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">ENROLMENT DATE</div>
                            <div style="font-weight: 600; margin-top: 2px;">2023-08-01</div>
                        </div>
                    </div>

                    <h2 style="font-size: 15px; font-weight: 700; color: #080707; border-bottom: 1px solid #dddbda; padding-bottom: 8px; margin: 24px 0 16px 0;">Academic Standing</h2>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 13px;">
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">COURSE / DEPARTMENT</div>
                            <div style="font-weight: 600; margin-top: 2px;">Computer Engineering</div>
                        </div>
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">CURRENT SEMESTER</div>
                            <div style="font-weight: 600; margin-top: 2px;">Semester 6</div>
                        </div>
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">CUMULATIVE GPA (10-SCALE)</div>
                            <div style="font-weight: 700; color: #0b8043; font-size: 15px; margin-top: 2px;">8.85</div>
                        </div>
                        <div>
                            <div style="color: #706e6b; font-size: 11px;">ACADEMIC STATUS</div>
                            <div style="margin-top: 4px;"><span class="badge badge-active">Active</span></div>
                        </div>
                    </div>
                </div>

                <!-- Right Activity Sidebar -->
                <div class="card" style="padding: 16px;">
                    <h2 style="font-size: 14px; font-weight: 700; color: #080707; border-bottom: 1px solid #dddbda; padding-bottom: 8px; margin: 0 0 12px 0;">Advising History & Tasks</h2>
                    <div style="font-size: 12px; color: #706e6b; display: flex; flex-direction: column; gap: 12px;">
                        <div style="background: #fafaf9; border: 1px solid #dddbda; padding: 10px; border-radius: 4px;">
                            <div style="font-weight: 700; color: #080707;">Mid-Term Review Completed</div>
                            <div style="margin-top: 2px;">Advisory session conducted by Prof. Vinay Gole. GPA standing verified.</div>
                            <div style="font-size: 10px; color: #706e6b; margin-top: 4px;">Oct 24, 2026 • Completed</div>
                        </div>
                        <div style="background: #fafaf9; border: 1px solid #dddbda; padding: 10px; border-radius: 4px;">
                            <div style="font-weight: 700; color: #080707;">Semester 6 Elective Approved</div>
                            <div style="margin-top: 2px;">Selected: Cloud Infrastructure & Distributed Systems.</div>
                            <div style="font-size: 10px; color: #706e6b; margin-top: 4px;">Aug 12, 2026 • Verified</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1280, "height": 840})
    page.set_content(html)
    page.wait_for_timeout(500)
    path = os.path.join(output_dir, "02_record_detail_view.png")
    page.screenshot(path=path)
    print("Generated:", path)

def generate_validation_screenshot(page):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Salesforce Validation Rule Error</title>
        {get_slds_base()}
    </head>
    <body>
        <div class="global-header">
            <div class="logo-area">
                <div class="app-launcher"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                <div class="cloud-logo">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0176d3"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>
                    Student Record Manager
                </div>
            </div>
            <div class="search-box">🔍 Search Student Records, Reports, Dashboards...</div>
            <div class="user-profile">
                <span style="font-size: 13px; color: #444;">Vinay Gole (Admin)</span>
                <div class="avatar">VG</div>
            </div>
        </div>
        <div class="nav-bar">
            <div class="nav-item active">Student Records ▼</div>
            <div class="nav-item">Reports</div>
            <div class="nav-item">Dashboards</div>
        </div>

        <div class="main-container">
            <!-- Edit Modal Overlay -->
            <div style="background: rgba(0,0,0,0.5); position: fixed; top: 0; left: 0; right: 0; bottom: 0; display: flex; align-items: center; justify-content: center; z-index: 1000;">
                <div style="background: white; border-radius: 6px; width: 720px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); overflow: hidden;">
                    <!-- Modal Header -->
                    <div style="padding: 16px 20px; border-bottom: 1px solid #dddbda; display: flex; justify-content: space-between; align-items: center;">
                        <h2 style="font-size: 18px; font-weight: 700; margin: 0; color: #080707;">Edit Student Record: Aarav Sharma</h2>
                        <span style="font-size: 20px; color: #706e6b; cursor: pointer;">✕</span>
                    </div>

                    <!-- Prominent Error Banner -->
                    <div style="background: #fef0ef; border-bottom: 2px solid #ea001e; padding: 12px 20px; display: flex; align-items: center; gap: 12px;">
                        <div style="background: #ea001e; color: white; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">!</div>
                        <div>
                            <div style="font-size: 13px; font-weight: 700; color: #ba0517;">Review the errors on this page.</div>
                            <div style="font-size: 12px; color: #ba0517;">These required fields must be corrected before saving: GPA (VR_GPA_Range).</div>
                        </div>
                    </div>

                    <!-- Form Body -->
                    <div style="padding: 20px; max-height: 400px; overflow-y: auto;">
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 13px;">
                            <div>
                                <label style="display: block; font-size: 12px; font-weight: 600; color: #514f4d; margin-bottom: 4px;">Student Name *</label>
                                <input type="text" value="Aarav Sharma" style="width: 90%; padding: 7px 10px; border: 1px solid #dddbda; border-radius: 4px;" readonly />
                            </div>
                            <div>
                                <label style="display: block; font-size: 12px; font-weight: 600; color: #514f4d; margin-bottom: 4px;">Roll Number *</label>
                                <input type="text" value="CS-2023-014" style="width: 90%; padding: 7px 10px; border: 1px solid #dddbda; border-radius: 4px;" readonly />
                            </div>
                            <div>
                                <label style="display: block; font-size: 12px; font-weight: 600; color: #514f4d; margin-bottom: 4px;">Course *</label>
                                <input type="text" value="Computer Engineering" style="width: 90%; padding: 7px 10px; border: 1px solid #dddbda; border-radius: 4px;" readonly />
                            </div>
                            <div>
                                <label style="display: block; font-size: 12px; font-weight: 600; color: #514f4d; margin-bottom: 4px;">Semester *</label>
                                <input type="number" value="6" style="width: 90%; padding: 7px 10px; border: 1px solid #dddbda; border-radius: 4px;" readonly />
                            </div>

                            <!-- Invalid Field with Error State -->
                            <div style="grid-column: span 2; background: #fff8f8; padding: 12px; border: 1px solid #ea001e; border-radius: 4px;">
                                <label style="display: block; font-size: 12px; font-weight: 700; color: #ea001e; margin-bottom: 4px;">GPA (Scale 0.00 – 10.00) *</label>
                                <input type="text" value="11.50" style="width: 200px; padding: 7px 10px; border: 2px solid #ea001e; border-radius: 4px; font-weight: bold; color: #ea001e;" />
                                <div style="color: #ea001e; font-size: 12px; font-weight: 600; margin-top: 6px; display: flex; align-items: center; gap: 4px;">
                                    ⚠️ Error: GPA must be between 0.00 and 10.00. (Rule: VR_GPA_Range)
                                </div>
                            </div>

                            <div>
                                <label style="display: block; font-size: 12px; font-weight: 600; color: #514f4d; margin-bottom: 4px;">Status *</label>
                                <input type="text" value="Active" style="width: 90%; padding: 7px 10px; border: 1px solid #dddbda; border-radius: 4px;" readonly />
                            </div>
                            <div>
                                <label style="display: block; font-size: 12px; font-weight: 600; color: #514f4d; margin-bottom: 4px;">Enrolment Date *</label>
                                <input type="text" value="2023-08-01" style="width: 90%; padding: 7px 10px; border: 1px solid #dddbda; border-radius: 4px;" readonly />
                            </div>
                        </div>
                    </div>

                    <!-- Modal Footer -->
                    <div style="padding: 14px 20px; background: #f3f3f3; border-top: 1px solid #dddbda; display: flex; justify-content: flex-end; gap: 10px;">
                        <button style="background: white; border: 1px solid #c9c7c5; padding: 7px 16px; border-radius: 4px; font-size: 13px; font-weight: 600;">Cancel</button>
                        <button style="background: #0176d3; color: white; border: none; padding: 7px 18px; border-radius: 4px; font-size: 13px; font-weight: 600;">Save</button>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    page.set_viewport_size({"width": 1280, "height": 840})
    page.set_content(html)
    page.wait_for_timeout(500)
    path = os.path.join(output_dir, "05_validation_rule_test.png")
    page.screenshot(path=path)
    print("Generated:", path)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        generate_report_screenshot(page)
        generate_dashboard_screenshot(page)
        generate_schema_screenshot(page)
        generate_record_detail_screenshot(page)
        generate_validation_screenshot(page)
        
        browser.close()
    print("All screenshots generated successfully.")

if __name__ == "__main__":
    main()
