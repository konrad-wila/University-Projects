 #Task1
letter_dict = dict()
#import numpy as np


def letter_counter(message: str):
    """
    Takes a word/message and returns a tuple that contains the letter frequency
    :param message: Enter a word or a message
    :return: Returns a tuple containing the letter frequency
    """
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
    """ Converts a dictionary to tuple
    :return: Dictionary converted into a tuple
    """
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
    def __init__(self, sn=" ", sid=0, sage=0, sms=0):
        self.student_id = sid
        self.student_age = sage
        self.student_marks = sms
        self.student_name = sn

    def get_student_age(self):
        return self.student_age

    def set_student_age(self, sage):
        self.student_age = sage

    def student_marks(self, sms):
        self.student_marks = sms

    def get_student_marks(self):
        return self.student_marks

    def __str__(self):
        return f"Student {self.student_name} of age {self.student_age} has student id {self.student_id} and has attained {self.student_marks} marks"


if __name__ == '__main__':

    name = str(input("Enter name of the student: "))
    sid = int(input("Students id: "))
    age = int(input("Student age: "))
    marks = int(input("Student marks: "))
    s = Student(name, sid, age, marks)
    print(s)
    s.set_student_age(20)
    print(s.get_student_age())
    print(s)





