v1=float(input())
v2=float(input())
v3=float(input())
r=0.001
p=0.1
s=2
prom=(v1+v2+v3)/3
print('\nEl promedio es ',prom,'\n')
e1=v1*p/100 + r*s
e2=v2*p/100 + r*s
e3=v3*p/100 + r*s
e12=pow(e1,2)
e22=pow(e2,2)
e32=pow(e3,2)
et=pow(e12+e22+e32,0.5)
print('El valor del error del promedio es ',et)