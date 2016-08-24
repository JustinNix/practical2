'''
1
outFile = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=outFile) # or outFile.write(name)
outFile.close()

2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

'''

'''Excercise 3 '''

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()
