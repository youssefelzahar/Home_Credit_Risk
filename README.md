# Home Credit Risk Prediction

Welcome to the **Home Credit Risk Prediction** repository! This project aims to build a machine learning model to predict the probability of a client defaulting on a loan, using historical application data. The goal is to assist financial institutions in assessing loan eligibility and minimizing credit risk.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Models and Methodologies](#models-and-methodologies)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project utilizes machine learning techniques to analyze and predict loan default risk. By leveraging historical data, the model helps lenders make informed decisions. The repository includes the following:
- Data preprocessing and feature engineering.
- Exploratory data analysis (EDA).
- Model training and evaluation.
- Hyperparameter tuning for optimization.

## Features
- **Data Cleaning:** Handle missing values, outliers, and inconsistent data.
- **Feature Engineering:** Generate meaningful features from raw data.
- **Model Development:** Train and test multiple machine learning models.
- **Evaluation Metrics:** Use metrics like AUC, accuracy, and F1-score to assess performance.
- **Visualization:** Insightful plots for better understanding of the data and model results.

## Dataset
The dataset used in this project is from [Kaggle's Home Credit Default Risk competition](https://www.kaggle.com/competitions/home-credit-default-risk/data). It includes the following:
- Application data.
- Previous loan information.
- Bureau data.
- Demographic information.

### Key Columns:
- **TARGET:** 1 if the client defaulted on the loan, 0 otherwise.
- **Numerical and Categorical Features:** Various socio-economic and loan-related details.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/youssefelzahar/Home_Credit_Risk.git
   cd Home_Credit_Risk
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset from [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/data) and place it in the `data/` directory.
   ```

## Models and Methodologies
- **Exploratory Data Analysis (EDA):** Identify trends, correlations, and outliers.
- **Feature Engineering:** Techniques include:
  - Encoding categorical variables.
  - Handling missing values.
  - Scaling numerical features.
  - Generating interaction terms and polynomial features.
- **Models Tested:**
  - Decsion tree
  - Random Forest
  - Gradient Boosting (e.g., XGBoost, LightGBM)
    

## Results
- **Best Model:** [Your best model, e.g., LightGBM]
- **Key Metrics:**
  - AUC: [98]
  - F1-Score: [class 0-> 0.99
  - class 1-> 0.83]

Visualizations and performance summaries are available in the `results/` directory.

## Future Work
- Incorporate more advanced feature engineering techniques.
- Test deep learning models for further improvements.
- Deploy the model as a web application or API for real-time predictions.

## Contributing
Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

