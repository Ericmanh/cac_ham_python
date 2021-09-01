# máy đoán số 1 đến 100
# chỉ đoán được 7 lần 

from random import randrange
while True:
    #số mấy là số ngẫu nhiên
    somay = randrange(1,101)
    #số lần đoán 
    solandoan=0
    win = False
    while solandoan <7:
        solandoan +=1
        songuoi =int(input("Máy đoán [1..100], mời bạn đoán:"))
        print("bạn đoán lần thứ", solandoan)
        if somay ==songuoi:
            print("chúc mừng bạn đoán đúng, số mấy là=",somay)
            win = True
            break
        if somay > songuoi:
            print("Bạn đoán sai, số mấy > số bạn")
        elif somay < songuoi:
            print("Bạn đoán sai, số mấy < số bạn")
    if win == False:
        print("Game over số máy =",somay)
    hoi=input("bạn có tiếp tục không :")
    if hoi=="k" :
        break
print("cám ơn bạn đã chơi game")