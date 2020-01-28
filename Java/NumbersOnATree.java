import java.util.*;
public class NumbersOnATree {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] line = scan.nextLine().split(" ");
		int n = Integer.parseInt(line[0]);
		double top = Math.pow(2, n + 1) - 1;
		if (line.length == 1) {
			System.out.println((int)top);
		}
		else {
		char[] arr = line[1].toCharArray();
		int debth = 0;

		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == 'L') {
				debth = (2*debth) + 1;


			}
			else {
				debth = (2 * debth) + 2;

			}
		}
		
		System.out.println((int)top - debth);
	}

	}
}