a=int(input('count no of length: '))
i=a+1
while i>1:
  i-=1
  s=a-i
  if i==1:
    print(" "*s+'*')
  else:
    print(" "*s+'*'+"-"*(i-2)+"*")