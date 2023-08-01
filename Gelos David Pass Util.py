import time
import string
import random

#
# Function for logging in
def Login():
    # Adding loop incase details are incorrect
    loop = 0
    while loop < 1:
        # Asking for UserName and Password from User
        print("Enter Login Details Below")
        time.sleep(1)
        Username = input("Username:")
        Password = input("Password:")
        # Confirming with user that above details are correct
        print("Confirm details below (Y/N)")
        ConfirmDetailsYN = input("(Username): " + Username + "  (Password): " + Password + "\n")
        ConfirmDetailsYNlower = ConfirmDetailsYN.lower()
        ConfirmDetailstxt = ("(Username): " + Username + "  (Password): " + Password)
        print(ConfirmDetailstxt)
        # Filtering if input is Y or N
        if ConfirmDetailsYNlower == "y":
            print("Verifying Details")
            # Verifying if Username and Password is listed in File
            with open("UserDetails.txt", "r") as Detailstxt:
                DetailstxtContents = Detailstxt.read()
                # If in File run function options (giving access to rest of code)
                if ConfirmDetailstxt in DetailstxtContents:
                    print("Details Valid\n")
                    # Grants access to rest of code by running options function.
                    Options()
                else:
                    # If Username is not in file continue loop
                    print("Incorrect Details")
                    time.sleep(1)


        # User denies details are correct and continues loop
        if ConfirmDetailsYNlower == "n":
            print("Reenter details")
            time.sleep(1)
# Options function
def Options():
    # loop so user can do multiple things with our restarting code
    loop = 0
    while loop < 1:
        # Showing all options to user
        print("a: Show all login info: ")
        print("b: Create new user: ")
        print("x: Exit: ")

        # Input from Options
        Menu_Selection_Option = input("Enter your selection : ")
        Menu_Selection_UserSelect = Menu_Selection_Option.lower()
        # If options input is "a" or "show all login info"
        if Menu_Selection_UserSelect == "show all login info" or Menu_Selection_UserSelect == "a":
            # Opens file and print contents to screen
            print("\nShowing all login info")
            with open("UserDetails.txt", "r") as UserDetails:
                UserDetailsContents = UserDetails.read()
                print(UserDetailsContents)
                time.sleep(2)
                # If options input is "b" or "create new user"
        elif Menu_Selection_UserSelect == "create new user" or Menu_Selection_UserSelect == "b":
            # local loop for Creating new user
            Menu_Selection_UserSelectLoop = 0
            while Menu_Selection_UserSelectLoop < 1:
                print("\nCreate new user selected")
                # Asking User for desired Username for new account
                Create_Username = input("Please input a Username:")
                # Asking User if they want to create or generate password for new account
                print("Choose from the following options below:")

                Option_Select_PasswordMake = input("\na: input your own Password" + "\nb: Generate a password" + "\n:")
                PasswordMake_UserSelected = Option_Select_PasswordMake.lower()
                # if user inputs "a" or "input you own password"
                if PasswordMake_UserSelected == "a" or PasswordMake_UserSelected == "input your own password":
                    # local loop for password making
                    Password_Accepted = 0
                    while Password_Accepted < 1:
                        Menu_Selection_UserSelectLoop += 1
                        # Asking user to enter password twice
                        PasswordMake_OwnPassword1 = input("Input Password:")
                        PasswordMake_OwnPassword2 = input("Re-Enter Password")
                        # if password was entered twice correctly
                        if PasswordMake_OwnPassword1 == PasswordMake_OwnPassword2:
                            PasswordAcceptedtxt = PasswordMake_OwnPassword1
                            print("Password has been accepted")
                            Password_Accepted += 1
                            with open("UserDetails.txt", "a") as UserDetails:
                                UserDetails.write("(Username): " + Create_Username + "  (Password): " + PasswordAcceptedtxt + "\n")
                                UserDetails.close()
                                print("User details added\n")
                        # if password was entered twice incorrectly
                        if PasswordMake_OwnPassword1 != PasswordMake_OwnPassword2:
                            print("Error: Password doesn't Match\n")
                            print("Re-Enter Password")
                            time.sleep(0.5)
                # If user inputs "b" or "generate a password"
                elif PasswordMake_UserSelected == "b" or PasswordMake_UserSelected == "generate a password":
                    # Local loop for Generating password
                    Genloop = 0
                    while Genloop < 1:
                        # Asking User for desired length of password
                        GenPassword_Len = int(input("Desired Generated Password Length: "))
                        # allow password if in certain range
                        if 0 < GenPassword_Len < 80:
                            Genloop += 1
                            # getting strings library for all characters and putting them into variables
                            GenPassword_Low = string.ascii_lowercase
                            GenPassword_Up = string.ascii_uppercase
                            GenPassword_Num = string.digits
                            GenPassword_SS = string.punctuation
                            # Putting all characters into a single variable
                            GenPass_list = (GenPassword_Low + GenPassword_Up + GenPassword_Num + GenPassword_SS)
                            # Randomly making a password from "GenPass_list"
                            Final_GenPassword = "".join(random.sample(GenPass_list, GenPassword_Len))
                            print(Final_GenPassword)
                            # Confirming Generated password with user
                            print("Confirm Username and Password" + "  (Y/N)")
                            time.sleep(0.5)
                            Confirm_UserDetails = input("(Username): " + Create_Username + "  (Password): " + Final_GenPassword + "\n")
                            txtdetails = ("(Username): " + Create_Username + "  (Password): " + Final_GenPassword + "\n")
                            Confirm_UserDetailsL = Confirm_UserDetails.lower()
                            # If User Confirms password (inputs y)
                            if Confirm_UserDetailsL == "y":
                                # Adding Username and generated password to File
                                print("User Details adding")
                                with open("UserDetails.txt", "a") as UserDetails:
                                    UserDetails.write(txtdetails)
                                    UserDetails.close()
                                    print("User details added")
                                    Menu_Selection_UserSelectLoop = 1
                            # User Denies Generated password (Continues loop)
                            if Confirm_UserDetailsL == "n":
                                print("User Details Denied")
                        # Length User inputted is outside range
                        else:
                            print("Invalid Number Choose Number Between 0-80")
        # User inputs x or "exit" (Exiting Program)
        elif Menu_Selection_UserSelect == "exit" or Menu_Selection_UserSelect == "x":
            print("\nExiting program!")
            # waits 2 seconds until terminating program
            time.sleep(2)
            # Terminates program
            exit()

# Runs Login Function
Options()