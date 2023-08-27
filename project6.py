star=int(input('count no of length: '))
counter = 0
count=range(100000)
n=-1
s=-1
while counter<star:

    if counter==0:
        print(" "*(star-counter-1)+ "*" +" "*(star-counter-1))
    elif counter/2 in count:
        n+=1
        print(" "*((star-counter+n))+ "*-" +"-"*(counter-2) + "*"+" "*(star-counter-1))
        
    else:
        print(" "*(star-counter+s)+ "*" +"-"*(counter-1) + "*"+" "*(star-counter-1))
        s+=1
    counter= counter+1

    
    # if counter<3:
    #     # print("asdfgh")
    #     pass
    # else:
    #     n=n+1