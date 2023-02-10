x0 = input('x0: ')
v0 = input('v0: ')
a = input('a: ')
t= input('t: ')

print ('xf = '+(x0)+'+'+(v0)+'*'+(t)+'+0.5'+'*'+(a)+'*'+(t)+'*'+(t))
print ('xf = '+x0+'+'+v0+'*'+t+'+0.5'+'*'+a+'*'+ str(float(t)*float(t)))
print ('xf = '+x0+'+'+str(float(v0)*float(t))+'+'+ str(float(0.5)*float(a)*float(t)*float(t)))

xf= float(x0)+(float(v0)*float(t))+(0.5*float(a)*float(t)* float(t))
print ("xf = "+str(xf))
