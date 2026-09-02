# 🚀 Cloud-Based MIPS Assembly Simulator

A high-performance, cloud-native virtual MIPS CPU assembly simulator built with FastAPI, MongoDB, and AWS S3. Fully containerized with Docker and featuring automated CI/CD pipelines.

---

## 🛠 Architecture & Technologies

- **Backend:** Python 3.11, FastAPI, Uvicorn
- **Core Logic:** Custom Virtual MIPS CPU Engine (R, I, J instruction execution)
- **Database:** MongoDB Atlas (via motor async driver) for execution history
- **Storage:** AWS S3 (via boto3) for assembly source code and artifact persistence
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions (Automated pytest suite) + Render Deployment

---

## 🏗 System Architecture Flow

[ Client / Postman ] ──> [ FastAPI Server ]
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
     [ CPU Simulator ]  [ AWS S3 Bucket ]  [ MongoDB Atlas ]

---

## 🚀 Live Demo

- **Live API Endpoint:** [https://cloud-assembly-simulator-1.onrender.com](https://cloud-assembly-simulator-1.onrender.com)
- **Interactive Swagger Docs:** [https://cloud-assembly-simulator-1.onrender.com/docs](https://cloud-assembly-simulator-1.onrender.com/docs)

---

## ⚙️ Local Setup Instructions

1. Clone the repository:
   git clone [https://github.com/ayalabd1/cloud-assembly-simulator.git](https://github.com/ayalabd1/cloud-assembly-simulator.git)
   cd cloud-assembly-simulator

2. Configure Environment Variables:
   Create a .env file based on .env.example:
   MONGO_URL=your_mongodb_connection_string
   AWS_ACCESS_KEY_ID=your_aws_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret
   AWS_BUCKET_NAME=your_s3_bucket

3. Run with Docker Compose:
   docker-compose up --build

4. Run Unit Tests:
   pytest