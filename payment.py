#payment.py
def payment(x, info):
    d = info['deductible']
    u = info['policy_limit']
    c = info['coinsurance_rate']/100

#Logic:
#NO DEDUCTIBLE means d==0 --
#NO POLICY LIMIT means u== float('inf')
#NO COINSURANCE means α==1 ---

    # Case 1: No deductible, no limit, no coinsurance
    if d == 0  and u == float('inf') and c == 1:
        return x

    # Case 2: Deductible only
    if d!=0 and u == float('inf') and c == 1:
        if x <= d:
            return 0
        elif x>d:
            return x-d

    # Case 3: Limit only
    if d==0 and u != float('inf') and c == 1:
        if x <= u:
            return x
        elif x>u:
            return u

    # Case 4: Deductible + Limit
    if d != 0 and u != float('inf') and c == 1:
        if x <= d:
            return 0
        elif d < x < d + u:
            return x - d
        elif x >= d + u:
            return u

    # Case 5: Deductible + Coinsurance
    if d !=0 and u==float('inf') and c!=1:
        if x <= d:
            return 0
        elif x > d:
            return c*(x-d)

    # Case 6: Limit + Coinsurance
    if d==0 and u!=float('inf') and c!=1:
        if x <= u:
            return c*x
        elif x>u:
            return u

    # Case 7: Deductible + Limit + Coinsurance
    if d !=0  and u != float('inf') and c!=1:
        if x <= d:
            return 0
        elif d < x < d + u/c:
            return c * (x - d)
        elif x >= d + u/c:
            return u

    # Case 8: Coinsurance only
    if d==0 and u == float('inf') and c !=1:
        return  c*x
