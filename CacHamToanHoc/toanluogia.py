from math import *
# ép thư viện toán học

do=30
print("30",radians(do))
rad=radians(do)
print(degrees(rad))
# các bài toán lượng giác
print("mời bạn nhập vào 1 góc:")
goc = float(input())
sinx = sin(radians(goc))
cosx = cos(radians(goc))
tanx = tan(radians(goc))
cotanx =1/tanx
print("sin({0}) = {1}".format( goc, sinx))
print("cos({0})= {1}".format(goc,cosx))
print("tan ({0}) ={1}".format(goc,tanx))
print("cotan({0})={1}".format(goc, tanx))