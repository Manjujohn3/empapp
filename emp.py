import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'employeedb')
mycursor = mydb.cursor()

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
        empcode= input("enter the code")
        empname = input("enter the name")
        designation = input("enter the value")
        salary = input("enter the salary")
        companyname = input("enter the value")
        phone = input("enter the number")
        emailid = input("enter the email")
        password = input("enter the password")
        sql = 'INSERT INTO `employees`(`empcode`, `empname`, `designation`, `salary`, `companyname`, `phone`, `emailid`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (empcode,empname,designation,salary,companyname,phone,emailid,password)
        mycursor.execute(sql , data)
        mydb.commit()
        print("value inserted succesfully") 

    elif(choice==2):
        print("view employee selected")

        sql = 'SELECT * FROM `employees`'
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i)


    elif(choice==3):
        print("search employee selected")

        empcode = input("enter the employee number: ")
        sql = 'SELECT `id`, `empname`, `designation`, `salary`, `companyname`, `phone`, `emailid`, `password` FROM `employees` WHERE `empcode` =' +empcode
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif(choice==4):
        print("update employee selected")
    elif(choice==5):
        print("delete employee selected")

        empc = input("enter the employee number: ")
        sql = 'DELETE FROM `employees` WHERE empcode='+empc
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted successfully")

    elif(choice==6):
        break
