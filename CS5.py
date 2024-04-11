# Design a code which will find the given number is Palindrome number or not.

num=int(input("Enter a number:"))
strng=str(input("Enter a string:"))

temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("The number is not palindrome!")


def isPalindrome(s):
    return s == s[::-1]


ans = isPalindrome(strng)

if ans:
    print("The string is palindrome!")
else:
    print("The string is not palindrome!")


