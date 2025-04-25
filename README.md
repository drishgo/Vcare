# VCare

VCare is a simple digital-wellbeing tracker that logs your application usage over time. It consists of a backend tracker & API, and an optional frontend client.

---

## Table of Contents

- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
  - [1. Start the Tracker](#1-start-the-tracker)  
  - [2. Start the API Server](#2-start-the-api-server)  
  - [3. (Optional) Start the Frontend Client](#3-optional-start-the-frontend-client)  
- [Data Output](#data-output)  
- [Contributing](#contributing)  
- [License](#license)

---

## Prerequisites

- Python 3.7 or higher  
- `pip` (Python package manager)  
- (Optional) A modern browser to view the frontend client  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/VCare.git
   cd VCare
Install backend dependencies

bash

cd backend
pip install {deps}          (you need to install flask for using over web ,         additionallly install plyer for notifs)
                            
cd ..
(Optional) Install frontend dependencies

bash

cd frontend
npm install       # or yarn install
cd ..
Configuration
API Server Port
By default the Flask API listens on port 5000. To change it, open backend/api.py and modify the line:

python

app.run( port=5000)
Replace 5000 with your preferred port number.

Data Storage
The tracker writes usage logs to backend/usage_data.json. No database setup is required.

Usage
1. Start the Tracker
Run the tracker in the background so it can continuously log your app usage:

bash

cd backend
python tracker.py &
Note: On Windows, you can open a new PowerShell window and run:

powershell

python tracker.py
2. Start the API Server
In a separate terminal, start the Flask API:

bash

cd backend
python api.py
The API exposes endpoints for:

Retrieving raw usage data

Aggregated reports (e.g. daily totals, per-app breakdown)

By default, visit http://localhost:5000/ (or your chosen port).

3. (Optional) Start the Frontend Client
The frontend provides a visual dashboard for your usage data.

bash

cd frontend
npm start          # or yarn start
Then open your browser to http://localhost:3000/ (or the port shown in the console). The frontend will communicate with the backend API to fetch and display your stats.

Data Output
All tracked events are appended to backend/usage_data.json in this format:

You can parse this JSON directly or use the API endpoints to get pre-aggregated summaries.

Contributing
Fork the repo

Create a feature branch (git checkout -b feature/my-feature)

Commit your changes (git commit -m "Add my feature")

Push to your branch (git push origin feature/my-feature)

Open a Pull Request

Please follow the existing code style and add tests for new functionality.

