import pandas

data = pandas.read_csv("lifestyle_data.csv")

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# leave your code under the comments.

# Find the total number of students
total_students = len(data)
print(f"Total number of students: {total_students}")

# Find the mean average GPA of the students
mean_gpa = data['GPA'].mean()
print(f"Mean average GPA: {mean_gpa}")

# Find the standard deviation of how much sleep students get per day
sleep_std = data['Sleep_Hours_Per_Day'].std()
print(f"Standard deviation of sleep hours: {sleep_std}")

# Find the maximum amount of study hours per day
max_study_hours = data['Study_Hours_Per_Day'].max()
print(f"Maximum study hours per day: {max_study_hours}")

# Sort the students by social hours per day ascending (lowest -> highest)
sorted_by_social = data.sort_values('Social_Hours_Per_Day')
print("Students sorted by social hours per day (ascending):")
print(sorted_by_social[['Social_Hours_Per_Day', 'GPA']].head())  # 显示前几行作为示例

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data['Total_hours'] = data[['Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day', 'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day', 'Physical_Activity_Hours_Per_Day']].sum(axis=1)
print("Added 'Total_hours' column. Sample:")
print(data[['Total_hours']].head())

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_stress = data[data['Stress_Level'] == 'High']
low_stress = data[data['Stress_Level'] == 'Low']
high_gpa_mean = high_stress['GPA'].mean()
low_gpa_mean = low_stress['GPA'].mean()
print(f"Mean GPA for high stress: {high_gpa_mean}")
print(f"Mean GPA for low stress: {low_gpa_mean}")
if high_gpa_mean > low_gpa_mean:
    print("Higher stress level is associated with higher GPA.")
else:
    print("Higher stress level is not associated with higher GPA.")
