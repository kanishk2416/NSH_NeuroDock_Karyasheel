# NSH_NeuroDock_Karyasheel
It is the repository of Solution for the problem statement of NSH, by Team Karyasheel. We Present you NeuroDock
# 🚀 Cargo Stowage Management System – National Space Hackathon 2025

Welcome to our submission for the **National Space Hackathon 2025**! This project addresses the challenge of efficiently organizing mission-critical cargo into spacecraft containers, optimizing for space, weight, priority, perishability, and zone preferences.

---

## 📦 Project Overview

Our system implements a cargo placement engine that:

- Matches cargo items with optimal containers based on volume, weight, and zones
- Handles high-priority and perishable items with special care
- Enables efficient search and retrieval
- Supports rearrangement and waste management workflows
- Simulates time passage for dynamic scenarios

---

## 📂 Repository Structure

```bash
.
├── input_items.csv              # Generated sample items
├── containers.csv               # Sample container definitions
├── generate_samples.py          # Item generator
├── generate_containers.py       # Container generator
├── sample_data.py               # Zone mappings for items
├── sample_checker.sh            # Bash script to validate submission
├── src/
│   ├── main.py                  # Entry point of the backend API
│   ├── placement.py             # Optimization algorithm
│   ├── api/                     # FastAPI endpoints
│   └── utils/                   # Helper functions
├── Dockerfile                   # For containerized deployment
├── requirements.txt             # Python dependencies
└── README.md                    # This file
🧠 Core Features
📌 Priority-Based Packing – High-priority items packed first with zone matching

🧪 Perishable & Medical Handling – Expiry and usage limit awareness

🛠️ Rearrangement & Optimization – Reevaluate placement dynamically

🗑️ Waste Management – Track unusable or expired items

🕓 Time Simulation API – Handles day-by-day mission progression

🔍 Item Retrieval APIs – Smart search and fetch mechanism

🚀 How to Run (Locally & Docker)
🔧 Local Setup
bash
Copy
Edit
# 1. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the API server
uvicorn src.main:app --host 0.0.0.0 --port 8000
🐳 Docker Setup
Make sure Docker is installed. Then run:

bash
Copy
Edit
docker build -t nsh2025-cargo-stowage .
docker run -p 8000:8000 nsh2025-cargo-stowage
The app will be accessible at http://localhost:8000

🔌 API Endpoints
Endpoint	Functionality
/api/placement	Get optimal placement recommendations
/api/search	Search for items
/api/retrieve	Retrieve specific item
/api/place	Manually place item
/api/waste/identify	List expired/damaged items
/api/waste/return-plan	Get disposal plan
/api/waste/complete-undocking	Finalize undocking
/api/simulate/day	Simulate a mission day
/api/import/items	Import items CSV
/api/import/containers	Import containers CSV
/api/export/arrangement	Export current stowage layout
/api/logs	View logs of all actions
📊 Dataset & Samples
Items: input_items.csv – Generated using generate_samples.py

Containers: containers.csv – Generated using generate_containers.py

Sample Zones: Defined in sample_data.py

🧪 Sample Checker
To validate your final arrangement, run:

bash sample_checker.sh
This checks for:

Overflow

Zone mismatches

Weight/volume breaches

📑 Submission Requirements
As per Submission Guidelines:

✅ [x] Working Source Code (Python, FastAPI)

✅ [x] Dockerfile using ubuntu:22.04, exposing port 8000

✅ [x] This README

📄 Technical Report: [Insert Google Drive Link]

🎥 Demo Video: [Insert Google Drive Link]

🧠 Tech Stack
Python 3.10

FastAPI – REST API backend

Pandas & NumPy – Data processing

Docker – Containerization

Uvicorn – ASGI server

🏁 Authors
Team Name: [Karyasheel]

Members:

[Siddharth Kumar]

[Aarav Majumdar]

[Ronit Jaiswal]

[Kanishk Nagar]


🏆 Let’s Launch!
This project aims to contribute toward safer and more efficient space missions by automating and optimizing cargo logistics. We hope this helps astronauts spend more time exploring — and less time packing.

“It’s not rocket science... wait, yes it is.” 🚀
