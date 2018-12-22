s=str(input())
t=str(input())

def lex_compare(s,t):
    o=len(s)
    p=len(t)
    x=0   
    for i in range (min(p,o)):
        if(s[i]!=t[i]):
            if(s[i]>t[i]):
                return 1
            else:
                return -1
        else:
            x+=1
    if(x==p and x==o):   
        return 0  
    if(x==min(p,o) and o>p):
        return 1 
    if(x==min(p,o) and o<p):
        return -1

    
print(lex_compare(s,t))
