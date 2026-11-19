with open("Sample2.txt","r") as f:
    print(f.tell())
    print(f.read(7))
    print(f.tell())