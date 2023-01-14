#Task1
letter_dict = dict()
#import numpy as np


def letter_counter(message: str):
    for letters in message:
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
            letter_dict[letters] = 1

    count = 0

    for k, v in letter_dict.items():
        count += v

    return f"Number of letters in {message} are {count}"


def dict_to_tuples():
    converted = [(k, v) for k, v in letter_dict.items()]
    # converted = List(letterdict.items())
    return converted


if __name__ == "__main__":
    while True:
        letter_dict = dict()
        msg = str(input("Enter a message: "))
        print(letter_counter(msg))
        print(dict_to_tuples())



#Task2
def get_product(text: str):
    mult = 1
    res = 0
    numbers = text.split("*")
    convert = [float(n) for n in numbers]
    for num in convert:
        mult *= num
        # alternatively we can also use prod(from numpy)
        #res = np.prod(convert)
    return mult, res


if __name__ == "__main__":
    print(get_product("4*3*2*1"))



#Task 3


class Student:
    def __init__(self, student_name=" ", student_id=0, student_age=0, student_marks=0):
        self.student_id = student_id
        self.student_age = student_age
        self.student_marks = student_marks
        self.student_name = student_name

    def set_student_age(self, sage):
        self.student_age = sage

    def get_student_age(self):
        return self.student_age

    def student_marks(self, mark):
        self.student_marks = mark

    def get_student_marks(self):
        return self.student_marks

    def __str__(self):
        return f"Student {self.student_name} of age {self.student_age} has student id {self.student_id} and has attained {self.student_marks} marks"




if __name__ == '__main__':
    s = Student
    name = str(input("Enter name of the student: "))
    sid = int(input("Students id: "))
    age = int(input("Student age: "))
    marks = int(input("Student marks: "))
    print(s(name, sid, age, marks))
    s.set_student_age(sid)




