print("주택 주거비 계산기입니다. by.동하")
print("신혼부부 버팀목 전세대출 실행을 가정합니다.")
print("--------------------------")
print()
RED='\033[91m'
RESET='\033[0m'
BLUE='\033[34m'
interest_loan_rate=float(input("신혼부부 버팀목 전세대출금리를 입력하세요(%) (1.2%~2.1%)"))
interest_loan_rate=interest_loan_rate/100

interest_cash_rate=float(input("자금조달 비용을 입력하세요(%)(신용대출 금리 등)"))
interest_cash_rate=interest_cash_rate/100
print()
while True:
    import math
    print(f"대출금리 {(interest_loan_rate*100):.2f}% / 자금조달 비용 {(interest_cash_rate*100):.2f}%으로 계산합니다.")

    deposit=float(input("보증금을 입력하세요(억원, 소수 가능)"))
    deposit=deposit*100000000

    rent=float(input("월세를 입력하세요(만원, 소수 가능)"))
    rent=rent*10000
    def notice() :
        housingcost=interest_loan/12+interest_cash/12
        print(BLUE+"-------------------------------------------"+RESET)
        print(BLUE+"월 주거비는""["+str(format(math.floor(rent+housingcost),','))+"]""만원 입니다.(관리비 별도)"+RESET)
        print(BLUE+"-------------------------------------------"+RESET)

    if deposit>400000000:
        print()
        interest_loan=deposit*interest_cash_rate
        interest_cash=0
        print(RED+"****신혼부부 버팀목 전세대출 이용이 불가합니다.****"+RESET)
        notice()

    elif 375000000<deposit<=400000000:
        print()
        interest_loan=300000000*interest_loan_rate
        interest_cash=(deposit-300000000)*interest_cash_rate
        notice()

    else :
        print()
        interest_loan=deposit*0.8*interest_loan_rate
        interest_cash=deposit*0.2*interest_cash_rate
        notice()

    
    print()