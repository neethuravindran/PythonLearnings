import re
def validatePwd(password):
    flag = 0
    while True:
        if len(password) <= 6:
            flag = -1
            break
        elif len(password) >= 12:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[$#@]", password):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            break

    if flag == -1:
        print("Not a Valid Password ")


def get_user_query():
    return input("Enter Password:  ")


if __name__ == "__main__":
    user_query = get_user_query()
    validatePwd(str(user_query))
