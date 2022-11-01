while True:
    print("select an option from menu")
    print("1 add employee")
    print("2 view all employee")
    print("3 search a employee")
    print("4 update the employee")
    print("5 delete a employee")
    print("6 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("employee enter selected")
    elif(choice==2):
        print("view employee selected")
    elif(choice==3):
        print("search employee selected")
    elif(choice==4):
        print("update employee selected")
    elif(choice==5):
        print("delete employee selected")
    elif(choice==6):
        break
