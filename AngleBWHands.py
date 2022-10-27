s=input()
h=int(s[0:2])
m=int(s[3:5])

a=abs(((h*30)+((m/60)*30))-(6*m))
b=360-a
print(min(a,b))
