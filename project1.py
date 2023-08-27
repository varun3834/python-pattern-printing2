a=int(input('count no of length: '))
i=0
while i<a:
  i+=1
  if i==1:
    print("*")
  else:
    print('*'+'-'*(i-2)+"*")