import java.util.*;
public class Tarifa {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int perMonth = scan.nextInt();
		int num = scan.nextInt();
		int leftOvers = (num + 1) * perMonth;
		for (int i = 0; i < num; i++) {
			leftOvers -= scan.nextInt();
		}
		System.out.println(leftOvers);

	}


}