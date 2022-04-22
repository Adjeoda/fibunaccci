n1=0
ne=1
n3=n1+n2
nth=int(input("input the nth term"))

count=0

while  count<nth:
    n1=n2
    n2=n3
    n3=n1+n2
    print(n3)
    
