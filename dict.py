# -*- coding: utf-8 -*-

tone = (1,2,3)
ttwo = (1,[2,3]) #里面的List不可以被哈希化

d = {tone:'one','three':'threeValue'}

print(d.get('three'))
print(d.get(tone))