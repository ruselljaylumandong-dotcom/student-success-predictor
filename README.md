# Student Success Predictor — Streamlit

## What this application does
This web application uses an Extra Trees Classifier trained on the supplied
`augmented_balanced_dataset_m.csv` dataset. Users enter eight LMS activity
counts and receive a predicted **High** or **Low engagement** category.

**Important target clarification:** The supplied dataset's target column is
`rating` with the labels `High` and `Low`. It does not contain a Pass/Fail
outcome. Therefore, this app does not claim to predict whether a student
passes or fails.

## Model details
- Dataset size: 3,602 records
- Input features: 8 numerical LMS activity variables
- Target: `rating` (High / Low)
- Train/test split: 80% / 20%, stratified
- Training records: 2,881
- Testing records: 721
- Algorithm: ExtraTreesClassifier
- Parameters: `n_estimators=250`, `min_samples_split=3`, `random_state=42`
- Test accuracy from this training run: 90.01%

## Run locally
1. Install Python 3.10 or newer.
2. Extract this project folder.
3. Open a terminal in the project folder.
4. Run:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
5. Open the local URL printed in the terminal (usually http://localhost:8501).

## Deploy free using Streamlit Community Cloud
1. Sign in to GitHub and create a **public** repository, for example
   `student-success-predictor`.
2. Upload these three files from this folder to the repository root:
   - `app.py`
   - `requirements.txt`
   - `student_engagement_model.joblib`
3. Visit https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app**, select your repository and branch, and set
   **Main file path** to `app.py`.
5. Click **Deploy** and wait for the app to finish building.
6. Copy the public `https://...streamlit.app` URL and submit that URL.

## Dataset feature meanings
- Submission.Actions — submission-related actions
- Quiz.Actions — quiz-related actions
- Forum.Actions — forum interactions
- Create.Actions — content creation actions
- Read.Actions — content reading actions
- Update.Actions — content update actions
- Delete.Actions — content deletion actions
- Days.Logged.In — days the student logged in

## Notes
The saved model was trained from the uploaded dataset. The CSV is not needed
to run the deployed app because the trained model is included in the project.
Predictions are decision-support estimates and should be reviewed by a human.
