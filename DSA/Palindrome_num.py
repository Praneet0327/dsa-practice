x = 121
og = x

rev = 0
while og!=0:
    if og < 0:
        break
    dig = og%10
    rev = rev*10 + dig
    og = og//10

if x == rev:
        print(True)
else:
        print(False)
        
