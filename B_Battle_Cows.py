def hitung_menang(a,k):
    menang = 0
    for ai in a:
        if ai == a[k]:
            continue
        if ai < a[k]:
            menang+=1
        else:
            break
    return menang

def solve(case):
    print("Case # : {}".format(case + 1))

    n, k = list(map(int, input().split(' ')))
    k = k - 1
    a = list(map(int, input().split(' ')))

    if len(a) == 2:
        if min(a) == a[k]:
            return 0
        else :
            return 1
    
    # Index Nilai Yang Lebih Besar Dari k 
    list_gede = [a.index(i) for i in a if i > a[k] and a.index(i) < k]

    if len(list_gede) == 0:
        if a.index(max(a)) == k:
            return n - 1
        else :
            return hitung_menang(a,k)
    else:
        hasil = []
        for n1 in list_gede:
            a[k], a[n1] = a[n1], a[k]
            cow_win = a[0]
            menang = 0
            for idx,val in enumerate(a):
                if idx == 0:
                    cow_win = val
                else:
                    if cow_win < val:
                        if val == a[n1]:
                            menang+=1
                        cow_win = val
                    else :
                        if cow_win == a[n1]:
                            menang+=1

            hasil.append(menang)
            a[k], a[n1] = a[n1], a[k]
        return max(hasil)
                

test_case = int(input())

for i in range(test_case):
    menang = solve(i)
    print(menang)
