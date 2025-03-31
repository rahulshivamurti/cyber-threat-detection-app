import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# Load dataset
data = pd.read_csv("cyber_dataset.csv")

# Combine all relevant fields into a single feature text
data['combined_text'] = data['log'] + " " + data['ip_address'] + " " + data['device'] + " " + data['location'] + " " + data['timestamp']

X = data['combined_text']
y = data['label']

# Train Model
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X, y)

# Save Model
joblib.dump(model, "cyber_model.pkl")
