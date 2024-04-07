count=int(input("input:"));score=[None]*count
for i in range(0,count,1):score[i]=int(input("input num:"))
print("average:",sum(score)/len(score),"&","all num:",score)