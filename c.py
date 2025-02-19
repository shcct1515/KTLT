import os
""" def createfile(direction, content):
    if os.path.exists(direction):
        f = open(direction, "a", encoding="utf8")
    else:
        f= open(direction, "w", encoding="utf8")
    f.write(content)
    f.close() """

def createfile(direction, content):
    try:
        f = open(direction, "a", encoding="utf8")
    except FileNotFoundError:
        f= open(direction, "w", encoding="utf8")
    f.write(content)
    f.close()

userinput1 = input("nhap duong dan file: ")
filename = input("nhap ten file: ")
direction = rf"{userinput1}\{filename}"
print(direction)
content = input("nhap noi dung: ")
createfile(direction, content)