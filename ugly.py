# ugly #
n = 10
ugly = [] 
ugly.append(1)

i2 = i3 = i5 = 0
multiple_2 = ugly[i2] * 2
multiple_3 = ugly[i3] * 3
multiple_5 = ugly[i5] * 5

for i in range(1,n):
  next_ugly = min(multiple_2 ,multiple_3 ,multiple_5)
  ugly.append(next_ugly)
  # print(multiple_2,multiple_3,multiple_5)
  if next_ugly == multiple_2:
    i2 += 1
    multiple_2 = ugly[i2] * 2
  if next_ugly == multiple_3:
    i3 += 1
    multiple_3 = ugly[i3] * 3
  if next_ugly == multiple_5:
    i5 += 1
    multiple_5 = ugly[i5] * 5

print(ugly)
