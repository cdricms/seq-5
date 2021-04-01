## 7
even = [x*2 for x in range(10)]
print(even)

## 8
odd = [x*2+1 for x in range(10)]
print(odd)

## 9
mul_7 = [x for x in range(20) if x % 7 == 0]
print(mul_7)


## 10 
mul_7 = [x for x in range(20) if x % 7 == 0 and x != 0]
print(mul_7)


## 11
s = [f"{x} * 7 = {x * 7}" for x in range(11)]
print(s)

## 12
nsi = ["NSI" for _ in range(20)]
print(nsi)


from random import randint
## 13
r = [randint(-10, 10) for _ in range(10)]

print(r)


from random import random
## 14
rf = [round(random(), 2) for _ in range(10)]
print(rf)


## 15
tempCelsius = [17.5, 19.2, 21, 20.3, 19.7]
converted = [round(x + 273.15, 2) for x in tempCelsius]
print(converted)


time_sec = (25, 78, 47, 228, 161)
## 16
conv_min = [round(x / 60, 2) for x in time_sec]
print(conv_min)


## 17
conv_min = [int(x / 60) for x in time_sec]
print(conv_min)

## 18
rem_sec = [int(str(round(x / 60, 2)).split(".")[1]) for x in time_sec]
print(rem_sec)

## 19

formated = [str(round(x / 60, 2)).replace(".", ":") for x in time_sec]
print(formated)


## 20
w = {"Fruit1" : "Pear", "Fruit2" : "Apple", "Fruit3" : "Banana"}
low = [x.lower() for x in w.values()]
print(low)


## 21
lt_eq_8 = [x for x in range(20) if x <= 8]
print(lt_eq_8)


## 22
lt_7_gt_15 = [x for x in range(20) if x < 7 or x > 15]
print(lt_7_gt_15)


## 23
even_50_70 = [x for x in range(50, 70) if x % 2 == 0 and x != 70]
print(even_50_70)


## 24
mult_7 = [x for x in range(141) if x % 7 == 0]
print(mult_7)

## 25
s = [f"{x} * 7 = {x * 7}" for x in range(141)]
print(s)


marks = (16, 17, 12.5, 14.5, 19, 15)
## 26
gt_15 = [x for x in marks if x > 15]
print(gt_15)


## 27
gt_15_lt_17 = [x for x in marks if x >= 15 and x <= 17]
print(gt_15_lt_17)

fruits = ('apple', 'pear', 'banana', 'ananas', 'raspberry', 'orange')
## 28
gt_5 = [x for x in fruits if len(x) <= 5]
print(gt_5)


## 29
starts_w_a = [x for x in fruits if x[0] == 'a']
print(starts_w_a)



