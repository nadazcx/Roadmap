import java.math.BigInteger;
import java.util.Scanner;

public class SumOfDigits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        BigInteger x = new BigInteger(input);
        int number = 0;

        while (input.length() > 1) {
            BigInteger newX = BigInteger.ZERO;
            for (int i = 0; i < input.length(); i++) {
                newX = newX.add(new BigInteger(String.valueOf(input.charAt(i))));
            }

            number++;
            x = newX;
            input = x.toString();
        }

        System.out.println(number);
    }
}
