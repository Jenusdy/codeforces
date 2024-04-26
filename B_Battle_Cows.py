def solve(case):
    n, k = list(map(int, input().split(' ')))
    k = k - 1
    a = list(map(int, input().split(' ')))
    idx_great = [a.index(i) for i in a if i > a[k] and a.index(i) < k]
    idx_great.insert(0,0)

    list_menang = []
    for i in idx_great:
        a[i], a[k] = a[k], a[i]
        idx_g = [a.index(j) for j in a if j > a[i]]
        print(a)
        print(i)

        for x in idx_g:
            print(x-i-1)

        a[i], a[k] = a[k], a[i]
    # return max(list_menang)
                
test_case = int(input())

for i in range(test_case):
    menang = solve(i)
    # print(menang)
    print("\n\n")
