# CI/CD Pipeline for Books Service

## Project Overview
This project implements a CI/CD pipeline using GitHub Actions for a books service interfacing with a MongoDB database. The pipeline automates building, testing, and querying stages for the books service, which does not utilize the loans service or NGINX as per the previous assignment.

## Features
- **Automated CI/CD Pipeline:** Utilizes GitHub Actions to automate the integration and delivery processes.
- **Docker Integration:** Leverages Docker and Docker Compose for environment management and service orchestration.
- **Testing with Pytest:** Includes automated tests to ensure service reliability and performance.

## Technologies Used
- GitHub Actions
- Docker & Docker Compose
- Pytest for testing
- MongoDB for database management

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- GitHub account

### Installation and Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yuvalmaliniak/Cloud-Computing-proj3.git
   cd Cloud-Computing-proj3
2. **Build and Run with Docker Compose**
     ```bash
      docker-compose up --build

### Usage
The pipeline is triggered by a push event to the repository.
The workflow defined in .github/workflows/assignment3.yml consists of three jobs: build, test, and query.

### CI/CD Pipeline Details
**Build Job:** Builds the Docker image for the books service.
**Test Job:** Runs the books service and MongoDB containers, and executes Pytest tests.
**Query Job:** Issues requests to the books service and records the results.

### Testing
Tests are located in the tests directory and can be run using:\
  pytest -v tests/assn3_tests.py


### Outputs
Logs: Available in log.txt at workflow termination.\
Test Results: Available in assn3_test_results.txt.\
Query Outputs: Recorded in response.txt.

### Authors
Yuval Maliniak \
Rotem Mizrachi

