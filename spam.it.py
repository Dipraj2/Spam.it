import pyautogui
import time
print("---------Welcome to SPAM.it-------\n")
print("Note : Dont use it for bad perpose !\n")
print("Created By Artim(Dipraj)\n")
time.sleep(2)
x = int(input("Enter how many time you want to comment : "))
comments1 = input("What you want to comment1: ")
comments2 = input("What you want to comment2: ")
comments = [comments1,comments2]
s = int(input("Enter time to wait after a comment (in second) :"))
print("You have 60 second to open the sight and click on the target comment!\nPress ctrl+x to stop it.")
time.sleep(6)

for i in range(x):
    pyautogui.typewrite(comments[i%2])
    pyautogui.typewrite("\n")
    time.sleep(s)