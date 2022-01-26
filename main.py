import math
mala=int(input("Ievadi kvadrāta malas garumu cm (lielāku par 5): "))
laukums=math.pow(mala,2)
print(laukums)
mala2=mala+5
laukums2=math.pow(mala2,2)
print(laukums2)
procenti=laukums/100
atbilde=laukums2/procenti-100
print(round(atbilde))