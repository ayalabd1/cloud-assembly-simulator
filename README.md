# cloud-assembly-simulator

A high-performance **Async Assembly Code Simulator & Execution Engine** built with **FastAPI**, **Python**, and **MongoDB Atlas**. 

This cloud-native system allows users to execute custom MIPS Assembly code instructions (`ADD`, `ADDI`, `SUB`, `LW`, `SW`, `BEQ`), calculate register states and memory layouts in real time, and persist simulation history to the cloud.

---

## System Architecture

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous Web Framework)
* **Database:** [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (Cloud NoSQL Database)
* **Database Driver:** [Motor](https://motor.readthedocs.io/) (Async Python driver for MongoDB)
* **Execution Engine:** Custom MIPS Instruction Set Simulator (`app/simulator.py`)
* **Environment Management:** `python-dotenv` for secure secret handling

---

## Features

- **Asynchronous Execution:** Handles multiple simulation requests concurrently without blocking the main event loop.
- **RESTful Endpoints:**
  - `POST /upload-assembly`: Uploads `.asm` files, parses instructions, executes simulation, and saves state to MongoDB Atlas.
  - `GET /history`: Retrieves the 10 most recent simulation runs sorted chronologically.
- **Security First:** Connection strings and credentials are safely managed via environment variables (`.env`).

---

## Project Structure

```text
cloud-assembly-simulator/
├── app/
│   ├── database.py      # MongoDB Atlas connection & Motor client initialization
│   ├── main.py          # FastAPI application & REST API routes (POST/GET)
│   └── simulator.py     # Custom Virtual CPU Engine (MIPS Registers & Memory)
├── .env.example         # Template for environment variables
├── .gitignore            # Git exclusion rules (securing .env and venv)
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

Getting Started
1. Prerequisites
Python 3.10+

Active MongoDB Atlas Cluster

2. Installation & Setup
Clone the repository:

git clone [https://github.com/ayalabd1/cloud-assembly-simulator.git](https://github.com/ayalabd1/cloud-assembly-simulator.git)
cd cloud-assembly-simulator

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Configure Environment Variables:

Create a .env file in the root directory based on .env.example:

MONGO_URL=mongodb+srv://<username>:<password>@cluster0.xxx.mongodb.net/?retryWrites=true&w=majority
3. Running the Server
Start the FastAPI application using Uvicorn:

uvicorn app.main:app --reload
Interactive API documentation (Swagger UI) will be available at:
http://127.0.0.1:8000/docs


### GitHub:
git add README.md
git commit -m "Update README with full architecture and Getting Started instructions"
git push origin main