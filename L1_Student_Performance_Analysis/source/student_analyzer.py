import numpy as np
import pandas as pd

df = pd.read_csv(r"python\numpy_project\L1_Student_Performance_Analysis\data\data.csv")

#fixing missing values with avg of that column
AssignmentMarkAvg = df["Assignment_Mark"].mean()
ExamMarkAvg = df["Exam_Mark"].mean()

df = df.fillna({"Assignment_Mark":AssignmentMarkAvg,"Exam_Mark":ExamMarkAvg})

print(df.to_string)

#converting columns to arrays
Student_ID_arr = df["Student_ID"].values
Name_arr = df["Name"].values
Student_ID_arr = df["Student_ID"].values
