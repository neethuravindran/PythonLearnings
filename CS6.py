#Please write a program which accepts a string from console and print it in reverse order.


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


def get_user_query():
    return input("Enter string:  ")


if __name__ == "__main__":
    user_query = get_user_query()
    print(reverse(user_query))
