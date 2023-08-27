a=int(input('count no of length: '))
i=0
while i<a:
  i+=1
  s=a-i
  if i==1:
    print(" "*(s-1),'*'*i)
  else:
    print(" "*s+"*"+'-'*(i-2)+"*")
i=a
while i>1:
  i-=1
  s=a-i
  if i==1:
    print(" "*(s-1),'*'*i)
  else:
    print(" "*s+'*'+"-"*(i-2)+"*")