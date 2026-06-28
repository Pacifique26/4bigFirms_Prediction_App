# 4bigFirms_Prediction_App

Financial Risk & Compliance: Prediction

## Short Presentation of the App

This Python application uses a Random Forest machine learning model to predict whether an audit engagement is likely to result in a high number of fraud cases. The model is trained on historical data from the Big 4 accounting firms (PwC, Deloitte, EY, and KPMG) and uses key audit-related indicators such as high-risk cases, compliance violations, AI usage in auditing, and employee workload.

## For Which Perspective the App Was Created

The application was developed from a risk management and audit analytics perspective. It is intended for students, researchers, and professionals interested in applying machine learning to financial risk assessment, fraud detection, and compliance monitoring. The project demonstrates how predictive analytics can support audit decision-making and identify engagements with elevated fraud risk.

## How to Use It

1. Install the required Python libraries (pandas and scikit-learn).
2. Place the CSV dataset in the specified directory or update the file path in the script.
3. Run the Python script.
4. The application automatically:
- Loads and preprocesses the dataset.
- Converts AI usage into numerical values.
- Creates a binary fraud-risk target.
- Splits the data into training and testing sets.
- Trains a Random Forest classifier.
- Evaluates the model using a classification report displaying precision, recall, F1-score, and accuracy.

## Summary

This project demonstrates a practical application of machine learning in financial auditing and compliance analysis. By leveraging historical audit data, the model predicts engagements with a higher likelihood of fraud, illustrating how AI-driven analytics can support risk assessment, improve audit planning, and enhance decision-making in the financial services sector.
