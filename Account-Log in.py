from dataclasses import replace




print("---------------------------------------------")
print("\n\nPlease First Log in to your Account")
print("---------------------------------------------\n")
print("Press '1' For Log in")
print("Press '2' For Exit")
c1 = int(input())

if c1 == 1:
    print("\nEnter you Username")
    un = str(input())
    print("Enter your Password")
    pw = str(input())

    save = open(f"{un}.txt",'r')
    username = save.readline()
    password = save.readline()
    name = save.readline()
    age = save.readline()
    phone = save.readline()
    gmail = save.readline()
    private = save.readline()
    save.close()

    if un in username:
        if pw in password:
            print(f"\nYou are Successfully Sign in {name}\n\n")
            print("Press '1' for View Your Profile")
            print("Press '2' for Edit Your Profile")
            print("Press '3' for Write your Seceret Text or Code")
            print("Press '4' for See your Seceret")
            ac = int(input())
            print("\n")

            if ac == 1:
                print("-------------------------")
                print("Your Profile is Here")
                print("-------------------------\n")
                print(f"Name : {name}")
                print(f"Age : {age}")
                print(f"Username : {username}")
                print(f"Password : ********\n")
                print(f"Phone : {phone}\n")
                print(f"Gmail : {gmail}\n")
                print("--------------------------------\n")

            elif ac == 2:
                print("---------------------")
                print("Edit your Profile\n")
                print("---------------------\n")
                print("Press '1' for Edit Phone Number\nPress '2' for Gmail\nPress '3' for Edit Name\nPress '4' for Edit Password\nPress '5' for Edit Age\n")
                ac2 = int(input())

                if ac2 == 1:
                    print("Enter your new Phone Number")
                    n_pn = int(input())
                    print("Enter your Password for Confirm")
                    n_pw = int(input())

                    if str(n_pw) in password:
                       print("\nYou are SuccessFully Changed the Phone number")
                       phone = phone.replace(str(phone),str(f"{n_pn}\n"))

                       save = open(f"{un}.txt",'w')
                       save.write(username)
                       save.write(password)
                       save.write(name)
                       save.write(age)
                       save.write(phone)
                       save.write(gmail)
                       save.write(private)
                       save.close()
                    else:
                        print("Your Password is Invalid\n")

                    
                if ac2 == 2:
                    print("Enter your new Gmail")
                    n_gm = str(input())
                    print("Enter your Password for Confirm")
                    n_pw = int(input())

                    if str(n_pw) in password:
                       print("\nYou are SuccessFully Changed the Gmail")
                       gmail = gmail.replace(str(gmail),str(f"{n_gm}\n"))

                       save = open(f"{un}.txt",'w')
                       save.write(username)
                       save.write(password)
                       save.write(name)
                       save.write(age)
                       save.write(phone)
                       save.write(gmail)
                       save.write(private)
                       save.close()
                    else:
                        print("Your Password is Invalid\n")
                    
                if ac2 == 3:
                    print("Enter your new Name")
                    n_nm = str(input())
                    print("Enter your Password for Confirm")
                    n_pw = int(input())

                    if str(n_pw) in password:
                       print("\nYou are SuccessFully Changed the Name")
                       name = name.replace(str(name),str(f"{n_nm}\n"))

                       save = open(f"{un}.txt",'w')
                       save.write(username)
                       save.write(password)
                       save.write(name)
                       save.write(age)
                       save.write(phone)
                       save.write(gmail)
                       save.write(private)
                       save.close()
                    else:
                        print("Your Password is Invalid\n")
                    
                if ac2 == 4:
                    print("Enter your new Password")
                    n_pw2 = int(input())
                    print("Enter your Old Password for Confirm")
                    n_pw = int(input())

                    if str(n_pw) in password:
                       print("\nYou are SuccessFully Changed the Password")
                       password = password.replace(str(password),str(f"{n_pw2}\n"))

                       save = open(f"{un}.txt",'w')
                       save.write(username)
                       save.write(password)
                       save.write(name)
                       save.write(age)
                       save.write(phone)
                       save.write(gmail)
                       save.write(private)
                       save.close()
                    else:
                        print("Your Password is Invalid\n")

                                        
                if ac2 == 5:
                    print("Enter your new Age")
                    n_ag = int(input())
                    print("Enter your Password for Confirm")
                    n_pw = int(input())

                    if str(n_pw) in password:
                       print("\nYou are SuccessFully Changed the Age")
                       age = age.replace(str(age),str(f"{n_ag}\n"))

                       save = open(f"{un}.txt",'w')
                       save.write(username)
                       save.write(password)
                       save.write(name)
                       save.write(age)
                       save.write(phone)
                       save.write(gmail)
                       save.write(private)
                       save.close()
                    else:
                        print("Your Password is Invalid\n")


            elif ac == 3:
                print("-----------------")
                print("Private Text.")
                print("-----------------\n")
                print("Enter your Text")
                new_private = str(input())
                print("\nYou are SuccessFully Saved")
                private = private.replace(str(private),str(f"{new_private}\n"))
                save = open(f"{un}.txt",'w')
                save.write(username)
                save.write(password)
                save.write(name)
                save.write(age)
                save.write(phone)
                save.write(gmail)
                save.write(private)
                save.close()
                
            

        else:
            print("\nYour Password is Wrong Please Try Again\n")
            print("Press '1' For Reset your Password")
            print("Press '2' for Exit\n")
            c2 = int(input())

            if c2 == 1:
                print("Enter your Username")
                f_un = str(input())
                print("Enter your First Name")
                f_name = str(input())
                print("Enter your Gmail")
                f_gmail = str(input())
                if f_un in username:
                    if f_name in name:
                        if f_gmail in gmail:
                            print(f"\nYour Password is {password}\n")
                        else:
                            print("\nYour Detail is Invalid Please Try Again\n")
                    else:
                        print("\nYour Detail is Invalid Please Try Again\n")
                else:
                    print("\nYour Detail is Invalid Please Try Again\n")      
    else:
       print("\nYour Username is Invalid Please Try Again\n")
       print("Press '1' if you Forget your Username")
       print("Press '2' For Exit")
       c4 = int(input())
       print("\n")
       
       if c4 == 1:
                print("Enter your First Name")
                f_fn = str(input())
                print("Enter your Age")
                f_age = str(input())
                print("Enter your Gmail")
                f_gmail = str(input())
                if f_fn in name:
                    if f_age in age:
                        if f_gmail in gmail:
                            print(f"\nYour Username is {username}\n")
                        else:
                            print("\nYour Detail is Invalid Please Try Again\n")
                    else:
                        print("\nYour Detail is Invalid Please Try Again\n")
                else:
                    print("\nYour Detail is Invalid Please Try Again\n")



print("\n\n")
