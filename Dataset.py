import pandas as pd
import numpy as np


np.random.seed(42)

n = 500


data = {
    "age": np.random.randint(17, 26, n),

    "gender": np.random.choice(
        ["Male", "Female"], n
    ),

    "origin": np.random.choice(
        ["Urban", "Rural"], n
    ),

    "high_school_avg": np.round(
        np.random.normal(3.5, 0.8, n), 2
    ),

    "admission_score": np.random.randint(
        30, 100, n
    ),

    "first_semester_grade": np.round(
        np.random.normal(3.2, 0.9, n), 2
    ),

    "socioeconomic_level": np.random.choice(
        ["Low", "Medium", "High"], n
    ),

    "scholarship": np.random.choice(
        ["Yes", "No"], n
    ),

    "loan": np.random.choice(
        ["Yes", "No"], n
    )
}


df = pd.DataFrame(data)


df["dropout"] = np.where(
    (df["first_semester_grade"] < 3.0) |
    (df["admission_score"] < 50) |
    (df["socioeconomic_level"] == "Low"),
    "Yes",
    "No"
)


for column in ["high_school_avg", "first_semester_grade"]:
    df.loc[
        df.sample(frac=0.05).index,
        column
    ] = np.nan


df.loc[
    df.sample(5).index,
    "high_school_avg"
] = 6

df.loc[
    df.sample(5).index,
    "admission_score"
] = 120

# Guardar dataset en CSV
df.to_csv(
    "student_dropout_dataset.csv",
    index=False
)

# Mostrar primeras filas
print(df.head())

print("\nDataset creado correctamente")
readme_text = """
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




Predict student dropout using supervised learning classification models such as Logistic Regression.

---



student_dropout_dataset.csv

---



Data Mining Project
Universidad de la Costa
"""

# guardar archivo
with open("README.md", "w") as file:
    file.write(readme_text)

print("README.md creado correctamente")