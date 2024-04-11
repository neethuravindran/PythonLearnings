#Write a program, which will find all the numbers between 1000 and 3000 (both 
#included) such that each digit of a number is an even number. The numbers 
#obtained should be printed in a comma separated sequence on a single line



items = []
for i in range(1000, 3000):

    s = str(i)

    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0 and (int(s[3]) % 2 == 0)):
        items.append(s)

print(",".join(items))
