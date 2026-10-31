# Python CI Pipeline using GitHub Actions

## 1. Project Overview

This project demonstrates the implementation of an automated Continuous Integration (CI) pipeline using GitHub Actions for a Python application.

The pipeline automatically runs whenever code is pushed to the `main` branch or when a Pull Request targets the `main` branch.

The main objective is to automate testing, detect code errors early, and improve code integration reliability.

## 2. Technologies Used

* Git and GitHub
* GitHub Actions
* Python 3.12
* Pytest
* YAML
* Ubuntu GitHub-hosted Runner

## 3. Project Structure

```text
github-actions-first-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app.py
├── test_app.py
├── requirements.txt
└── README.md
```

## 4. CI Pipeline Workflow

The pipeline consists of the following steps:

1. **Checkout Repository:** Retrieves the project source code.
2. **Setup Python:** Configures Python 3.12.
3. **Install Dependencies:** Installs the required Python packages.
4. **Set Environment Variable:** Configures the application environment.
5. **Run Tests:** Executes automated tests using Pytest.
6. **Success Message:** Displays a confirmation message after successful execution.

## 5. Pipeline Triggers

The workflow is triggered by:

* Push events targeting the `main` branch.
* Pull Requests targeting the `main` branch.

## 6. Automated Testing

Pytest is used to validate the application functionality.

The project includes tests for:

* Greeting functionality.
* Addition operations.
* Negative number calculations.
* Multiplication operations.

### Run Tests Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Execute tests:

```bash
python -m pytest -v
```

## 7. Failure Testing

The pipeline was tested with an intentionally incorrect assertion to simulate a test failure.

The expected behavior was:

* The test step fails.
* The workflow reports a failed run.
* Subsequent normal steps are skipped.
* After fixing the test, the pipeline runs successfully again.

## 8. Pull Request Automation

A feature branch named `feature/update-app` was created to introduce a new multiplication function.

A Pull Request was opened against the `main` branch.

GitHub Actions automatically executed the CI workflow, and all checks passed successfully.

## 9. Key Learning Outcomes

Through this project, I gained practical experience in:

* Building automated CI pipelines.
* Configuring GitHub Actions workflows.
* Understanding Events, Jobs, Steps, and Runners.
* Working with YAML workflow files.
* Managing Python dependencies.
* Automating unit tests.
* Using environment variables.
* Troubleshooting pipeline failures.
* Working with Git branches and Pull Requests.

## 10. Author

**Abubaker Abdallh**

B.Tech Information Technology | Cloud & DevOps Enthusiast

GitHub: Abubaker-cloud
