

s = input("Enter the string ")
n = len(s)
d = int(input("Enter the shift"))
d = d%n
way = input("enter direction '\n'1.left'\n'2.right")

if(way=="1"):
    s = s[d:] + s[:d] # first char
else :
    s = s[(-d):] + s[:(-d)] # last char 

print(s)


    


    