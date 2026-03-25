<<<<<<< HEAD

# Student Dropout Synthetic Dataset

## Description
This dataset was synthetically generated to simulate the prediction of student dropout in undergraduate programs.

The objective is to apply supervised machine learning models to predict whether a student will drop out (Yes/No).

The dataset contains 500 records including demographic, academic, and financial variables.

---

## Variables

age
Student age (17 - 25 years)

gender
Male or Female

origin
Urban or Rural

high_school_avg
High school grade average (0 - 5 scale)

admission_score
Admission exam score (30 - 100)

first_semester_grade
First semester grade average (0 - 5 scale)

socioeconomic_level
Low, Medium, High

scholarship
Indicates if the student has a scholarship (Yes/No)

loan
Indicates if the student has a loan (Yes/No)

dropout
Target variable indicating if the student drops out (Yes/No)

---

## Null Values

Null values were added randomly in:

high_school_avg
first_semester_grade

Approximately 5% of the data contains null values to simulate real-world datasets.

---

## Outliers

Outliers were intentionally introduced:

high_school_avg contains values equal to 6

admission_score contains values equal to 120

These values simulate extreme academic cases.

---

## Objective

Predict student dropout using supervised learning classification models such as Logistic Regression.

---

## File Included

student_dropout_dataset.csv

---

## Author

Data Mining Project
Universidad de la Costa
=======
# generadordataset
>>>>>>> f2592636c358868e10131f4a2f10749ab56643b2
