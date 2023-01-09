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

    return letter_dict, f"Total number of letters are {count}"


if __name__ == "__main__":
    while True:
        letter_dict = dict()
        msg = str(input("Enter a message: "))
        print(letter_counter(msg))


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



