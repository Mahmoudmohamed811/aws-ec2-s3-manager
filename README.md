# Cloud Resource Manager

A Python-based project to manage AWS cloud resources such as EC2 instances and S3 buckets. This tool allows users to create, list, and terminate EC2 instances, as well as create, list, and delete S3 buckets. It also includes functionality for monitoring EC2 instance metrics.

## Features

### EC2 Management:
- Create EC2 instances with configurable options (AMI ID, instance type, security groups, tags, etc.).
- List all EC2 instances with details (ID, name, and state).
- Terminate EC2 instances.

### S3 Management:
- Create S3 buckets.
- List all available S3 buckets.
- Delete S3 buckets.

### EC2 Monitoring:
- Fetch and display CloudWatch metrics for specific EC2 instances.

## Prerequisites

### AWS Credentials:
Ensure you have an AWS account and configure your credentials using the AWS CLI:

```bash
aws configure
```

### Python:
Make sure Python 3.x is installed on your system. You can check this by running:

```bash
python --version
```

### Dependencies:
Install the required Python packages using:

```bash
pip install boto3
```

## Getting Started

### Clone the Repository

```bash
git clone git@github.com:username/repository_name.git
cd repository_name
```

### Run the Program
Execute the main script to start the Cloud Resource Manager:

```bash
python cloud_resource_manager.py
```

## Usage

### Menu Options

#### Create EC2 Instance
Enter the necessary details (AMI ID, instance type, security group IDs, etc.) to launch an EC2 instance.

#### List EC2 Instances
Displays a list of all EC2 instances in your AWS account, including their IDs, names, and states.

#### Terminate EC2 Instance
Enter the instance ID to terminate a specific EC2 instance.

### Manage S3 Buckets

#### Create an S3 bucket
Provide its name.

#### List all S3 buckets
List all S3 buckets in your AWS account.

#### Delete an S3 bucket
Provide its name.

### Monitor EC2 Instances
View CloudWatch metrics for a specific EC2 instance by entering its ID.

### Exit
Quit the program.

## Project Structure

```plaintext
├── ec2_manager.py         # Manages EC2 instances (create, list, terminate).
├── s3_manager.py          # Manages S3 buckets (create, list, delete).
├── monitor.py             # Monitors EC2 metrics via CloudWatch.
├── cloud_resource_manager.py # Main script for the project.
├── requirements.txt       # List of dependencies (e.g., boto3).
├── README.md              # Project documentation.
```

## Contributing
Contributions are welcome! If you'd like to improve this project, please:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add your message"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## Acknowledgements
- AWS Boto3 Documentation
- CloudWatch Metrics
