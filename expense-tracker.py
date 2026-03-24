expense={
    "food":120,
    "transport":60,
    "shopping":200
    }
print("1.Add Expense")
print("2.Update Expense")
print("3.Show All Expenses")
print("4.Show Total Expense")
print("5.Show Highest Expense")
print("6.Show Expense Ranking")
print("7.Save Data")
print("8.Load Data")
print("9.Exit")

def add_expense(category,cost):
    expense[category]=cost
def update_expense(category,new_cost):
    expense[category]=new_cost
def show_all():
    for category,cost in expense.items():
        print(f"{category}-{cost}")
def total_expense(expense_list):
    total=sum(cost for(category,cost) in expense_list)
    return total
def exp_list():
    expense_list=list((category,cost) for category,cost in expense.items())
    return expense_list
def show_highest(expense_list):
    highest=max(expense_list, key=lambda x:x[1])
    return highest
def show_rank(sorted_list):
     for i,(category,cost) in enumerate(sorted_list, start=1):
         print(f"{i}-{category}:{cost}")
def save_data(expense_list):
    with open ("data.txt","w") as f:
        for category,cost in expense_list:
            f.write(f"{category}-{cost}\n")
        print("data saved")
def load_data():
    expense.clear()
    with open("data.txt","r") as f:
        for line in f:
            line=line.strip()
            line=line.split("-")
            category=line[0]
            cost=int(line[1])
            expense[category]=cost
        print("data loaded")    
        

while True:
    try:
        ch=int(input("Enter your choice:"))
    except ValueError:
        print("Please enter only numbers")
    if ch==9:
        print("Thank You")
        break
    elif ch==1:
        category=input("Enter the expense category:")
        cost=int(input("Enter the amount:"))
        add_expense(category,cost)
    elif ch==2:
        category=input("Enter the category for which the cost is to be updated:")
        if category in expense:
            new_cost=int(input("Enter the new cost:"))
            update_expense(category,new_cost)
        else:
            print("The mentioned category is not there!")
    elif ch==3:
        show_all()
    elif ch==4:
        expense_list=exp_list()
        total=total_expense(expense_list)
        print(f"The total expense is :{total}")
    elif ch==5:
        expense_list=exp_list()
        highest=show_highest(expense_list)
        print(f"The highest expense is: {highest}") 
    elif ch==6:
        expense_list=exp_list()
        sorted_list=sorted(expense_list,key=lambda x:x[1], reverse=True)
        show_rank(sorted_list)
    elif ch==7:
        expense_list=exp_list()
        save_data(expense_list)
    elif ch==8:
        load_data()
                     








                     
    
