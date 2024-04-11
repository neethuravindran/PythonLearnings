#Write a code which accepts a sequence of words as input and prints the words in a 
#sequence after sorting them alphabetically. 

def getwords(my_str):
    words = [word.lower() for word in my_str.split()]
    # sort the list
    words.sort()
    print("The sorted words are:")
    for word in words:
        print(word)


def get_user_query():
    return input("Enter sentence:  ")


if __name__ == "__main__":
    user_query = get_user_query()
    getwords(str(user_query))
