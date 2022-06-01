print("WELCOME TO REGISTER AND LOGIN PORTAL")
welcome = input("Do you have an account YES/NO: ")

if welcome == "no":
    while True:
        print("please enter your details to register")
        username1 = input("ENTER A NEW USERNAME HERE: ")
        password1 = input("ENTER A NEW PASSWORD HERE: ")
        password2 = input("CONFIRM PASSWORD: ")

        if password1 == password2:
            file = open(username1 + ".txt", "w")
            file.write(username1 + "," + password2)
            file.close()
            print("SUCCESSFUL")
        else:
            print("password does not match")
            break

if welcome == "yes":
    while True:
        print("please enter your username")

        username1 = input("USERNAME: ")
        print("enter your password")
        password2 = input("PASSWORD: ")
        file = open(username1 + ".txt", "r")
        data = file.readline()
        file.close()
        if data == username1 + "," + password2:
            print("welcome", username1)
            break
        else:
            print("invalid password")
            break



