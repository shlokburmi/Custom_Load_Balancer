## 🏗️ Custom_Load_Balancer
A high-level, customizable load balancer built with Python and Docker for scalable, reliable traffic management.
Supports security features, Dockerized deployment, and seamless scaling.

## 🚀 Features

🔄 Round Robin Load Balancing

🛡️ Security Enhancements: Rate limiting, IP blocking, JWT Authentication

🔒 Containerized: Easy deployment via Docker Compose

📈 Logging & Monitoring

## 📂 Project Structure
Dockerfile.lb, dockerfile: Docker build files

docker-compose.yml: Multi-container configuration

app.py: Example backend service/app

loadbalancer.py: Main load balancer logic

.gitattributes, README.md: Project meta

## 🐳 Getting Started
bash


Clone the repo
git clone https://github.com/shlokburmi/Custom_Load_Balancer.git

cd Custom_Load_Balancer

Build and run with Docker Compose
docker-compose up --build

Access services at http://127.0.0.1:8080

## 🔐 Security
✋ Rate limiting: Prevent abuse by restricting client request rate.

🚫 IP blocking: Block suspicious/abusive IPs after threshold triggers.

🗝️ JWT Authentication: Protects endpoints from unauthorized access.

## 📄 Usage
Modify or extend the load balancer and app logic as needed:

Add more Flask or Python backend services.

Customize loadbalancer.py for advanced routing or security logic.

## 📦 Requirements
Docker & Docker Compose

Python 3.x for local running

## 🤝 Contributing
Pull requests welcome! For major changes, please open an issue first.

## 📷 Snapshots




<img width="1847" height="1001" alt="image" src="https://github.com/user-attachments/assets/6d54d302-a706-471a-85f0-bdd5fdf71cea" />




<img width="1566" height="886" alt="image" src="https://github.com/user-attachments/assets/d2fc8fa0-8cd3-45ac-b5c2-834d27055838" />




