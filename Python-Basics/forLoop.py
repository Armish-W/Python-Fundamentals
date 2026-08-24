#sum monthly expenses
monthly_expense=[10,20,30,4,5,2,3]
total=0
for i,j in enumerate(monthly_expense):
    total= total + j
    print(f"Month {i+1}, Expense:{j}")
print(f"Total expense is {total}.")

#other way
total1=0
for i in range(len(monthly_expense)):
    total1=total1+monthly_expense[i]
    print(f"For Month {i+1}, Expense is {monthly_expense[i]}")
print(f"Total of all expenses is {total1}.")


# for i in range (1,11):
#    print (i*i)

home=['socks','ball','bat','key','cat']
for i in home:
    if i=='key':
        print("Key is found in",i)
        break
    else:
        print("Key is not found in",i)

#square of 1-5 except even numbers
for i in range(1,6):
    if i%2==0:
        continue
    print (i*i)
    
    #while

    i=1
    while i<=5:
        print(i)
        i=i+1