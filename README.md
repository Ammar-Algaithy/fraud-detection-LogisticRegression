# fraud-detection-LogisticRegression

# Objective

The objective of this project is to develop a fraud detection system for a banking web application. Leveraging machine learning techniques, specifically logistic regression, the system aims to classify transactions as fraudulent or legitimate based on various features associated with each transaction.

# Data Overview

The dataset used for this project was obtained from Kaggle, https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud/suggestions?status=pending&yourSuggestions=true, and consists of transaction data with the following features:

Distance from Home: Distance from the cardholder's home to where the transaction occurred.

Distance from Last Transaction: Distance from the location of the last transaction.

Ratio to Median Purchase Price: Ratio of the purchase price of the transaction to the median purchase price.

Repeat Retailer: Indicates whether the transaction occurred at the same retailer as a previous transaction.

Used Chip: Indicates whether the transaction was conducted using a chip-enabled credit card.

Used Pin Number: Indicates whether the transaction was authenticated using a personal identification number (PIN).

Online Order: Indicates whether the transaction was made online.

Fraud (Target Variable): Indicates whether the transaction is fraudulent.

# Model Training

A logistic regression model is trained on the training data with hyperparameter tuning performed using grid search with cross-validation to find the optimal value of the regularization parameter (C). The best model is selected based on the hyperparameters yielding the highest accuracy on the validation set.

# Model Evaluation

The trained model is evaluated on the test data using metrics such as accuracy, confusion matrix, and classification report.

# Model Interpretation

Feature importance is analyzed using ELI5 and SHAP (SHapley Additive exPlanations) methods. ELI5 library is used to visualize feature weights, indicating their impact on the model's predictions, while SHAP values are calculated to explain the impact of each feature on individual predictions.

# Testing

The model is tested on both legitimate and fraudulent cases using sample transactions. Predictions are made, and the probability of fraud is calculated for each transaction.

# Summary

This project demonstrates the development of a fraud detection system for a banking web application using logistic regression. By leveraging machine learning techniques and interpreting model predictions, the system can effectively identify fraudulent transactions and mitigate financial risks. Further enhancements and refinements can be made to optimize the system's performance and ensure robustness in real-world scenarios.

# Conclusion

In conclusion, this project showcases the application of machine learning in developing a fraud detection system for banking web applications. By leveraging the provided dataset and implementing logistic regression, the system demonstrates promising results in identifying fraudulent transactions. Continued refinement and improvement of the model can further enhance its effectiveness in real-world scenarios.
