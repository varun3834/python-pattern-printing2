a=int(input('count no of length: '))
i=1
while i<=a:
  s=(a-i)*2
  if(a==i):
      print('*'+"-"*(i-2)+'*'+"-"*(i-2)+'*')
  else:
       if i==1:
          print('*'+" "*(s-1)+'*')
       else:
          print("*"+'-'*(i-2)+"*"+" "*(s-1)+"*"+'-'*(i-2)+"*")
          
          

  i+=1
i=a
while i>1:
  i-=1
  s=(a-i)*2
  if i==1:
     print('*'+" "*(s-1)+'*')  
  else:
      print("*"+'-'*(i-2)+"*"+" "*(s-1)+"*"+'-'*(i-2)+"*")