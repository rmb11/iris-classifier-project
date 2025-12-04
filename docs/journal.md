# Project Development Journal

## Thursday, 20/11/2025 – Initial Teacher Discussion and Project Setup
- Chose the Iris dataset for the ML model. 
- Created the GitHub repository and set up the Project Board for planning.
- Met with lecturer to confirm project requirements and folder structure.
- Discussed using decorators for logging inputs, outputs and errors.
- Confirmed the project needs logging, an observer pattern and clear separation between Django and ML logic.
- Agreed to use Django for backend and Streamlit for the prediction interface.

## Monday, 24/11/2025 – Project Setup Session
- Cloned the repository and set up the virtual environment.
- Installed Django and created the project (`config`) and app (`classifier`).
- Implemented the required folder structure (ml, api, logs, docs) including template file.
- Updated README with project overview, MVP and folder structure.
- Completed first commit and pushed changes to GitHub.
- Removed previously created GitHub issues as they did not follow the specified issue template.
- Created Issue 8.1 using the correct structure provided in the assessment documentation.
- Added detailed Model Research and Justification section to the README.

## Tuesday, 25/11/2025 – Data Ingestion & Streamlit Integration
- Began Stage 8.2 - Data Ingestion and Preparation.
- Created `streamlit_app.py` in the project root and connected it to the placeholder `predict()` function in `ml/predict.py`.
- Added number input fields for sepal length, sepal width, petal length and petal width using Streamlit’s built-in validation.
- Tested inputs and confirmed values were successfully passed into `predict()` during runtime.
- Reviewed teacher’s Streamlit example and adapted it.
- Confirmed end to end flow works correctly. 

## Wednesday, 26/11/2025 – Model Training & Integration
- Completed Stage 8.3 (Model Training and Serialisation).
- Installed scikit-learn and trained a Logistic Regression model using the Iris dataset via a separate training script.
- Exported the trained model using joblib and saved it as `iris_model.joblib` in the `ml/` folder.
- Updated `predict()` to import and load trained model instead of using placeholder logic.
- Tested end to end prediction in Streamlit using the real model.

## Tuesday, 02/12/2025 - Adding Issue
- Began deployment steps last week but then paused them to follow milestones in the correct order.
- Added Issue 8.5 Add Testing and Logging which was missed in the initial documentation. 

# Wednesday, 03/12/2025 - Branch Cleanup
- Spent time reviewing Django class notes and documentation to prepare for the next milestones. 
- Created a few test branches today to experiment with logging and views.
- Deleted the unused test branches to keep the repository clean and easier to manage.