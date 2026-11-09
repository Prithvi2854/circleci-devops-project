# Continuous Integration and Testing Pipeline Using CircleCI

## 📌 Project Overview

This project demonstrates the implementation of a **Continuous Integration and Continuous Delivery (CI/CD) pipeline using CircleCI** for a Python-based Streamlit web application.

A calculator application is used as the sample application to demonstrate how DevOps practices can automate software testing, code-quality validation, and deployment workflows.

Whenever new code is pushed to GitHub, CircleCI automatically retrieves the latest code, installs the required dependencies, executes automated tests, and performs code-quality checks.

---

## 🎯 Objectives

- Implement a CI/CD pipeline using CircleCI.
- Automate dependency installation.
- Perform automated unit testing using PyTest.
- Perform static code-quality checking using Flake8.
- Integrate GitHub with CircleCI.
- Develop a simple interactive web interface using Streamlit.
- Demonstrate automatic pipeline execution whenever code changes are pushed.

---

## 🏗️ System Architecture

```text
                  Developer
                      │
                      │ git push
                      ▼
                 ┌──────────┐
                 │  GitHub  │
                 └────┬─────┘
                      │
                      ▼
                 ┌──────────┐
                 │ CircleCI │
                 └────┬─────┘
                      │
             ┌────────┴─────────┐
             │                  │
             ▼                  ▼
     Install Dependencies   Code Checkout
             │
             ▼
       Automated Testing
           (PyTest)
             │
             ▼
      Code Quality Check
          (Flake8)
             │
             ▼
          Build/Deploy
             │
             ▼
       Streamlit Web App
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web-based user interface |
| PyTest | Automated unit testing |
| Flake8 | Code-quality checking |
| Git | Version control |
| GitHub | Source-code repository |
| CircleCI | CI/CD automation |

---

## 📂 Project Structure

```text
circleci-devops-project/
│
├── .circleci/
│   └── config.yml
│
├── app/
│   ├── __init__.py
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧮 Application Features

The Streamlit application provides an interactive calculator interface with:

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero error handling
- Interactive input fields
- Operation selection
- Result display

The calculator logic is separated from the user interface so that the core functionality can be independently tested using automated tests.

---

## 🧪 Automated Testing

PyTest is used to verify the calculator functionality.

The test suite checks:

- Addition functionality
- Subtraction functionality
- Multiplication functionality
- Division functionality
- Division-by-zero handling

Tests can be executed locally using:

```bash
python -m pytest
```

---

## 🔍 Code Quality Checking

Flake8 is used to identify Python coding issues such as:

- Trailing whitespace
- Syntax-related issues
- Improper formatting
- Unused imports
- Other PEP 8 violations

Run the code-quality check using:

```bash
python -m flake8 app tests
```

---

## 🔄 CI/CD Pipeline

The CircleCI pipeline is triggered whenever changes are pushed to the GitHub repository.

The pipeline performs the following stages:

### 1. Checkout Code

CircleCI retrieves the latest source code from GitHub.

### 2. Install Dependencies

The required Python packages are installed using:

```bash
pip install -r requirements.txt
```

### 3. Automated Testing

PyTest executes the application's unit tests:

```bash
python -m pytest
```

### 4. Code Quality Check

Flake8 checks the application and test code:

```bash
python -m flake8 app tests
```

### 5. Build / Deployment

After successful validation, the application can proceed to the deployment stage.

---

## ▶️ Running the Application Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/Prithvi2854/circleci-devops-project.git
cd circleci-devops-project
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit application

```bash
python -m streamlit run streamlit_app.py
```

The application will open in the browser.

---

## 🔁 Development Workflow

The project follows a simple DevOps workflow:

```text
Develop
   ↓
Test Locally
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub
   ↓
CircleCI Pipeline
   ↓
Automated Tests
   ↓
Code Quality Check
   ↓
Build / Deployment
```

If a test or quality check fails, the CircleCI pipeline stops and reports the failure. The developer can then correct the code and push the changes again.

---

## 📊 Expected CI Result

A successful CircleCI pipeline should contain successful stages such as:

```text
✓ Checkout code
✓ Install dependencies
✓ Run automated tests
✓ Code quality check
✓ Build / Deploy
```

A failure in any required stage causes the pipeline to fail, preventing invalid code from progressing further.

---

## 🚀 Future Enhancements

The project can be extended with:

- Deployment to Streamlit Community Cloud or another hosting platform.
- Docker containerization.
- Automated deployment after successful tests.
- Test-result reports and artifacts.
- Code coverage using `pytest-cov`.
- Security scanning.
- Separate development and production workflows.
- Notifications for pipeline failures.

---

## 🎓 Conclusion

This project demonstrates how **CI/CD practices can be applied to a Python web application using CircleCI**.

The application is automatically validated through unit testing and code-quality checks whenever changes are pushed to GitHub. This reduces manual testing effort, detects errors early, and provides a foundation for automated deployment.

The project demonstrates the core DevOps principle of:

> **Build → Test → Validate → Deploy → Repeat**