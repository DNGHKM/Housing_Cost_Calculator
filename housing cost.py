print("행복주택 주거비 계산기입니다. by.동하")
print("--------------------------")
print()
while True:
    import math
    deposit=float(input("보증금을 입력하세요(억원, 소수 가능)"))
    deposit=deposit*100000000

    rent=float(input("월세를 입력하세요(만원, 소수 가능)"))
    rent=rent*10000

    if deposit>400000000:
        interest_loan=deposit*0.04
        interest_cash=0
    elif 375000000<deposit<=400000000:
        interest_loan=300000000*0.0165
        interest_cash=(deposit-300000000)*0.04
    else :
        interest_loan=deposit*0.8*0.0165
        interest_cash=deposit*0.2*0.04

    housingcost=interest_loan/12+interest_cash/12
    print()
    print("-------------------------------------------")
    print("월 주거비는""["+str(format(math.floor(rent+housingcost),','))+"]""만원 이며,")
    print("관리비를 포함한 금액(예상)은""["+str(format(math.floor(rent+housingcost+200000),','))+"]""만원 입니다.")
    print("-------------------------------------------")
    print()