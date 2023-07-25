/**
 * HousingCost
 */
import java.util.Scanner;

public class HousingCost {
    public static double interest_loan;
    public static double interest_cash;
    public static double TotalCost=Math.ceil(interest_loan/12+interest_cash/12);
    public static float rent;

    public static void main(String[] args) {
           try (Scanner in = new Scanner(System.in)) {
            System.out.println("주택 주거비 계산기입니다. by.동하");
            System.out.println("신혼부부 버팀목 전세대출 실행을 가정합니다.");
            System.out.println("--------------------------");
            System.out.println();
            
            System.out.println("신혼부부 버팀목 전세대출금리를 입력하세요(%) (1.2%~2.1%)");
            float interest_loan_rate=in.nextFloat();
            System.out.println("* 신혼부부 버팀목 전세대출금리 : "+interest_loan_rate);
            interest_loan_rate=interest_loan_rate/100;
            System.out.println();
            System.out.println("자금조달 비용을 입력하세요(%)(신용대출 금리 등)");
            float interest_cash_rate=in.nextFloat();
            System.out.println("* 자금조달 금리 : "+interest_cash_rate);
            interest_cash_rate=interest_cash_rate/100;
            System.out.println();

            System.out.println();
            System.out.println("대출금리 "+interest_loan_rate*100+"% / 자금조달비용 "+interest_cash_rate*100+"% 로 계산합니다.");

   while (true) {
            System.out.println("보증금을 입력하세요(억원, 소수 가능)");
            float deposit=in.nextFloat();
            deposit = deposit * 100000000;

            System.out.println("월세를 입력하세요(만원, 소수 가능)");
            rent=in.nextFloat();
            rent = rent*10000;

   if (deposit>400000000) {
            interest_loan = deposit*interest_cash_rate;
            interest_cash = 0;
            System.out.println("****신혼부부 버팀목 전세대출 이용이 불가합니다.****");
            Notice();

   }else if ((deposit>375000000)&&(deposit<=400000000)) {
            interest_loan = 300000000*interest_loan_rate;
            interest_cash = (deposit-300000000)*interest_cash_rate;
            Notice();

   }else{
            interest_loan=deposit*0.8*interest_loan_rate;
            interest_cash=deposit*0.2*interest_cash_rate;
            Notice();
   }
   }
        }
}
public static void Notice(){
        double TotalCost = Math.ceil(interest_loan/12+interest_cash/12);
        System.out.println("------------------------------------------");
        System.out.println("월 주거비는 "+(rent+TotalCost)+" 만원 입니다.(관리비 별도)");
        System.out.println("------------------------------------------");
}
}