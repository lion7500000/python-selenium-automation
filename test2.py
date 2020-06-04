#Array (1,21,4,11,9,10)
import copy
def arr (n):
    arr2 = copy.copy(n)
    #m = max(n)
    #result = [m]
    for idx, num in enumerate(n):
         m = max(n)
         #result = [m]
         if num == m:
            #result.append(idx)
            in1 = idx

         #print(in1)
    arr2.remove(m)

    for idx2, num in enumerate(arr2):
        m1 = max(arr2)
        #result2 = [m1]
        if num == m1 :
            in2 = idx2
            #result2.append(idx2)

    if in1 <= in2:
        return sum(n[in1:in2+2])
    else:
        return sum(n[in2:in1+1])





n= [1,35,44,11,33,10]
print (arr(n))