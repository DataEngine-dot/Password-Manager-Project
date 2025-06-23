# PASSWORD MANAGER Project
A command-line based password manager that securely stores and managers user credentials using AWS Secret Manager. Using Python and Boto3, this code provides options to create, retrieve, delete and list secrets.

## Features
 - stores credentials (username and password) securely in AWS Secret Manager
 * retrieve and saves the secrets to a local JSON file
 + deletes stored secrets
 - list all secrets in AWS secrets Manager
 - includes error handling and tests
 - CI/CD integration via GitHub Actions

## Technologies Used:
 - Python 
 - Boto3
 - Pytest
 - GitHub Actions (CI/CD)

## Requirememts:

    - Python3+
    - Boto3
    - Pytest
    - flak8
    - AWS account

## Setup:

1. **Create and activate a virtual environment:**

   - On **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Install the dependencies:**

   After activating the virtual environment, install the required packages by running:
   ```bash
   pip install -r requirements.txt
    ```

3. **Configure AWS CLI credentials** (make sure you have AWS CLI installed):

    ```bash
    aws configure
    ```

    You will be asked to enter your:
     - AWS Access Key ID
     - AWS Secret Access Key 
     - Default region
     - Output format (keep this as `json`)

# Running Tests:
```bash
export PYTHONPATH=$(pwd)
pytest -v
```

# Usage:
Run the script:
```bash
python main.py
```
Then follow the CLI prompts to store or retrieve secrets.

# Example:
```bash
Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
> l
0 available
Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
> e
Secret Identifier: Secret1
UserId: testEmail
Password: testPassword
> Secret saved.
Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
> l
1 available
- Secret1
Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:
> x
Thank you. Goodbye.
```