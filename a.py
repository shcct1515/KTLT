# viết hàm nhận vào tập tin txt trả về nội dung
def readfile(direction):
    f = open(direction, "r")
    data = f.readlines()
    f.close()
    return data

# viết hàm tạo file lưu vào ổ D với nội dung "I'm expent python"
def createfile(direction, userinput):
    f = open(direction, "a")
    f.write(userinput)
    f.close()

def count(direction, n):
    f = open(direction, "r")
    line =0
    for j in enumerate(f):
        line +=1
    return line

#tạo hàm đọc file theo từng dòng
def readlinefile(direction, n):
    f = open(direction, "r")
    data = []
    if n > count(direction, n):
        return "vuot qua so dong"
    if n ==0:
        return "so dong phai lon hon 0"
    for i in range(0, n):
        data.append(f.readline())
    f.close()
    return data

direction = r"D:\Library\open.txt"
n = int(input("nhap so dong ban muon doc: "))
print(readlinefile(direction, n))