# ELT Data Pipeline using Microservices Architecture

This project implements a microservices-based **ELT (Extract, Load, Transform)** data pipeline using **FastAPI**. The architecture separates concerns into different microservices for data ingestion, loading, and transformation, and provides an API gateway for external consumers to interact with the services. 

### Table of Contents
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)


### Project Structure
```bash
dalberg-ingestflow/
├── api_gateway/                    # The API gateway for the microservices(Entry point)
│   ├── __init__.py
│   └── routes.py                   # API routes for interacting with services
├── services/
│   ├── data_ingestion/             # Microservice for data ingestion
│   │   ├── __init__.py
│   │   └── ingestion_service.py    # Contains the data extraction logic
│   ├── data_loading/               # Microservice for data loading (ELT step)
│   │   ├── __init__.py
│   │   └── load_service.py         # Loads data into a database
│   ├── data_transformation/        # Microservice for data transformation (after loading)
│   │   ├── __init__.py
│   │   └── transform_service.py    # Transforms the data
├── utils/
│   ├── logger.py                   # Centralized logging service
│   ├── config.py                   # Handles environment variables
├── main.py                         # Entry point for the application
├── requirements.txt
└── README.md


### Solution Architecture
                       +----------------------+
                       |  External Consumers   |
                       +----------------------+
                                |
                                |
                      +-------------------------+
                      |        API Gateway       |
                      +-------------------------+
                         /      |     |      \
                        /       |     |       \
                       /        |     |        \
       +----------------+ +-------------+ +-------------+
       | Ingestion       | | Loading     | | Transformation|
       | Microservice    | | Microservice| | Microservice  |
       +----------------+ +-------------+ +-------------+
             |                     |                |
     +----------------+     +-----------------+     |
     | External Source |     | PostgreSQL (Raw)|     |
     +----------------+     +-----------------+     |
                                    |            +-------------+
                                    |            | Transformed |
                                    |            |  Data (DB)  |
                                    |            +-------------+
                                    |                   
                            +------------------+        
                            |  Raw data Source |        
                            +------------------+        



## Requirements

Make sure you have the following installed:
- Python 3.9+
- PostgreSQL 12+
- **pip** for Python package management
- **virtualenv** (optional but recommended for isolating Python environments)


## Setup and Installation

### 1. Clone the repository
git clone https://github.com/alpho07/dalberg-ingestflow.git
cd dalberg-ingestflow


python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt



### **2. requirements.txt**

This file lists the dependencies your project needs to install via pip.


fastapi==0.70.0
uvicorn==0.15.0
pandas==1.3.3
sqlalchemy==1.4.22
asyncpg==0.23.0
requests==2.26.0
python-dotenv==0.19.0

### **3. Setup .env variables**
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database>
API_URL=https://api.example.com/api/v1           # External API endpoint for ingestion
API_KEY=your-api-key   

### **4. Run the application**

python main.py

The API Gateway will be accessible at http://127.0.0.1:8001/.

### **5. API Endpoint Documentation **

FastAPI API documentation can be accessed at:

    Swagger UI: http://127.0.0.1:8001/docs
    ReDoc: http://127.0.0.1:8001/redoc

