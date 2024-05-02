import joblib

# Load the model
model = joblib.load('fraud_detection_model.joblib')

# Define feature names
feature_names = ['distance_from_home', 'distance_from_last_transaction', 'ratio_to_median_purchase_price',
                 'repeat_retailer', 'used_chip', 'used_pin_number', 'online_order']

# Function to make predictions
def predict_fraud(transaction_data, model):
    # Preprocess transaction data
    transaction_data = [transaction_data[key] for key in feature_names]
    # Use the trained model to predict
    probability_fraud = model.predict_proba([transaction_data])[:, 1]
    # Apply threshold (e.g., 0.5) to classify as fraud or not
    threshold = 0.5
    if probability_fraud >= threshold:
        prediction = "Fraudulent"
    else:
        prediction = "Legitimate"
    return prediction, probability_fraud[0]

# Test data
legitimate_transaction = {
    'distance_from_home': 10,
    'distance_from_last_transaction': 5,
    'ratio_to_median_purchase_price': 0.8,
    'repeat_retailer': 0,
    'used_chip': 1,
    'used_pin_number': 1,
    'online_order': 0
}

fraudulent_transaction = {
    'distance_from_home': 55,
    'distance_from_last_transaction': 190,
    'ratio_to_median_purchase_price': 9.0,
    'repeat_retailer': 0,
    'used_chip': 0,
    'used_pin_number': 0,
    'online_order': 0
}

# Test legitimate transaction
legitimate_prediction, legitimate_probability = predict_fraud(legitimate_transaction, model)
print("Legitimate Transaction Prediction:", legitimate_prediction)
print("Probability of Fraud:", legitimate_probability)

# Test fraudulent transaction
fraudulent_prediction, fraudulent_probability = predict_fraud(fraudulent_transaction, model)
print("Fraudulent Transaction Prediction:", fraudulent_prediction)
print("Probability of Fraud:", fraudulent_probability)
