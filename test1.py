def find_sub_string(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    res = 0
    lc = [[0 for k in range(l2+1)] for l in range(l1+1)]
    for i in range (l1+1):
        for j in range(l2+1):
            if (i==0 or j==0):
                lc[i][j] =0
            elif (s1[i-1] == s2[j-1]):
                lc[i][j] = lc[i][j] + 1
                res = max(res,lc[i][j])
            else:
                lc[i][j] = 0
    return res
    
s1 = input("ENTER FIRST STRING : ")
s2 = input("ENTER SECOND STRING : ")
x = find_sub_string(s1,s2)
print(x)