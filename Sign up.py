
print("\n")

print("Hello Sir in this Program you can make your Proflie\n")
print("Press '1' for Sign up \nPress '2' for log in")
com1=int(input())

if com1 == 1:
    username=str(input("Enter your Username\n"))
    password=int(input("Enter your Password (Num)\n"))
    name=str(input("Enter your First Name\n"))
    lname=str(input("Enter your Last Name\n"))
    age=int(input("Enter your Age\n"))
    phone=int(input("Enter your Phone number\n"))
    gmail=str(input("Enter you Email id\n"))
    private="..."
    print("\nYou are Successfully Sign-up\n")
    
    data = open(f"{username}.txt",'w')
    save = data.write(str(username))
    data.close()


    data = open(f"{username}.txt",'a')
    save = data.write(str(f"\n{password}"))
    data.close()


    data = open(f"{username}.txt",'a')
    save = data.write(str(f"\n{name} "))
    data.close()

    data = open(f"{username}.txt",'a')
    save = data.write(str(f"{lname}"))
    data.close()

    data = open(f"{username}.txt",'a')
    save = data.write(str(f"\n{age}"))
    data.close()
    
    data = open(f"{username}.txt",'a')
    save = data.write(str(f"\n{phone}"))
    data.close()

    data = open(f"{username}.txt",'a')
    save = data.write(str(f"\n{gmail}"))
    data.close()


    data = open(f"{username}.txt",'a')
    save = data.write(str(f"\n{private}"))
    data.close()





if com1 == 2:
    data = open('file1.txt','r')
    line1 = data.readline()
    line2 = data.readline()
    line3 = data.readline()
    data.close()
    
    un = str(input("Enter you Username\n"))
    pword = int(input("Enter your Password\n"))
    if un in line1:
        if str(pword) in str(line2):
            print(f"\nYour most Welcome in This Program {line3}\n")
        else:
            print("\nYour Password is Incorrect\n")
            
    else:
        print("\nYour Username is invalid, Please first sign-up\n")
        
    



print("\n")
