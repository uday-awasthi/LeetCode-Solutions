🧠 Problem Statement

Given a DataFrame students, select the name and age of the student whose student_id = 101.

students DataFrame:

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

## SOlutions
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[
        students['student_id'] == 101,
        ['name', 'age']
    ]
