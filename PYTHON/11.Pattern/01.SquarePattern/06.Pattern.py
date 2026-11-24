'''
Enter the number of rows : 5
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1  '''

def get_pattern(n):
    for i in range(n):
        print((str((i+1)%2)+' ')*n)


num = int(input("Enter the number of rows : "))
get_pattern(num)