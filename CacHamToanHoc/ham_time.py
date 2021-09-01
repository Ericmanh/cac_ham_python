# Hàm time gồm clock và time 
from time import clock
print("enter your name:", end="")
start_time =clock()
name  = input()
print("nhập name")
elapsed = clock() - start_time
print(name, "it took you", elapsed ,"second to repond")
