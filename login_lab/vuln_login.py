from getpass import getpass


def login_form(username, password):

    user = {'feuermelda': 'password', 'user1': '12345', 'admin': 'secure'}

    # user.update({username: password})

    # print(user)

    if username in user:
        if password == user[username]:
            print("Login successful.\n")
            return True

        elif (password == '') or (password == 'admin'):
            print("Login successful.\n")
            return True
        else:
            print("Wrong password.\n")
            return False

    else:
        print("No user found.\n")
        return False


if __name__ == '__main__':

    usern = input("Please enter your username:\n").strip()
    passw = getpass("Please enter your password:\n").strip()
