import time
print("#######|WELCOME TO U.S BANK!|########")
print("""
PLEASE INSERT YOUR CARD""")
time.sleep(2)
print("""
ATM HAVE READ YOUR CARD!! PLEASE WAIT
""")
time.sleep(2)
print("""=============+++++++++++++++++++==================
===============+++++++++++++===================
===============++++++++++++====================""")
print("HELLO MR.john WELCOME TO U.S BANK ATM")

#  PASSWORD OF ATM MACHINE IS BELOW (1234)

pin =1234
chance=3

#  ASSUME THAT MR. JOHN ACCOUNT HAVE 5000 BALANCE AND BALANCE IS LESS THAN =TO 2000. THE BANK SHOW ACCOUNT HAVE LOW BALANCE******************

balance=5000

while chance !=0:
    user_pin = int(input("""
Please enter the four digit PIN: """))
    if user_pin!=pin:
        chance=chance-1
        print("Wrong pin number")
        print(f"you have {chance} chance left")
        if chance == 0:
            print("""#########################
#############################""")
            print("YOU HAVE TRY SO MANY ATTEMPT")
            break
    else:
        print("""
                    1 == BALANCE
                    2 == DEPOSITE
                    3 == WITHDRAW
                    4 == EXIT
        """)

        choice= int(input("PLEASE SELECT A OPTION: "))
        if choice==1:
            print("YOUR CURRENT BALANCE IS: ",balance)
        if choice==2:
            deposite=int(input("PLEASE ENTER AMOUNT TO DEPOSITE: "))
            print(f"YOUR CURRENT BALANCE IS: {balance+deposite}")
        if choice==3:
            withdraw=int(input("PLEASE ENTER AMOUNT TO WITHDRAW: "))
            if withdraw>balance:
                print("INSUFFICIENT BALANCE!!")
            else:    
                balance=balance-withdraw
                if balance<=2000:
                    print(f"YOUR CURRENT BALANCE IS: {balance}")
                    print(f"YOUR ACCOUNT HAVE LOW BALANCE PLEASE MAKE SUFFICIENT BALANCE GREATER THAN 2000")

                else:
                    print(f"YOUR CURRENT BALANCE IS: {balance}")
        if choice==4:
            print("""
            
        ***********THANK YOU FOR USING U.S BANK ATM***********
            
            """)
            break
        if choice>4:
            print("///////PLEASE ENTER A VALID OPTION///////")
    print("""=============================================================================================
====================================================================================================
=======================================================================================================""")
    user_exit=input("WOULD YOU LIKE TO EXIXT? YES/NO:--")
    if user_exit=="YES" or user_exit=="yes":
        print("""

        **************THANK YOU FOR USING U.S BANK ATM************

                  """)
        break

    else:
        continue



#         ******************************************ATM MACHINE PROJECT COMPLETED AND THIS PROJECT IS MADE BY UJJAWAL SHARMA****************************************************


