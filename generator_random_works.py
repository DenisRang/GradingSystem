import os
import random
from mimesis import Person

STUDENTS_COUNT = 50

new_directory = os.getcwd() + r'\New works'
person = Person('en')

for i in range(STUDENTS_COUNT):
    name_letter = person.name()[0]
    surname = person.surname()
    file_name = new_directory + '//' + name_letter + '.' + surname + '.'

    file_a1 = open(file_name + 'a1', 'w')
    random_grade = random.randint(30, 100)
    file_a1.write(str(random_grade))
    file_a1.close()

    file_a2 = open(file_name + 'a2', 'w')
    random_grade = random.randint(30, 100)
    file_a2.write(str(random_grade))
    file_a2.close()

    file_a3 = open(file_name + 'a3', 'w')
    random_grade = random.randint(30, 100)
    file_a3.write(str(random_grade))
    file_a3.close()

    file_p = open(file_name + 'p', 'w')
    random_grade = random.randint(30, 100)
    file_p.write(str(random_grade))
    file_p.close()

    file_m = open(file_name + 'm', 'w')
    random_grade = random.randint(30, 100)
    file_m.write(str(random_grade))
    file_m.close()

    file_f = open(file_name + 'f', 'w')
    random_grade = random.randint(30, 100)
    file_f.write(str(random_grade))
    file_f.close()
