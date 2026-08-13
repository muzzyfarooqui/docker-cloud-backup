# Cloud Object Storage Client

## Overview

Cloud Object Storage Client is a Python command-line application that allows users to upload, list, download, and delete files stored in Amazon S3.

The project was originally developed using Docker and MinIO to understand object storage fundamentals in a local environment before being migrated to AWS S3. The migration demonstrates how a well-designed application can transition from a self-managed object storage server to a managed cloud service with minimal changes to the application logic.

The project demonstrates cloud engineering fundamentals including object storage, client-server architecture, AWS IAM authentication, SDK integration, and Python application development.

---

## Features

- ✅ Upload files to Amazon S3
- ✅ List objects stored in an S3 bucket
- ✅ Download objects from Amazon S3
- ✅ Delete objects from Amazon S3
- ✅ Interactive command-line interface (CLI)
- ✅ AWS IAM authentication
- ✅ Graceful error handling

---

## Technologies Used

- Python
- Amazon S3
- AWS IAM
- boto3
- Git
- GitHub
- Visual Studio Code

---

## Skills Demonstrated

- Python application development
- Amazon S3 object storage
- AWS IAM authentication
- Client-server architecture
- SDK integration using boto3
- Command-line interface (CLI) development
- Error handling
- Git version control
- Cloud application migration

---

## Architecture

The diagram below illustrates how the Python application communicates with Amazon S3. The application uses the AWS SDK (`boto3`) to send authenticated HTTPS requests to the Amazon S3 service, which stores uploaded objects in the configured S3 bucket.

![Architecture Diagram](images/architecture.png)

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/muzzyfarooqui/docker-cloud-backup.git
cd docker-cloud-backup
```

### 2. Create and activate a virtual environment

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS credentials

```bash
aws configure
```

Provide:

- AWS Access Key ID
- AWS Secret Access Key
- Default Region (`us-east-1`)
- Output Format (`json`)

### 5. Run the application

```bash
python3 app.py
```

---

## What I Learned

The biggest lesson from this project was learning by building instead of memorizing commands.

Building the application locally with Docker and MinIO helped me understand how object storage works behind the scenes. Migrating the application to AWS S3 showed me that a well-designed architecture allows the storage backend to change while the application itself remains largely the same.

This project strengthened my understanding of:

- Amazon S3
- AWS IAM
- boto3
- Object storage
- Buckets and objects
- Client-server architecture
- SDK integration
- HTTP communication
- Authentication
- Error handling
- Python application design
- Git version control

---

## Future Improvements

- Provision AWS infrastructure using Terraform
- Implement least-privilege IAM policies
- Add CloudWatch monitoring and logging
- Build a web interface
- Add automated testing
- Implement CI/CD using GitHub Actions