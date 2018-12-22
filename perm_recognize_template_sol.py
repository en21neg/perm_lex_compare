n = int(input())

f=str(input())
#f = list( map( int, input().strip().split() ) )
assert len(f) == n

def is_perm(f):
    
    for i in range (n):  #no ripetizioni
        x=0
        for j in range (n):
            if f[i]==f[j]:
                x+=1
            if x>1:
                return False
            
    for k in range (n):
       if f[k]>=(str(n)):
            return False  

    return True

print( is_perm(f) )

