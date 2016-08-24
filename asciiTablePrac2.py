def main():
    lower = 33
    upper = 127
    character = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character, ord(character)))
    get_Number(lower,upper)
    print("The character for {} is {:>3}".format(num, chr(num)))
    for i in range(lower, upper, 1):
     print("{} {:>3}".format(i, chr(i)))



def get_Number(lower,upper):
    try:
        num = int(input("Enter a number between {}-{}: ".format(lower, upper)))
    except ValueError:
        print("not a valid integer")
    return num
#not sure how to fix this?

main()

