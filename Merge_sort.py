def ms(ls):
    n = len(ls)
    if n != 1:
        ls_1 = ms(ls[0:n // 2])
        ls_2 = ms(ls[n // 2:])
        s_ls = []
        ls_1.append(9999)
        ls_2.append(9999)
        i = 0
        j = 0
        for k in range(n):
            if ls_1[i] < ls_2[j]:
                s_ls.append(ls_1[i])
                i = i+1
            else:
                s_ls.append(ls_2[j])
                j = j+1
        return s_ls
    else:
        return ls



ls = [2,5,346,457,5,8,35,2435,7,5,86,5]
print(ms(ls))
