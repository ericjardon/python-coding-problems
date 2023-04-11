import java.util.Scanner;

public class CandyDivision {

        public static void main (String[] args){
            Scanner sc = new Scanner(System.in);
            int numCandy = sc.nextInt();
            System.out.print("0");
            for (int i=2; i<=numCandy;i++){
                if (numCandy%i==0)
                    System.out.print(" "+(i-1));
            }
        }
}