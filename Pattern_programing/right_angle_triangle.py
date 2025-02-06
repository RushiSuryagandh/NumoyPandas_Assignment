'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
n=5
for i in range(5):
    for j in range(n-i-1): # print spaces
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=" ")
    print() 