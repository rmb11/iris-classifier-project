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

## Wednesday, 03/12/2025 - Branch Cleanup
- Spent time reviewing Django class notes and documentation to prepare for the next milestones. 
- Created a few test branches today to experiment with logging and views.
- Deleted the unused test branches to keep the repository clean and easier to manage.

## Thursday, 04/12/2025 - Connecting Django API with Streamlit
- Added the /api/predict/ endpoint and view to handle POST requests and call the ML predict() function.
- Updated Streamlit to send the four iris values to Django using requests.post().
- Tested the full flow in Streamlit and confirmed the prediction shows correctly.
- Verified the API separately using curl which returned {"prediction": "setosa"}.
- Learned how Django processes JSON in POST requests and why @csrf_exempt is needed for external clients.
- Created the PR for Issue 8.4 after everything worked end-to-end.

## Thursday, 04/12/2025 – CI/CD Setup and Fixes
- Added the teacher’s GitHub Actions workflow file.
- Created a simple test and renamed the test file so CI could detect it.
- Committed the iris_model.joblib file to fix the failing workflow.
- Pushed the branch, opened a PR and confirmed the workflow passed.
- Merged the PR and closed the CI/CD issue.

## Friday, 05/12/2025 – Authentication + Permissions Setup
- Set up login, logout and signup using Django’s built-in auth.
- Updated base.html to show the logged-in user and a working Logout button.
- Protected the home page with @login_required and made /logs/ staff-only.
- Removed the unused dashboard to simplify the flow.
- Tested login, logout and staff access. Learned how Django handles redirects and permission decorators.
- Main challenge was figuring out the best login flow as the original redirect to Streamlit didn’t feel natural so I adjusted it.

## Friday, 05/12/2025 – Testing + Logging (Milestone 8.5)
- Added simple tests in tests.py to confirm the prediction view works.
- Created a basic logging decorator to record inputs, outputs and errors.
- Applied it to predict_api so predictions go to logs/app.log.
- Tested predictions through Streamlit and confirmed logs update correctly.
- Checked invalid inputs to make sure errors are handled safely.

## Saturday, 06/12/2025 – Prediction Metadata

- Added a database model to store prediction metadata.
- Updated prediction view to save a record for each prediction.
- Registered the model in the Django admin panel.
- Tested predictions through Streamlit and confirmed metadata saves correctly.