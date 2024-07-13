from mainfile import main 

def login():
    count = 3
    while count != 0:
        print("||==================================================||")
        print("||             ........LOGIN FORM........           ||")      
        print("||==================================================||")
        uname = input("||      Enter the Username :   ")
        print("||--------------------------------------------------||")
        upass = input("||      Enter the Password :   ")
        print("||==================================================||")
        
        un = "Vaibhavi"
        up = "1808"
        if uname == un and upass == up:
            print("Login successfully")
            main()
            break
        elif uname != un and upass != up:
            print("Username and Password are incorrect")
        elif uname != un:
            print("Incorrect Username")
        elif upass != up:
            print("Incorrect Password")
        
        count -= 1
        if uname != un or upass != up:
            print("Remaining Attempts", count)
        if count == 0:
            print("No remaining attempts. Exiting...")

if __name__ == "__main__":
    login()