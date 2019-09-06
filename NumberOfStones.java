import java.util.*;
public class NumberOfStones {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		if (num % 2 != 0) System.out.println("Alice");
		else System.out.println("Bob");
	}
}