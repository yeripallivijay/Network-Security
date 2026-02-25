<div align="center">
  <h1>🔐 Network Security & Anomaly Detection</h1>
  <p>Full Stack Data Science Pipeline — MLflow, Docker, Production Deployment</p>
  
  <!-- Badges -->
  <a href="https://github.com/yeripallivijay/Network-Security/stargazers">
    <img src="https://img.shields.io/github/stars/yeripallivijay/Network-Security?style=social" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/yeripallivijay/Network-Security/network/members">
    <img src="https://img.shields.io/github/forks/yeripallivijay/Network-Security?style=social" alt="GitHub Forks" />
  </a>
  <a href="https://github.com/yeripallivijay/Network-Security/issues">
    <img src="https://img.shields.io/github/issues/yeripallivijay/Network-Security" alt="Issues" />
  </a>
  <a href="https://github.com/yeripallivijay/Network-Security/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/yeripallivijay/Network-Security" alt="License" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue" alt="Python" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Docker-Production-green" alt="Docker" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/MLflow-2.10%2B-orange" alt="MLflow" />
  </a>
</div>

---

## 🎯 Full Stack Data Science Showcase

**End-to-end ML pipeline** for **network anomaly detection** — from raw data ingestion to production deployment.

**As a Full Stack Data Scientist**, this project demonstrates:

- 🔄 **Complete MLOps workflow** (ETL → Training → Deployment)
- 📊 **Advanced feature engineering** on network traffic data
- 🤖 **Ensemble ML models** with hyperparameter tuning
- 🖥️ **Production web application** (Flask + Docker)
- 📈 **Experiment tracking** (MLflow)
- ☁️ **Scalable deployment** practices

---

## 🖼 Live Demo

**Model Predictions Dashboard**  
![Predictions](screenshots/dashboard.png)

**Data Pipeline Flow**  
![ETL Pipeline](screenshots/pipeline.png)

**Model Performance Metrics**  
![Metrics](screenshots/metrics.png)

---

## 🛠 Data Science Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Data Pipeline** | Pandas, PyArrow, Dask |
| **Feature Engineering** | Scikit-learn, Featuretools |
| **Modeling** | XGBoost, RandomForest, MLflow |
| **API/Backend** | Flask, FastAPI |
| **Database** | MongoDB, SQLAlchemy |
| **MLOps** | MLflow, Docker, GitHub Actions |
| **Visualization** | Plotly, Streamlit |

---

## 🚀 Production Deployment

### Local Development
```bash
git clone https://github.com/yeripallivijay/Network-Security.git
cd Network-Security
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py  # http://localhost:8080
Docker Production
bash
docker build -t network-security .
docker run -p 8080:8080 -e MLFLOW_URI=mlflow network-security
MLflow Experiments
bash
mlflow ui  # Track all experiments at http://localhost:5000
📊 Model Performance Matrix
Model	Accuracy	F1-Score	ROC-AUC	Training Time
XGBoost	97.8%	97.4%	0.99	2.1s
Random Forest	96.5%	96.2%	0.98	3.4s
LightGBM	97.1%	96.8%	0.98	1.8s
Dataset: 500K+ network packets
Features: 22 engineered features (packet size, protocol, timing)

🔬 Data Science Workflow
text
1. DATA INGESTION → Raw CSV → MongoDB
2. FEATURE ENGINEERING → 22 features
3. MODEL TRAINING → MLflow experiments
4. MODEL EVALUATION → Cross-validation
5. API DEPLOYMENT → Flask + Docker
6. MONITORING → MLflow + custom metrics
📁 Repository Structure
text
Network-Security/
├── src/
│   ├── data/          # ETL pipelines
│   ├── features/      # Feature engineering
│   ├── models/        # Training + evaluation
│   └── api/           # Flask application
├── models/            # Saved production models
├── mlruns/            # MLflow tracking
├── data/              # Raw + processed datasets
├── app.py             # Production entrypoint
├── Dockerfile
└── requirements.txt
🌟 Full Stack Data Scientist Skills Demonstrated
✅ Data Engineering: ETL pipelines, data validation
✅ Machine Learning: Ensemble methods, hyperparameter tuning
✅ MLOps: MLflow, model versioning, experiment tracking
✅ Full Stack: Flask API, Docker deployment, web UI
✅ Production: Scalable, containerized, monitored

🚀 Next Phase Roadmap
 Real-time inference (Kafka + FastAPI)

 AutoML integration (H2O.ai)

 Cloud MLOps (AWS SageMaker / Vertex AI)

 A/B testing framework

 Model monitoring (Drift detection)

📞 Vijay Yeripalli
Full Stack Data Scientist | ML Engineer

Portfolio
LinkedIn
Email

💼 Production ML system showcasing complete data science lifecycle — from messy data to scalable APIs. Interview-ready for Data Scientist / ML Engineer roles.

<div align="center"> <img src="https://img.shields.io/badge/⭐%20Star%20This%20Repo!-000000?style=social&logo=github" alt="Star Repo" /> </div> ```
