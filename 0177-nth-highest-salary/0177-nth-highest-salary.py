import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    unique_salaries = (
        employee['salary']
        .drop_duplicates()
        .sort_values(ascending=False)
    )
    
    column = f'getNthHighestSalary({N})'
    
    # Invalid N or not enough distinct salaries
    if N < 1 or N > len(unique_salaries):
        return pd.DataFrame({column: [None]})
    
    # Nth highest
    salary = unique_salaries.iloc[N - 1]
    
    return pd.DataFrame({column: [salary]})