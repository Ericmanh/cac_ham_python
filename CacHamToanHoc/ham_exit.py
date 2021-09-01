# Hàm exit dùng thoát phần mềnkh
while True:
    s = input("tên ban:")
    print(s)
    hoi = input("tiếp hay không? (c/k):")
    if hoi == "k":
        exit()
print("bye!")
