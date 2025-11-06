# 🧠 Bankruptcy Prediction using Machine Learning

## 📘 Overview
This project predicts company bankruptcy using advanced **machine learning models**.  
It demonstrates a complete end-to-end workflow — from **data wrangling** and **resampling** to **model tuning**, **evaluation**, and **deployment** — comparing three approaches: **Decision Tree**, **Random Forest**, and **Gradient Boosting**.

The goal is to identify financial risk early by analyzing company metrics such as liquidity, leverage, and profitability indicators.

---

## ⚙️ Project Highlights
- 🧩 **Data Preprocessing**: Handled missing values with `SimpleImputer` and balanced the dataset using `RandomOverSampler`.
- 🌳 **Decision Tree**: Built an interpretable baseline model.
- 🌲 **Random Forest**: Improved model generalization through ensembling.
- 🚀 **Gradient Boosting**: Delivered the highest accuracy by sequentially correcting model errors.
- 📊 **Evaluation**: Used cross-validation, accuracy, precision, recall, and confusion matrices for model assessment.
- 💾 **Deployment**: Serialized the best model (`model-5-3.pkl`) and implemented a reusable `make_predictions()` function.

---

## 🔧 Hyperparameter Tuning
Model optimization was performed using **GridSearchCV** with **5-fold cross-validation** to ensure robustness and prevent overfitting.  
Key hyperparameters tuned:
- `imputer__strategy`: `["mean", "median"]`
- `max_depth`: `[10, 20, 30, 40, 50]`
- `n_estimators`: `[25, 50, 75, 100]`

This systematic tuning enhanced performance and reduced bias across all ensemble models.

---

## 🧰 Tech Stack
**Python**, **pandas**, **scikit-learn**, **imbalanced-learn**, **matplotlib**, **ipywidgets**

---

## 📈 Results
| Model | Accuracy | Highlights |
|--------|-----------|-------------|
| Decision Tree | Moderate | Baseline interpretability |
| Random Forest | Higher | Reduced overfitting |
| Gradient Boosting | Best | Balanced precision & recall |

---

## 🙋‍♂️ About Me
Hi, I’m **Pushkin Kumar** — a data enthusiast passionate about building predictive models and turning data into actionable insights.  

📫 [LinkedIn](https://www.linkedin.com/in/pushkin-kumar/) | [GitHub](https://github.com/Pushkin-Kumar/)

---
