"""
Arrays in python are dynamic, which means that the size of allocated
memory constantly changes as the program develops. 

Exercise: Array DataStructure

    Let us say your expense for every month are listed below,
        January - 2200
        February - 2350
        March - 2600
        April - 2130
        May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""
monthly_expenses = [2200, 2350, 2600, 2130, 2190]
# 1.
january = monthly_expenses[0]
february = monthly_expenses[1]
extra_expenses = february - january
print(f'Ex 1: I spent {extra_expenses} dollars extra.')

# 2.
expenses_1q = 0
for i in range(3):
    expenses_1q += monthly_expenses[i]
print(f"Ex 2: In first quarter my total expense was {expenses_1q}")

# 3.
for i in monthly_expenses:
    if i == 2000:
        print('Ex3: I spent exactly 2000 dollars in ',
              monthly_expenses.index(i), ' month')
# 4.
monthly_expenses.append(1980)
print(monthly_expenses)

# 5.
monthly_expenses[4] = monthly_expenses[3] - 200
print(monthly_expenses)
