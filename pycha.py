base_code = "p=a=ic=ha=1;paic=h=a;paicha=\"paic\"[ha+p*a+ic];ha=\"%\";pa=lambda icha,pa:icha%pa;ic=ha+paicha;paicha=exec;paicha("
code = 'num = int(input("enter a number... > "))\nprint(f"your number + 3 = {num + 3}")'
paicha = base_code
for ch in code:
    n = ord(ch)
    if n % 3 == 2:
        paicha += f"pa(ic,{('h+a+paic+'*round(n/3))[:-6]})+"
    elif n % 3 == 0:
        paicha += f"pa(ic,{'h+a+paic+'*round(n/3)}h-a)+"
    else:
        paicha += f"pa(ic,{"h+a+paic+"*round(n/3)}h*a)+"
paicha = paicha[:-1] + ")"
with open("paicharm.py", "w") as f:
    f.write(paicha)
