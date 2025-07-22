# GYM-Calorie-Predictor
This project presents a machine learning model designed to predict the daily calorie intake needs for individuals engaged in gym or fitness routines. The primary goal is to assist users in identifying their appropriate calorie intake class—Low, Medium, or High—based on personal physical attributes and fitness goals.

The system takes user inputs such as age, height, weight, gender, dietary goal, and activity level, applying a machine learning model to provide a classification output that aids in crafting a more informed diet plan.
# Features
Personalized Calorie Prediction: Estimates daily calorie intake based on individual parameters.

Categorical Output: Classifies calorie needs into "Low," "Medium," or "High" categories.

User-Friendly Input: Prompts for essential physical attributes and fitness goals.

Data Validation: Includes basic validation for user inputs to ensure data integrity.

Python-Based: Developed entirely in Python for ease of implementation and future enhancements.

# Technologies Used
Python 3.6: The core programming language.

Pandas: For data manipulation and analysis.

Scikit-learn (sklearn):

LabelEncoder: For transforming categorical features (Gender, Goal) into numerical representations.

RandomForestRegressor: The machine learning algorithm used for predicting calorie values.

Joblib: For efficient saving and loading of the trained machine learning model.

# How to Run
Execute the Python Script:

python calorie_predictor.py

Provide User Input:
The script will prompt you to enter the following details:

Enter Age (years): (e.g., 25)

Enter Weight (kg): (e.g., 70.5)

Enter Height (cm): (e.g., 175)

Enter Gender (Male/Female): (e.g., Male)

Enter Goal (lose/gain/maintain): (e.g., gain)

Enter Activity Level (1-5): (e.g., 3)

View Prediction:
After you provide all inputs, the model will output the estimated daily calorie intake.

# Sample Output
--- Calorie Intake Prediction ---
Enter Age (years): 18
Enter Weight (kg): 80
Enter Height (cm): 170
Enter Gender (Male/Female): Male
Enter Goal (lose/gain/maintain): gain
Enter Activity Level (1-5): 5

✅ Estimated Daily Calorie Intake: 2850 calories

# Model Details
The project utilizes a RandomForestRegressor model to predict the continuous calorie value. This value is then rounded to provide an estimated daily calorie intake.

Data Preprocessing:

Categorical features (Gender, Goal) are transformed into numerical representations using LabelEncoder.

The model learns the relationship between user attributes and calorie requirements from the gym_diet_planner_dataset.csv.

Note on Classification: While the report mentions RandomForestClassifier and classifying into Low/Medium/High, the provided Python code uses RandomForestRegressor to predict a continuous calorie value. The output is a numerical calorie count, which can then be interpreted into calorie classes based on predefined thresholds (e.g., Low, Medium, High).

# Evaluation Metrics
The project report indicates that model performance is evaluated using metrics like F1 Score and Recall, which are typically used for classification tasks. This suggests an underlying classification logic or post-processing of the regressor's output into classes for evaluation.

# Future Improvements
Based on the project report, here are some potential enhancements:

Combined Output: Provide both the estimated exact calorie number and its corresponding calorie class (Low, Medium, High).

Web-Based Interface: Develop a user-friendly web application using frameworks like Flask or Streamlit for broader accessibility.

Meal Suggestion System: Integrate a feature that suggests meal plans based on the predicted calorie class.

Model Enhancement: Explore more advanced machine learning algorithms or expand the dataset for improved accuracy and generalization.

Mobile Support: Adapt the application for use on mobile devices.

# License
This project is open-source and available under the MIT License.

