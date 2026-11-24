'''Enter the number of rows : 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *    '''


def get_pattern(n):
    for i in range(n):
        print("* "*(n))

n = int(input("Enter the number of rows : "))
get_pattern(n)