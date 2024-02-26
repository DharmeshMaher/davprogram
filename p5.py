hour=float(input("enter the working hours"))
price=float(input("enter the price per hour"))
if hour <= 30:
    print(hour*price)
else :
    print(30* price + (hour-30)*1.5 * price)
#50*10
#500
#50-30=20
#1.5 * 10=15
#20 *15
'''
hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 30:
 	print( h  * x)
elif h > 30:
	print(30* x + (h-30)*1.5*x)
	'''
