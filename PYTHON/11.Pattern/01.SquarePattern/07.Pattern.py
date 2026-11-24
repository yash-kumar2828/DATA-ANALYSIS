'''
Enter the number of rows : 5
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 '''

def get_pattern(n):
    for i in range(n):
        print((str(i%2)+' ')*n)

num = int(input("Enter the number of rows : "))
get_pattern(num)