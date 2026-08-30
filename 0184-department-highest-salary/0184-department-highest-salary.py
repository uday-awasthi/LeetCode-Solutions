import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Find highest salary in each department
    max_salary = employee.groupby("departmentId")["salary"].transform("max")
    
    # 2. Keep employees whose salary is the highest in their department
    result = employee[employee["salary"] == max_salary]
    
    # 3. Add department name
    result = result.merge(
        department,
        left_on="departmentId",
        right_on="id"
    )
    
    # 4. Select and rename required columns
    result = result[["name_y", "name_x", "salary"]]
    result.columns = ["Department", "Employee", "Salary"]
    
    return result