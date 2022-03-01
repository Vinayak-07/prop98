from tkinter import W


def swapFileData():
    file1 = input("enter the nameof file one")
    file2 = input("enter the nameof file two")
    with open(file1,'r') as a:
        data_a  = a.read()
    with open(file2,'r') as b:
        data_b  = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)
    print("file a has data " + data_a)
    print("\n file b has data" + data_b)
swapFileData()