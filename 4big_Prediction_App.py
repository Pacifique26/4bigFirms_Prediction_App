import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv(r'C:\Users\pacif\Desktop\big4_financial_risk_compliance.csv')

# Feature Engineering
df['AI_Used_for_Auditing'] = df['AI_Used_for_Auditing'].map({'Yes':1, 'No':0})

# Target: High Fraud (binary)
df['High_Fraud'] = df['Fraud_Cases_Detected'].apply(lambda x: 1 if x > 50 else 0)

# Features
X = df[['High_Risk_Cases','Compliance_Violations','AI_Used_for_Auditing','Employee_Workload']]
y = df['High_Fraud']

# Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))