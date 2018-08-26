# name for program should be i.ivanov.<task>
# task may be a# - assigments(3*10%), p - project(10%), m - midterm(30%), f - final exam(30%)
import os
import students_data_manager

# Evaluate specific task by "task_name". This method should contains some algorithm but in my case it just reads grade from file
def evaluate_task(task_name, file):
    grade = file.read()
    return grade

new_directory = os.getcwd() + r'\New works'
evaluated_directory = os.getcwd() + r'\Evaluated works'

for file_name in os.listdir(new_directory):
    index_dot2 = file_name.rfind(".", 0, len(file_name) - 1)
    student_name = file_name[0, index_dot2]
    task_name = file_name[index_dot2, len(file_name)]
    file_path = new_directory + '\\' + file_name

    file = open(file_path)
    grade = evaluate_task(task_name, file)
    students_data_manager.put_grade(student_name, task_name, grade)
    file.close()

    os.replace(file_path, evaluated_directory + '\\' + file_name)
