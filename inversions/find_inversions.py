def spl_inv(ls1,ls2):
    i = 0
    j = 0
    ls = []
    num = 0
    n = len(ls1) + len(ls2) - 1
    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            ls.append(ls1[i])
            i = i + 1
        else:
            ls.append(ls2[j])
            j = j + 1
            num = num + len(ls1) - i
    if i < len(ls1):
        while i < len(ls1):
            ls.append(ls1[i])
            i = i+1
    if j < len(ls2):
        while j < len(ls2):
            ls.append(ls2[j])
            j = j+1
    return ls,num

def inv(ls):
    if len(ls) == 1:
        return ls,0
    else:
        n = len(ls)//2
        ls1 = ls[0:n]
        ls2 = ls[n:]
        n_ls1,n1 = inv(ls1)
        n_ls2,n2 = inv(ls2)
        o_ls,n3 = spl_inv(n_ls1,n_ls2)

        return o_ls,n1+n2+n3



fo = open("IntegerArray.txt","r",encoding = "utf-8")
ls = []
for line in fo.readlines():
    line = line.replace("\n","")
    ls.append(eval(line))


n = inv(ls)[1]
print(n)
