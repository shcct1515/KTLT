try:
    a =10
    b =5
    c = a/b
    print("dap an la: ", c)
except ValueError:
    print("so ko hop le")
except ZeroDivisionError:
    print("ko the chia cho 0")
else:
    print("t thich chay vay do")