N = int(input("Enter len of list: ")) #Get len of lis
st = input("Enter a list: ") #Get a list of integers of length N-1

lis = []
for i in st:
  lis.append(int(i))
lis.sort()

for i in range(N):
  while lis[i]+1<lis[i+1]:
    pass
  else:
    print(lis[i+1])