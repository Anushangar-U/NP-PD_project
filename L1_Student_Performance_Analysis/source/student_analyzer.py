import numpy as np
import pandas as pd

df = pd.read_csv(r"python\numpy_project\L1_Student_Performance_Analysis\data\data.csv")

#fixing missing values with avg of that column
AssignmentMarkAvg = df["Assignment_Mark"].mean()
ExamMarkAvg = df["Exam_Mark"].mean()

df = df.fillna({"Assignment_Mark":AssignmentMarkAvg,"Exam_Mark":ExamMarkAvg})

print(df.to_string)

#converting columns to arrays
Attendance_arr = df["Attendance_%"].values
Assignment_Mark_arr = df["Assignment_Mark"].values
Exam_Mark_arr = df["Exam_Mark"].values

#Calculate the final score
df["Final_score"] = (Assignment_Mark_arr * 0.3) + (Exam_Mark_arr * 0.7)

#Use np.where to create the FAIL/PASS columns

df["Final_score_fail"] = np.where(df["Final_score"] < 50, "FAIL", "PASS")
df["Attendance_fail"] = np.where(df["Attendance_%"] < 75, "FAIL", "PASS")

#Classifying students at risk
df["Overall_Status"] = np.where(
    (df["Final_score_fail"] == "FAIL") | (df["Attendance_fail"] == "FAIL"), "At Risk", "Safe")

#Filtering the students at risk
Student_at_risk = (df[df["Overall_Status"] == "At Risk"])
print(Student_at_risk)

#summary stats of the class
print(f"Average score : {df['Final_score'].mean()}")
print(f"Lowest score : {df['Final_score'].min()}")
print(f"highest score : {df['Final_score'].max()}")
print(f"Number of students at risk : {len(Student_at_risk)}")

#saving analyzed data
df.to_csv(r"python\numpy_project\L1_Student_Performance_Analysis\data\analyzed_data.csv")
Student_at_risk.to_csv(r"python\numpy_project\L1_Student_Performance_Analysis\data\student_at_risk.csv")