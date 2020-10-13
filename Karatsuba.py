def str_minus(a,b):     #时间复杂度为n
    tw = 0
    k = len(a) - 1
    outstr = ""
    for i in range(1,len(b)+1):
        if (eval(a[k]) - eval(b[len(b)-i]) - tw) < 0 :
            outstr = str(10 + eval(a[k]) - eval(b[len(b)-i]) - tw) + outstr
            tw = 1
        else:
            outstr = str(eval(a[k]) - eval(b[len(b)-i]) - tw) + outstr
            tw = 0
        k = k - 1
    j = 0
    for i in range(len(b), len(a)): #多余位数的计算。
        k = len(a) - i - 1
        if eval(a[k]) - tw < 0:
            outstr = str(10 + eval(a[k]) - tw) + outstr
            tw = 1
        else:
            outstr = str(eval(a[k]) - tw) + outstr
            tw = 0

    return outstr

def str_plus(a,b):
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            b = "0" + b
    else:
        for i in range(len(a), len(b)):
            a = "0" + a
    jw = 0
    k1 = len(a)
    k2 = len(b)
    outstr = ""

    for i in range(1,k1+1):
        if (eval(b[k2-i]) + eval(a[k1-i]) + jw < 10):
            outstr = str(eval(b[k2-i]) + eval(a[k1-i]) + jw ) + outstr
            jw = 0
        else:
            outstr = str(eval(b[k2 - i]) + eval(a[k1 - i]) + jw)[1] + outstr
            jw = 1

    if jw:
        outstr = "1" + outstr

    if len(outstr) > len(a):
        for i in range(len(outstr),2*len(a)):
            outstr = "0" + outstr
    return outstr


def kara(x,y):
    if len(x) > len(y):
        for i in range(len(y),len(x)):
            y = "0" + y
    else:
        for i in range(len(x),len(y)):
            x = "0" + x

    n = len(x)//2     #默认x，y等长。并且是2的幂级数
    a = x[0:n]
    b = x[n:]
    c = y[0:n]
    d = y[n:]
    if (len(a) != 1) and (len(b) != 1) and (len(c) != 1) and (len(d) != 1):
        result_ac = kara(a,c)
        result_bd = kara(b,d)
        o1 = kara(str_plus(a,b),str_plus(c,d))
        result_mid = str_minus(str_minus(o1,result_bd),result_ac)
        op = str_plus(str_plus(result_ac + 2*n*"0",result_mid + n*"0"),result_bd)
        return op
    else:
        op = str(100 * (eval(a) * eval(c)) + 10 * (eval(a) * eval(d) + eval(b) * eval(c)) + eval(b) * eval(d))
        if len(op) != 4:
            for i in range(4 - len(op)):
                op = "0" + op
        return op


print(kara("3141592653589793238462643383279502884197169399375105820974944592","2718281828459045235360287471352662497757247093699959574966967627"))

print(str(3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627))