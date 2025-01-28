# Automated Student Registration Testing Overview

The **Automated Student Registration Testing** works is a web application designed for educational institutions to manage student registration efficiently. The primary goal of this project is to automate and test the user-friendlt interface as well as to join practice in quality assurance and ensure form validation, data accuracy, error handling, and form submissions.

This project focus is on ensuring high quality Data Integrity, Automation, documentation, and bug tracking.

- **Data Integrity**: Ensuring accurate data by creating and documenting constraints and validation checks.
- **Automation**: Implementing automated testing for functionality and performance testing.
- **Reporting and Bug Tracking**: Documentations are written for every input that is tested as well as big tickets are created for every test that has a different outcome than expected.
- **Data Validation**: Each form is validated through the HTML pages and the flask server.

## Table of Contents
1. [Website Creation](website-creation)
2. [Reporting](#reporting)
3. [Stack](#stack)
4. [Project Workflow](#project-workflow)
5. [How to Run](#how-to-run)


## Website Creation

### Homepage
- **Purpose:** A welcoming page with basic information, navigation, and links.
- **Functionality:**
  - Responsive design.
  - UI consistency across different screen sizes.

### Student Registration Form
- **Purpose:** A form for entering student details (name, age, grade, parent/guardian name, etc.).
- **Functionality:**
  - Input field validation (e.g., required fields, valid formats for email and phone).
  - Error handling for incorrect or missing inputs.
  - Successful form submission and redirection to the confirmation page.

### Confirmation Page
- **Purpose:** Displays a confirmation message after successful form submission.
- **Functionality:**
  - Shows the submitted form data for verification.
  - Option to return to the homepage.

### Error Handling Page
- **Purpose:** Informs the user about incomplete or invalid registration attempts.
- **Functionality:**
  - Displays appropriate error messages (e.g., missing fields or invalid formats).
  - Allows the user to return to the form to correct inputs.


### Reporting:
- Generate detailed reports for each test run, tracking:
  - Test results (pass/fail).
  - Defect logs for failed tests.
- Genate bug tracking reports for each test with unexpected results:
  - Tracks the outcome of the test and what was tested.
  - Logs tests in bug tracking csv.


# Stack
### Frontend:
- **HTML** and **CSS** for page structure and styling.
- Basic **JavaScript** for optional form enhancements.

### Backend:
- **Flask** for server-side processing of form submissions.

### Automation:
- **Python** with **Selenium WebDriver** for automated testing.

### Version Control:
- **GitHub** for versioning and collaboration.


## Project Workflow
1. **Build the Registration System**:
   - Create HTML forms for student input.
   - Implement backend logic to handle form submissions and validation using Flask.
   - Develop a confirmation page to display submitted data.
   - Integrate error handling for invalid submissions.

2. **Automate Testing with Selenium**:
   - Write scripts for form validation, submission, and redirection testing.
   - Test cross-browser compatibility.

3. **Test Management and Reporting**:
   - Organize and structure test cases for easy tracking.
   - Automate bug tracking and generate detailed reports for each test cycle.


## How to Run
### Prerequisites:
- Python installed on your system.
- Selenium WebDriver installed.
- Flask installed (via `pip install flask`).


### Steps:
1. Clone the repository:
2. Navigate to the project directory:
3. Run the Flask server:
   ```
   python "Automated Test Scripting\Student Registration\app.py"
   ```
4. Run automated tests:
   ```
   python "Automated Test Scripting\Student Registration\tests\test_registration_documentation"
   ```
