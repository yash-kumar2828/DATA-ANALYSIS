while True:
    name = input("Enter your name : ")

    if name == 'kumar':
        raise ValueError("Don't provide the name as kumar")

    print(f"Good morning {name}")