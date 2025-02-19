def readline(direction):
    f = open(direction, "r")
    n=0
    while(n <= 5):
        data = f.readline(n)
        n +=1
    f.close()
    return data

#userinput1 = input("nhap duong dan file: ")
#filename = input("nhap ten file: ")
#direction = rf"{userinput1}\{filename}"
print(readline(r"D:\Study Project\KTLT\test\open.txt"))