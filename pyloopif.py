import time
my_list = [1,2,3,4,5,6,7,8,9,10]

for i in my_list:
    time.sleep(1)
    if i%2 == 0:
        print('Par')
    else:   
        print('Impar')
    print(i)