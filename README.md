
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Adityatyagi077/student-performance-analysis/blob/main/student_analysis.ipynb)

# 📊 Student Performance Analysis & Prediction (AWS + ML)

## 🔍 Overview
This project analyzes student performance data to identify key factors affecting academic scores and builds a machine learning model to predict student performance.

The project also integrates AWS S3 for cloud-based data storage and retrieval, simulating a real-world data pipeline.

---

## 🎯 Objectives
- Perform data cleaning and preprocessing
- Analyze relationships between study time, courses, and performance
- Visualize key insights using graphs
- Build a predictive machine learning model
- Integrate AWS S3 for cloud-based data access

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- AWS S3 (boto3)

---

## 📂 Dataset
- Student performance dataset (courses, study time, marks, grade)
- Data stored and accessed via AWS S3

---

## ☁️ AWS Integration
- Dataset uploaded to Amazon S3
- Accessed programmatically using boto3
- Demonstrates cloud-based data retrieval workflow

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

### 📈 Performance
- R² Score: **0.93**
- MAE: ~3 marks

---

## 💡 Key Insights
- Study time has a strong positive impact on student performance
- Increasing the number of courses does not guarantee better scores
- StudyTime is the most influential feature in prediction
- Model explains 93% of variation in student scores

---

## 📌 Conclusion
This project demonstrates how data analysis and machine learning can be combined with cloud technologies to build scalable and practical solutions. Study time emerges as the most critical factor influencing student performance, and the model shows strong predictive capability.

---

## 🚀 Future Improvements
- Add more features (attendance, sleep patterns)
- Try advanced ML models
- Build a dashboard (Streamlit / Power BI)
- Automate pipeline (S3 → ML → Output)

---

## 🔗 Project Link
👉 https://github.com/Adityatyagi077/student-performance-analysis

---

## 💼 Resume Highlight
Built an end-to-end student performance analysis and prediction system using Python and Scikit-learn, integrated with AWS S3 for cloud-based data handling, achieving an R² score of 0.93.
