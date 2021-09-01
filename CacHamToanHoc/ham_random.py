# Random là một trong những hàm lấy số ngẫu nhiên
# randrange (x,y) --> lấy số ngẫu nhiên >=x và <y
from random import randrange
count =0

while True:
    x= randrange (-100,100)
    count +=1
    print(x,end=",")
    if x==50:
        break

print("\n ơ lần ngẫu nhiên thư",count)
print("Bye!")