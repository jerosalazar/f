import os
from time import sleep

w, h = os.get_terminal_size()
f_w = 40
f_h = 4 * f_w // 5
bor = "0" * w
fir = "0" * ((w - f_w) // 2) + "1" * (f_w) + "0" * ((w - f_w) // 2)
sec = "0" * ((w - f_w) // 2) + "1" * (3 * f_w // 10) + "0" * (7 * f_w // 10) + "0" * ((w - f_w )// 2)
if len(fir) < w:
    fir += "0"
if len(sec) < w:
    sec += "0"

options = (("0", "1"), ("_", "*"), ("o", "f"), (".", "?"), ("=", " "), ("`", "$"), ("+", "@"))

f = [fir for _ in range(f_h // 10)]
f += [sec for _ in range(f_h // 5)]
f += [fir for _ in range(f_h // 10)]
f += [sec for _ in range(2 * f_h // 5)]
f = [bor for _ in range((h - f_h) // 2 + f_h // 10)] + f
f += [bor for _ in range((h - f_h) // 2 + f_h // 10)]

i = 0
while True:
    zer, one = options[i % len(options)]
    os.system("cls || clear")
    for l in f:
        sleep(0.03)
        print(l.replace("0", zer).replace("1", one))
    i += 1

# crl + c para terminar la ejecucion