a = float(input())
b = float(input())

imit= a/(b*b)
if (imit<18.5):
    print("Недостаточная масса")
elif (imit>=18.5 and imit<=25):
    print("Оптимальная масса")
elif (imit>25):
    print("Избыточная масса")
    
