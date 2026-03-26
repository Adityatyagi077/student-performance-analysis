
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Adityatyagi077/student-performance-analysis/blob/main/student_analysis.ipynb)

# 📊 Student Performance Analysis & Prediction

## 🔍 Overview
This project analyzes student performance data to identify key factors affecting academic scores. It also builds a Machine Learning model to predict student scores based on study behavior.

---

## 🎯 Objectives
- Perform data cleaning and preprocessing
- Analyze relationships between study time, courses, and performance
- Visualize key insights using graphs
- Build a regression model to predict student scores

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib & Seaborn
- Scikit-learn

---

## 📂 Dataset Features
- StudyTime
- NumberOfCourses
- Score
- Grade

---

## 🧹 Data Cleaning
- Removed duplicate records
- Standardized column names
- Converted data types
- Handled missing values

---

## 📊 Exploratory Data Analysis
- Distribution of student scores
- Study Time vs Score relationship
- Correlation heatmap
- Grade distribution

---

## 🤖 Machine Learning Model
- Model: Linear Regression
- Features: StudyTime, NumberOfCourses
- Target: Score

### 📈 Performance Metrics
- MAE: ~3 (average prediction error of 3 marks)
- R² Score: 0.93 (strong predictive performance)

---

## 💡 Key Insights
1. Study time has a strong positive impact on student performance.
2. Increasing the number of courses does not significantly improve scores.
3. The model explains 93% of the variance in student scores.
4. StudyTime is the most influential feature in predicting performance.

---

## ⚠️ Limitations
- Dataset may be small or simplified
- Model may not generalize to real-world scenarios without more features

---

## 🚀 Future Improvements
- Add more features (attendance, sleep, etc.)
- Try advanced ML models
- Deploy model using Flask or Streamlit
- Integrate with cloud storage (AWS S3)

---

## 📌 Conclusion
This project demonstrates how data analysis and machine learning can be used to uncover patterns in student performance and make accurate predictions based on study habits.

---
