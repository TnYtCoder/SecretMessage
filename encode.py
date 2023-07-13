import sys, time as t, os
from colorama import Fore , Back , Style

#banner
os.system("clear")
t.sleep(1.5)
print("")
print(Fore.GREEN , " ███████╗███╗░░██╗░█████╗░░█████╗░██████╗░███████╗")
t.sleep(0.1)
print(" ██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝")
t.sleep(0.1)
print(" █████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║█████╗░░")
t.sleep(0.1)
print(" ██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██╔══╝░░")
t.sleep(0.1)
print(" ███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝███████╗")
t.sleep(0.1)
print(" ╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚══════╝")
t.sleep(0.1)
print("")
print("[~]  GitHub : TnYtCoder")
print("[~]  A Python Tool To Store Password")
t.sleep(3)
print("")
print(Fore.LIGHTBLUE_EX , "")

# Get the text to be stored.
text = input("[>]  Eɴᴛᴇʀ Tᴇxᴛ Tᴏ Bᴇ Sᴛᴏʀᴇᴅ :  ")

# Convert the text to numerical code.
numerical_code = []
for character in text:
    numerical_code.append(ord(character))

t.sleep(1)
print("")

# Create a new file to store the numerical code.
file_name = input("[>]  Eɴᴛᴇʀ Tʜᴇ Fɪʟᴇ Nᴀᴍᴇ   Iɴᴄʟᴜᴅᴇ(.ᴛxᴛ) :  ")
with open(file_name, "w") as file:
    for number in numerical_code:
        file.write(str(number) + "\n")

#processing...

print("")
print("")
print(Fore.GREEN , "[>]  Processing...")
t.sleep(2)
print("")

# Print a message to indicate that the file has been created.
print("[>]  Yᴏᴜʀ Sᴇᴄʀᴇᴛ Fɪʟᴇ Hᴀs Bᴇᴇɴ Cʀᴇᴀᴛᴇᴅ ✓")
t.sleep(1.5)
