#please write a program which count and print the numbers of each character in a 
#string input by console.

def stroccurence(inp_str):
    print(set(inp_str))
    out = {x: inp_str.count(x) for x in set(inp_str)}
    print("Occurrence of all characters  : " + str(out))


def get_user_query():
    return input("Enter string:  ")


if __name__ == "__main__":
    user_query = get_user_query()
    stroccurence(user_query)
