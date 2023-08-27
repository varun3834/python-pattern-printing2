a=int(input('count no of length: '))
i=0
while i<a:
  i+=1
  s=a-i
  if i==1:
    print(" "*s+'*'*i)
  else:
    print(" "*(s)+"*"+"-"*(i-2)+"*")