# Student Performance Analysis System

This project uses **Python**, **NumPy**, and **Pandas** to evaluate student performance based on attendance, assignments, and exam results. It automates the process of identifying "at-risk" students who fall below specific academic or attendance thresholds.

---

## 🚀 Features
* **Data Cleaning:** Automatically fills missing assignment and exam marks using the column mean to ensure calculation consistency.
* **Weighted Scoring:** Calculates a final grade based on a weighted average:
    * **Assignments:** 30%
    * **Final Exams:** 70%
* **Risk Assessment:** Flags students as "At Risk" if they meet either of the following criteria:
    * A final score below **50**.
    * Attendance below **75%**.
* **Automated Reporting:** Generates summary statistics (mean, min, max) and exports the results to CSV files.

---

## 🛠️ Tech Stack
* **Python 3.x**
* **Pandas:** For data manipulation and CSV handling.
* **NumPy:** For high-performance array operations and conditional logic.

---

## 📊 Calculation Logic
The script uses vectorized operations for efficiency. The final score is determined by:

$$FinalScore = (AssignmentMark \times 0.3) + (ExamMark \times 0.7)$$

[Image of a data analysis pipeline flowchart showing data ingestion, cleaning, calculation, and output]

A student is categorized as **At Risk** if:
1. `Final_score < 50` OR 
2. `Attendance_% < 75`
