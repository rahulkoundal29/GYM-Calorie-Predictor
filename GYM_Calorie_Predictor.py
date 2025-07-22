import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

file_path = r"C:\Users\rahul koundal\Downloads\gym_diet_planner_dataset.csv"
df = pd.read_csv(file_path)

le_gender = LabelEncoder()
le_goal = LabelEncoder()

df['Gender'] = le_gender.fit_transform(df['Gender'])
df['Goal'] = le_goal.fit_transform(df['Goal'])


X = df.drop('Calories', axis=1)
y = df['Calories']


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# --- Prediction using User Input ---
print("\n--- Calorie Intake Prediction ---")

try:
    # Take user input
    age = int(input("Enter Age (years): "))
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (cm): "))
    gender_input = input("Enter Gender (Male/Female): ").strip().capitalize()
    goal_input = input("Enter Goal (lose/gain/maintain): ").strip().lower()
    activity_level = int(input("Enter Activity Level (1-5): "))

   
    if gender_input not in le_gender.classes_:
        raise ValueError("Invalid Gender. Please enter 'Male' or 'Female'.")
    
    if goal_input not in le_goal.classes_:
        raise ValueError("Invalid Goal. Please enter 'lose', 'gain', or 'maintain'.")
    
    if not (1 <= activity_level <= 5):
        raise ValueError("Activity level must be between 1 and 5.")

    
    gender = le_gender.transform([gender_input])[0]
    goal = le_goal.transform([goal_input])[0]

    
    input_data = pd.DataFrame([[age, gender, height, weight, goal, activity_level]],
                              columns=['Age', 'Gender', 'Height_cm', 'Weight_kg', 'Goal', 'Activity_Level'])

    
    predicted_calories = model.predict(input_data)[0]
    print(f"\n✅ Estimated Daily Calorie Intake: {round(predicted_calories)} calories")

except ValueError as ve:
    print(f"\n❌ Input Error: {ve}")
except Exception as e:
    print(f"\n⚠️ Unexpected Error: {e}")
