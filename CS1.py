#Write a program which will find factors of given number and find whether the 
#factor is even or odd

def factornumber(num):     
    cumm = []  
    for i in range(1, num+1):
        if num % i == 0: 
            cumm.append(i) 
 
    for j in cumm:        
        if j % 2 ==0: 
            print(str(j) + ": Even") 
        else: 
            print(str(j) + ": Odd") 
            
 
def get_user_query():
    return input("Enter number:  ")

    
if __name__ == "__main__":
    user_query = get_user_query()
    factornumber(int(user_query))
    

