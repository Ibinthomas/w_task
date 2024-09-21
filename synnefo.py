synnefo=[]
while True:
    print("""
    1. Add Employee
    2. view emp details
    3. emp updations
    4. emp schedule
    5. view schedule
    6. delete employee
    7. student management
    8. view student details
    9. update student details
    10. delete student
    11. exit
    """)
    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        id=int(input("Enter Employee ID : "))
        name = input("Enter a Name: ")
        mob_no = int(input("Enter mobile number: "))
        position = input("Enter position: ")
        salary=float(input("Enter a salary: "))
        address=input("Enter the address :")
        synnefo.append({'id':id,'name':name, 'mob':mob_no,'position':position,'salary':salary,'address':address ,})
        print("Empolyee added successfully!")

    elif choice == 2:
            
            if synnefo:
                print('_' * 85)
                print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('ID', 'Name', 'Mobile', 'Position', 'Salary','address'))
                print('_' * 85)
                for i in synnefo:
                    print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['id'], i['name'], i['mob'], i['position'], i['salary'], i['address']))
            else:
                print("Employee IS NOT FOUND")

    elif choice == 3:

        emp_id = input("Enter the Id of employee to update: ")
        for i in synnefo:
            if i['id'] == id:
                mob_no = int(input("Enter a new mobile number: "))
                salary = int(input("Enter a new salary: "))
                address= input("Enter the new address :")
                i['mob'] = mob_no
                i['salary'] = salary
                i['address']= address
                print("Employ updated successfully.")
                break 
        else:
            print("Employee ID not in the Database")
                    
    elif choice == 4:

        s_id=int(input("Enter Employee ID : "))
        s_name = input("Enter a Name: ")
        time=input("Enter the time slot: ")
        subject = input("Enter the subject: ")
        lab_no = int(input("Enter the lab_no: "))
        synnefo.append({'s_id':s_id,'s_name':s_name,'emp_time':time,'emp_subject':subject, 'emp_lab':lab_no})
        print("Empolyee schedule added successfully!")

    elif choice == 5:
            
            if synnefo:
                print('_' * 70)
                
                print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format('ID', 'Name', 'Time', 'Subjuct', 'Lab number'))
                print('_' * 70)
            for i in synnefo:
                print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format(i['s_id'], i['s_name'], i['emp_time'], i['emp_subject'], i['emp_lab']))
            else:
                print("Employee IS NOT FOUND")

    elif choice==6:

        id=int(input('Enter the id to be delete: '))
        f=0
        for i in synnefo:
            if i['id']==id:
                synnefo.remove(i)
                f=1
        if f==0:
            print('invalid id!!!')

    elif choice==7:

        std_id=int(input("Enter Student ID : "))
        std_name = input("Enter Student Name: ")
        std_mobno = int(input("Enter mobile number: "))
        cource = input("Enter Cource: ")
        fee=float(input("Enter a Fee: "))
        address=input("Enter the address :")
        synnefo.append({'std_id':std_id,'std_name':std_name, 'mob':std_mobno,'cource':cource,'std_fee':fee,'address':address ,})
        print("Empolyee added successfully!")

    elif choice == 8:
            
            if synnefo:
                print('_' * 85)
                print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('ID', 'Name', 'Mobile', 'Cource', 'Fee','address'))
                print('_' * 85)
                for i in synnefo:
                    print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['std_id'], i['std_name'], i['mob'], i['cource'], i['std_fee'], i['address']))
            else:
                print("Employee IS NOT FOUND")
        
    elif choice==9:
            
            std_id = input("Enter the Id of student to update: ")
            for i in synnefo:
                if i ['std_id']==std_id:
                    std_mobno = int(input("Enter a new mobile number: "))
                    fee = int(input("Enter a new salary: "))
                    address= input("Enter the new address :")
                    i['std_mobno'] = std_mobno
                    i['fee'] = fee
                    i['address']= address
                    print("student updated successfully.")
                    break 

    elif choice==10:
         std_id=int(input('Enter the id to be delete: '))
         f=0
         for i in synnefo:
            if i['std_id']==std_id:
                synnefo.remove(i)
                f=1
         if f==0:
            print('invalid id!!!')

    elif choice == 11:
        print("Existing .......")
        break
    else:
        print("Invalid Choice")