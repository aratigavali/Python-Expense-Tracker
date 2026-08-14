#EXPENSE TRACKER : 

expenses = []  #list of all expenses in  form of dictionary 

print("welcome to expense tracker!") 

while True:
    print("=====MENU====")
    print("1.Add expense")
    print("2.view all expense")
    print("3.view total spending ")
    print("4.exit")

    choice = int(input("please enter your choice : "))

#ADD EXPENSE: 

    if(choice == 1):
        date = input("enter the date : ")
        category = input("enter the category (food,travel,shopping) : ")
        description = input("enter description : ")
        amount =float(input("enter the amount : "))

        expense = {
            "date" : date,
            "category": category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("\nexpenses added successfully !!")

#view all expenses 
    
    elif(choice == 2):
        if(len(expenses)==0):
            print("no expenses added ")
        else:
            print("=====this is your all expenses====")
            count = 1
            for eachexpenses in expenses:
                print(f"expenses number {count} -> {eachexpenses["date"]} ,{eachexpenses["category"]},{eachexpenses["description"]},{eachexpenses["amount"]} ")
                count += 1 

#view total spending             
    elif(choice == 3):
        total = 0 
        for eachexpenses in expenses :
            total = total +eachexpenses["amount"]
        print("\n total spending : " , total)

#exit 
    elif(choice == 4): 
        print("thank you for using our system")
        break

    else:
        print("invalid choise , try again ")

    

