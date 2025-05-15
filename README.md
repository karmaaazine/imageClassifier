# Image Classifier API with FastAPI + MobileNet

This project is an image classification API built using **FastAPI** and **TensorFlow's MobileNet** model. It allows users to upload an image and receive a predicted class label. The application is containerized using Docker, deployed on **Kubernetes (Minikube)**, and tested for performance with **Locust**.

---

## 📁 Project Structure
---

├── app/
│ ├── main.py 
│ ├── model.py 
│ ├── utils.py 
│ ├── web/
│ └──index.html
├── Dockerfile
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
├── locustfile.py 
├── requirements.txt
└── README.md

---

## ⚙️ Requirements

- Python 3.8+
- Docker
- Minikube (Kubernetes locally)
- Locust (`pip install locust`)

---

## Setup & Run Locally (Without Docker)

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/imageClassifier.git
cd imageClassifier
```


2. **Create virtual environment and install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # or .venv\Scripts\activate on Windows PowerSHell
pip install -r requirements.txt
```

3. **Run the app**
```bash
uvicorn main:app --reload
```
**Congrats! you just ran your FastAPI app.**

---

## Deploy on Minikube

1. **Start Minikube**
```bash
minikube start
```

2. **Build Docker image inside Minikube**
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned #run inside Powershell
.\venv\Scripts\Activate.ps1 #enter your env
minikube -p minikube docker-env | Invoke-Expression
docker build -t mobilenet-api:latest .
```
3. **Expose the service**
```bash
minikube service mobilenet-service
```

4. **Visualize Minikube**
```bash
minikube dashboard
```
<img width="960" alt="image" src="https://github.com/user-attachments/assets/a6ace3ae-331f-414d-845e-904ea5aa10c9" />


Fantastic! this will open your app with Monikube IP.
---

## App UI:
<img width="960" alt="image" src="https://github.com/user-attachments/assets/3cf1e06a-7288-4fbd-bed7-744a00420efc" />


---

## Load Testing with Locust

1. **Prepare a sample image**
Add a file like test.jpg in the root folder for testing.

2. **Run Locust**
after creating a locustfile.py, you can run it with:

```bash
locust
```

4. **Open the UI**
<img width="960" alt="image" src="https://github.com/user-attachments/assets/28b8d452-837e-4dbf-b005-41d563b12cc1" />


---

Go to: http://localhost:8089, give as example:

-Users: 10
-Spawn rate: 2


---

## License
This project is licensed under the MIT License.

## Author
Salma Zine
salmazine2021@gmail.com






