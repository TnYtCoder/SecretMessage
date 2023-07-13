import sys , os , argparse
from colorama import Fore

# Get the name of the file containing the numerical code.
filename = sys.argv[1]

# Open the file and read the numerical code.
with open(filename, "r") as file:
    numerical_code = file.readlines()

# Convert the numerical code to text.
text = ""
for number in numerical_code:
    text += chr(int(number))

# Print the text.
print(Fore.LIGHTBLUE_EX , "Your Text :  ")
print("")
print(Fore.RED , text)
