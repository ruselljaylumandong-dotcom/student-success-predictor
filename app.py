import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Pass/Fail Predictor",
    page_icon="🎓",
    layout="centered",
)

@st.cache_resource
def load_artifacts():
    return joblib.load("student_engagement_model.joblib")

artifacts = load_artifacts()
model = artifacts["model"]
features = artifacts["features"]

# Mapping confirmed by the instructor for this assignment.
# The original Machine Problem 2 dataset contains High/Low rating labels,
# not independently recorded academic Pass/Fail outcomes.
OUTCOME_MAPPING = {"High": "Pass", "Low": "Fail"}

st.title("🎓 Student Pass/Fail Predictor")
st.write(
    "Enter a student's Learning Management System (LMS) activity counts "
    "to estimate whether the student is likely to pass or fail."
)

st.info(
    "For this assignment, the instructor-approved interpretation is "
    "**High = Pass** and **Low = Fail**. The underlying Machine Problem 2 "
    "dataset records High/Low ratings, so the application applies this "
    "mapping to the model's prediction."
)

st.subheader("Student information: LMS activity")
st.caption("Enter the number of recorded actions for the period being evaluated.")

defaults = {
    "Submission.Actions": 5,
    "Quiz.Actions": 1,
    "Forum.Actions": 1,
    "Create.Actions": 5,
    "Read.Actions": 50,
    "Update.Actions": 2,
    "Delete.Actions": 0,
    "Days.Logged.In": 10,
}

labels = {
    "Submission.Actions": "Submission actions",
    "Quiz.Actions": "Quiz actions",
    "Forum.Actions": "Forum actions",
    "Create.Actions": "Create actions",
    "Read.Actions": "Read actions",
    "Update.Actions": "Update actions",
    "Delete.Actions": "Delete actions",
    "Days.Logged.In": "Days logged in",
}

with st.form("prediction_form"):
    left, right = st.columns(2)
    values = {}
    for i, feature in enumerate(features):
        col = left if i % 2 == 0 else right
        with col:
            values[feature] = st.number_input(
                labels[feature],
                min_value=0,
                max_value=100000,
                value=defaults[feature],
                step=1,
                help="Enter a non-negative whole-number count.",
            )
    submitted = st.form_submit_button(
        "Predict Pass or Fail", type="primary", use_container_width=True
    )

if submitted:
    input_df = pd.DataFrame([[values[f] for f in features]], columns=features)
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    predicted_rating = str(artifacts["classes"][int(prediction)])
    predicted_outcome = OUTCOME_MAPPING.get(predicted_rating)
    confidence = float(probabilities[int(prediction)]) * 100

    st.divider()
    st.subheader("Prediction result")
    if predicted_outcome == "Fail":
        st.error("⚠️ Predicted outcome: FAIL")
        st.write(
            "Based on the instructor-approved mapping, the student's "
            "predicted rating is Low. Consider reviewing the student's "
            "learning activity and offering appropriate academic support."
        )
