from fun1 import messagespam
from fun2 import stickerspam



def main(case):
    if case == 1:
        phone_no = int(input("Please enter the recipient's mobile number: "))
        n = int(input("How many times would you like to send the message? "))
        message = input("Please enter the message you'd like to send: ")
        messagespam(phone_no, n, message)
    elif case == 2:
        phone_no = int(input("Please enter the recipient's mobile number: "))
        folder = input(r"Please enter the folder path where the stickers are located (give path without " "): ")
        n = int(input("Please enter the number of images to send: "))
        stickerspam(phone_no,folder,n)

if __name__ == '__main__':
    case = int(input("Enter 1 for message spam or 2 for sticker spam: "))
    main(case)