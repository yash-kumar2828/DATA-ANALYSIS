with open("Sample2.txt","r") as f:
    print(f.seek(5))
    print(f.read(6))
    
    print(f.seek(0))
    print(f.read(4))