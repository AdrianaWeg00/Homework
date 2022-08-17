#TASK 1

class CFGStudent:

    def __init__(self, name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id(self):
        import random
        id = random.randint(1000, 10000)

    def get_id(self):
    return f"Your ID number is: {id}"


    def get_fullname(self):
      return f"{self.name} , {self.surname}"


class NanoStudent(CFGStudent):

    def __init__(self, specialization, course_grades):
        self.specialization = specialization
        self.course_grades = course_grades

    @staticmethod
    def generate_id():
        import random
        id = random.randint(1000, 10000)
        full_id = "NANO" + id
        return f"Your ID  is: {full_id}"


    def add_new_grade(self, ):


    def get_course_grades(self):
        return f"{specialization} : {course_grade}"

print(CFGStudent.
      generate_id())
############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
def even_fibonacci_sum (limit):
    if ( limit < 2):
        return 0

    number1 = 0
    number2 = 2
    sum = number1 + number2

    while (number2 <= limit):

        number3 = 4 * ( number2 + number1 )

        if (number3 > limit):
            break

        number1 = number2
        number2 = number3
        sum = sum + number2

    return sum

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0




#TASK 3


def is_valid_subsequence(array, sequence):
    i = 0
    for valid in array:
        if i == len(sequence):
            break
        if sequence[i] == valid:
            i += 1
    return i == len(sequence)

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))

array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))

array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))

#TASK 4

#WRITTEN ASSIGNMENT

"""One of the important principles is that each class should be responsible one functionalty
and in this example there is only one class Employee with many many 
different properties. It should be seperated into more classes which will help to understand the code better.

"""










