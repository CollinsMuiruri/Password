import random
from info import Credentials

def create_credentials(fname,lname,phone,email):
    '''
    Create new User
    '''
    new_user = Credentials(fname,lname,phone,email)
    return new_user

def save_credentials(credentials):
    '''
    saves credentials
    '''
    credentials.save_credentials()

def display_credentials():
    '''
    displays user Credentials
    '''
    return Credentials.display_credentials()

def main():
    print('''Welcome to password where you can save your credentials and retrieve them later.
    Please input your name''')

    user_name = input()

    print(f"Hello {user_name}.")
    print('\n')

    while True:
        print('''
        This will help you move around:
        new - creating a new account,
        display - viewing your contacts,
        generate - generating a new password for you,
        exit - exiting the app''')
        initials = input().lower()

        if initials =='new':
            print("Sign up")
            print("-"*10)

            print("Enter your first name")
            f_name = input()

            print("Enter your last name")
            l_name = input()


            print("Input your phone number")
            p_number = int(input())

            print("Enter your email address")
            e_address = input()

            save_credentials(create_credentials(f_name,l_name,p_number,e_address))

            print ('\n')
            print(f"New Account {f_name}{l_name} is saved")


        elif initials == 'display':

            if display_credentials():
                print("Here are your up-to-date credentials.")
                print('\n')
                for credentials in display_credentials():
                    print(f"{credentials.first_name} {credentials.last_name}...{credentials.number}")
                    print('\n')
                else:
                    print('\n')
                    print("No more accounts")
                    print ('\n')

        elif initials == 'generate':

                choices = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ?()@#$%^&*!"
                length = len(choices)
                print("Give the preferred length to your password")
                lent = int(input())
                password = "".join(random.sample(choices,lent ))
                print ('\n')

                print(password)

        elif initials == 'exit':

                print("Goodbye, see you soon")
                break

        else:
                print("Please use the given commands to navigate")

if __name__ == '__main__':
    main()
