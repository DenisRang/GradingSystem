import pandas as pd


def put_grade(student_name, task_name, grade):
    try:
        df = pd.read_excel('students.xls')
    except:
        df = pd.DataFrame({}, index=[])
        pass
    df.loc[student_name, task_name] = grade
    df.to_excel('students.xls')


def evaluate_students():
    df = pd.read_excel('students.xls')
    df['Total grade'] = df['a1'] * 0.1 + df['a2'] * 0.1 + df['a3'] * 0.1 + df['p'] * 0.1 + df['m'] * 0.3 + df['f'] * 0.3
    for i in range(len(df['Total grade'])):
        grade = df.iloc[i, 6]
        if (grade >= 85):
            df.iloc[i, 6] = 'A'
        elif (grade >= 70 and grade < 85):
            df.iloc[i, 6] = 'B'
        elif (grade >= 55 and grade < 70):
            df.iloc[i, 6] = 'C'
        else:
            df.iloc[i, 6] = 'D'
    df.to_excel('students.xls')
