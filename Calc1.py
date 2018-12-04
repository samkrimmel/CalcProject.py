#calc RRAM, LRAM, MRAM

a = float(input('Enter left bound'))
b = float(input('Enter right bound'))
n = int(input('Enter a number of subintervals'))
f = input('Enter the function')

LRAM = 0.0
RRAM = 0.0
MRAM = 0.0
TRAM = 0.0

x = a
dX = (b-a)/n

for i in range(n):
    x1 = x
    f1 = eval(f)
    LRAM = LRAM + f1*dX
    x = x+dX
    x2 = x
    f2 = eval(f)
    RRAM = RRAM + f2*dX
    TRAM = TRAM + ((f2-f1)/2)*dX
    x = (x1 +x2)/2
    fm = eval(f)
    MRAM = MRAM + fm*dX
    x = x2
    
print('LRAM =',LRAM,'RRAM =',RRAM,'MRAM =', MRAM, 'Trapezoidal Rule =', TRAM)