data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))
print(",".join(data))