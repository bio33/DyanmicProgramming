### 
https://www.spoj.com/problems/COINS/
###


# your code goes here
def find_max(k,storage):
  if k in storage.keys():
    return (storage[k],storage)
  else:
    storage[k] = max(k,(find_max(k//2,storage)[0]+find_max(k//3,storage)[0]+find_max(k//4,storage)[0]))
    # print(k,storage[k])
    return (storage[k],storage) 


storage = {
  0:0,
  1:1
}

val=find_max(231,storage)
print(val[0])
