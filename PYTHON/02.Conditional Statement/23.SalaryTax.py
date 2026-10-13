# WAP to calculate tax of a person based on the given below :- salary 200000 and above then tax 30%, salary above 1500000 then tax 20%, salary above 1200000 then tax 10% and salary below 1200000 then no tax

sal = int(input("Enter your salary:"))
 
if sal<=1200000:
    print("No Tax")
 
elif sal<=1500000:
    tax = (sal-1200000)*10/100
    print(f"Your salary is {sal} then your tax is: {tax}")

elif sal<=2000000:
    tax = (300000*10/100)+(sal-1500000)*20/100
    print(f"Your salary is {sal} then your tax is: {tax}")

else:
    tax = (300000*10/100)+(500000*20/100)+(sal-2000000)*30/100
    print(f"Your salary is {sal} then your tax is: {tax}")