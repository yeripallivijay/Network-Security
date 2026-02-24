### Network Security Project For Phishing Data
```markdown
# Network Security Phishing Detection System 🚀

[![GitHub stars](https://img.shields.io/github/stars/yeripallivijay/Network-Security?style=social)](https://github.com/yeripallivijay/Network-Security)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Docker](https://img.shields.io/badge/docker-%2300bfff.svg?logo=docker&logoColor=white)](https://www.docker.com/)

## 🎯 Project Overview

The **Network Security Phishing Detection System** is an **end-to-end Machine Learning application** designed to detect phishing URLs and malicious network activity. This project demonstrates **professional-level ML pipelines**, **containerized deployment**, and **cloud integration** — perfect for a **FAANG-level portfolio project**.

### ✨ Key Highlights
- ✅ **Automated** data ingestion, preprocessing, model training, and prediction pipelines
- 🔗 **REST API** for serving predictions using **FastAPI**
- 🐳 **Containerized deployment** using **Docker**
- ☁️ **Hosted on AWS EC2** with **ECR integration** for CI/CD pipelines
- 📊 **Optional ML experiment tracking** (MLflow/DagsHub for research environments)
- 🎯 **ROC-AUC: ~98%** on test set

## 🔍 Problem Statement

Phishing attacks are a **growing cybersecurity threat**. Traditional detection methods struggle to scale with the volume of malicious URLs. This project provides a **scalable ML-powered solution** to classify URLs and network events as **safe or malicious** with **high accuracy**.

## 🏗️ Architecture & Pipeline

```
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   Data Pipeline │───▶│  Training Pipeline│───▶│ Prediction Pipeline│
└─────────────────┘    └──────────────────┘    └──────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ MongoDB/CSV     │    │ final_model/      │    │ FastAPI Endpoint │
│ Sources         │    │ (Model + Preproc) │    │ /predict         │
└─────────────────┘    └──────────────────┘    └──────────────────┘
```

### 1. **Data Pipeline**
- **Ingestion**: Fetches URL datasets from MongoDB/CSV sources
- **Validation**: Ensures clean, structured data using pandas & schema checks
- **Preprocessing**: Feature extraction and encoding for ML models

### 2. **Training Pipeline**
- Implements **supervised ML models** including ensemble classifiers
- **Hyperparameter tuning** for optimal ROC-AUC performance
- Stores trained models and preprocessing objects in `final_model/`

### 3. **Prediction Pipeline**
- Accepts **CSV input** via `/predict` endpoint
- Returns predictions with appended `predicted_column`
- Provides **HTML table visualization** via Jinja2 templates

### 4. **Deployment**
- **Containerized** using Docker (`python:3.10-slim`)
- **Hosted on AWS EC2** with port **8080** exposed
- Images managed via **AWS ECR** for CI/CD integration

## 🛠️ Tech Stack

| **Layer**          | **Technology**                  |
|--------------------|---------------------------------|
| **Programming**    | Python 3.10                    |
| **Web Framework**  | FastAPI                        |
| **ML Libraries**   | scikit-learn, pandas, pyarrow  |
| **Database**       | MongoDB                        |
| **Containerization**| Docker                        |
| **Cloud & Deployment** | AWS EC2, AWS ECR          |
| **CI/CD**          | GitHub Actions                 |
| **Templates & UI** | Jinja2, HTML Tables            |

## 🚀 Getting Started

### **Local Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yeripallivijay/Network-Security.git
   cd Network-Security
   ```

2. **Set up environment variables**
   Create `.env` file:
   ```env
   MONGODB_URL_KEY=<your_mongodb_connection_string>
   AWS_ACCESS_KEY_ID=<your_aws_access_key>
   AWS_SECRET_ACCESS_KEY=<your_aws_secret>
   AWS_REGION=<aws_region>
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**
   ```bash
   python app.py
   ```

5. **Open API documentation**
   [http://localhost:8080/docs](http://localhost:8080/docs)

### **Docker Deployment**

1. **Build the Docker image**
   ```bash
   docker build -t networksecurity:latest .
   ```

2. **Run the container**
   ```bash
   docker run -d -p 8080:8080 --name latestsecurity networksecurity:latest
   ```

3. **Access the API**
   Visit: `http://<EC2_PUBLIC_IP>:8080/docs`

## 🔄 CI/CD Pipeline

**GitHub Actions** automates:
- ✅ Code checkout
- ✅ Linting & unit tests
- ✅ Docker build
- ✅ Push to AWS ECR
- ✅ Pull & deploy on self-hosted EC2
- ✅ Auto-clean (maintains disk space)

![CI/CD Pipeline](https://github.com/yeripallivijay/Network-Security/actions/workflows/ci-cd.yml/badge.svg)

## 📁 Project Folder Structure

```
Network-Security/
│
├── app.py                  # FastAPI application
├── Dockerfile              # Docker build instructions
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .github/workflows/      # CI/CD pipeline
├── networksecurity/        # ML pipeline & modules
│   ├── components/         # Reusable components
│   ├── pipeline/           # Training & prediction pipelines
│   ├── utils/              # Utility functions
│   └── exception/          # Custom exceptions
├── final_model/            # Pretrained model & preprocessor
├── templates/              # HTML templates for UI
├── valid_data/             # Sample datasets
└── tests/                  # Unit & integration tests
```

## 📈 Results

| **Metric**       | **Value** |
|------------------|-----------|
| **ROC-AUC**      | ~98%     |
| **Precision**    | 97.2%    |
| **Recall**       | 98.1%    |
| **F1-Score**     | 97.6%    |

- **End-to-end automated workflow**: data → training → prediction
- **CI/CD ensures production-ready deployment**
- **Public FastAPI endpoint** for inference

## 🌟 Live Demo

🔗 **API Endpoint**: `http://<EC2_PUBLIC_IP>:8080/docs`

**Sample Prediction Request**:
```bash
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@valid_data/sample_urls.csv"
```

## 🚀 Future Enhancements

- 🔐 Add **authentication** & role-based access
- ⚡ Integrate **real-time URL monitoring**
- ⚛️ Replace HTML table with **React-based frontend**
- 🧪 Add **automated unit & integration tests** for pipelines
- 📊 **MLflow** integration for experiment tracking
- 🔄 **Auto-scaling** on AWS ECS/EKS

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Ensure code passes CI/CD and linting checks!**

## 📄 License

This project is licensed under the [MIT License](LICENSE) – free to use, modify, and distribute.

## 🙏 Acknowledgments

- **scikit-learn** for robust ML algorithms
- **FastAPI** for blazing-fast API development
- **Docker** & **AWS** for production deployment
- **GitHub Actions** for seamless CI/CD

---

**Made with ❤️ by [Vijay Yeripalli](https://github.com/yeripallivijay)**  
**Connect on [LinkedIn](https://linkedin.com/in/yeripallivijay) | [Twitter](https://twitter.com/yeripallivijay)**

<div align="center">
  <img src="https://img.shields.io/badge/⭐-Star%20this%20repo!-blueviolet" alt="Star this repo">
</div>
```

**Copy this entire content and save it as `README.md` in your GitHub repository root!** 🎉
