# FitSense AI  
Clustering and Personalised Advisory System for Fitness and Healthy Lifestyle  

## 1. Introduction  

FitSense AI is an intelligent fitness advisory system developed as a Final Year Project. The system applies unsupervised machine learning techniques to analyse fitness-related data and generate personalised workout and dietary recommendations. Unlike traditional rule-based systems, FitSense AI identifies hidden patterns within user data to group individuals into meaningful fitness archetypes.

The application is built as a full-stack system integrating a machine learning pipeline, a backend API, and a frontend interface to deliver real-time predictions and recommendations.

---

## 2. Objectives  

The main objectives of this project are:

- To design an intelligent system capable of analysing fitness data without labelled outputs  
- To implement clustering techniques for discovering distinct fitness profiles  
- To develop a recommendation engine based on cluster characteristics  
- To provide a user-friendly interface for real-time interaction  
- To evaluate the effectiveness of unsupervised learning in personalised fitness advisory  

---

## 3. System Overview  

FitSense AI operates through a multi-stage pipeline:

1. Data preprocessing and cleaning  
2. Feature engineering to derive meaningful health indicators  
3. Dimensionality reduction using UMAP  
4. Clustering using HDBSCAN  
5. Model deployment via Flask API  
6. User interaction through a React frontend  
7. Generation of personalised fitness and dietary recommendations  

---

## 4. Technology Stack  

### 4.1 Machine Learning  

- Python 3.10  
- pandas  
- scikit-learn  
- umap-learn  
- hdbscan  

### 4.2 Backend  

- Flask  
- Flask-CORS  
- joblib  

### 4.3 Frontend  

- React 18  
- React Router  

### 4.4 Visualisation  

- matplotlib  
- seaborn  

---

## 5. Project Structure  

```
FYP_Fitness-Health-Advisory-App/
│
├── project/
│   ├── data/
│   │   ├── gym_members_exercise_tracking_synthetic_data.csv
│   │   └── output_with_activity_levels.csv
│   │
│   └── models/
│       ├── cluster_model.pkl
│       └── scaler.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── pruning.py
│   ├── feature_engineering.py
│   ├── clustering.py
│   ├── evaluation.py
│   └── recommendation.py
│
├── fitness-frontend/
│   └── src/
│       ├── App.js
│       ├── home.js
│       ├── fitness.js
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 6. Machine Learning Pipeline  

### 6.1 Data Preprocessing  

The dataset is cleaned to remove inconsistencies, missing values, and irrelevant attributes. Numerical features are standardised to ensure consistent scaling across all inputs.

### 6.2 Feature Engineering  

Several derived features are introduced to improve clustering performance:

- Body Mass Index (BMI)  
- Heart Rate Recovery (HRR)  
- BPM Efficiency  
- Intensity Score  
- Hydration Ratio  

These features provide deeper physiological insights beyond raw data.

### 6.3 Dimensionality Reduction  

UMAP (Uniform Manifold Approximation and Projection) is used to reduce high-dimensional data into a lower-dimensional representation while preserving the structure of the data.

### 6.4 Clustering  

HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) is applied to identify clusters of similar fitness profiles. The algorithm is capable of handling noise and irregular cluster shapes.

### 6.5 Model Storage  

The trained clustering model and scaler are saved using joblib for reuse during inference.

---

## 7. Recommendation System  

The recommendation engine generates outputs based on cluster assignment:

- Personalised workout suggestions  
- Estimated daily caloric needs  
- Macronutrient breakdown (protein, carbohydrates, fats)  

Caloric requirements are calculated using the Mifflin-St Jeor equation, ensuring realistic and personalised dietary guidance.

---

## 8. Backend API  

The backend is implemented using Flask and exposes endpoints for:

- Receiving user input data  
- Applying preprocessing and feature engineering  
- Performing cluster prediction  
- Returning recommendations in JSON format  

Flask-CORS is used to allow communication between the backend and frontend.

---

## 9. Frontend Application  

The frontend is developed using React and provides:

- User input forms for fitness data  
- API integration for real-time predictions  
- Display of personalised recommendations  

The interface is designed to be simple and intuitive for ease of use.

---

## 10. Installation Guide  

### 10.1 Clone Repository  

```bash
git clone https://github.com/your-username/FYP_Fitness-Health-Advisory-App.git
cd FYP_Fitness-Health-Advisory-App
```

### 10.2 Backend Setup  

```bash
pip install -r requirements.txt
```

### 10.3 Frontend Setup  

```bash
cd fitness-frontend
npm install
```

---

## 11. Running the System  

### 11.1 Start Backend  

```bash
python main.py
```

### 11.2 Start Frontend  

```bash
cd fitness-frontend
npm start
```

The application will run on a local development server and can be accessed through a web browser.

---

## 12. Dataset Description  

The system uses a synthetic dataset containing approximately 1,800 records of gym member activity. The dataset includes:

- Age  
- Weight  
- Height  
- Heart rate metrics  
- Workout duration  
- Exercise intensity  

This dataset simulates real-world fitness tracking scenarios.

---

## 13. Evaluation  

The clustering performance is evaluated using internal validation metrics and interpretability of cluster structures. A Random Forest classifier is also trained to replicate cluster labels, achieving high accuracy due to learning from the same feature space.

---

## 14. Limitations  

- Use of synthetic data instead of real-world datasets  
- Lack of temporal tracking of user progress  
- Limited personalisation without user history  
- No deployment in a production environment  

---

## 15. Future Work  

- Integration with wearable fitness devices  
- Deployment using cloud platforms  
- Mobile application development  
- Hybrid recommendation systems combining clustering and supervised learning  
- User authentication and long-term tracking  

---

## 16. Conclusion  

FitSense AI demonstrates the effectiveness of unsupervised machine learning in analysing fitness data and generating personalised recommendations. The system successfully integrates data processing, clustering, and web technologies into a cohesive application, highlighting the potential of intelligent systems in the health and fitness domain.

---

## 17. Author  

Final Year Project  
FitSense AI – Intelligent Fitness Advisory System  

---

## 18. License  

This project is developed for academic purposes. Redistribution and modification are permitted with proper attribution.