# LeetCode Problem: 2877. Create DataFrame from List
# Difficulty: Easy
# Topic: Pandas

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])

    return df
