def matrix(r,c,m,n,count):
    if r>m or c>n:
        return count
    if r==m and c==n:
        count+=1
        return count
    matrix(r+1,c,m,n,count)
    matrix(r,c+1,m,n,count)


r=c=0
m=n=4
count=0
print(matrix(r,c,m,n,count))