def validateStr(Str):
    lower = 0
    upper = 0
    for i in Str:
        if i.islower() and i.isalpha():
            lower += 1
        elif i.upper() and i.isalpha():
            upper += 1
    print("The number of lowercase characters is:", lower)
    print("The number of uppercase characters is:", upper)


def get_user_query():
    return input("Enter string:  ")


if __name__ == "__main__":
    user_query = get_user_query()
    validateStr(str(user_query))
