import java.util.*;
public class TheOwlAndTheFox {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = Integer.parseInt(scan.nextLine());
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(scan.nextLine());
			int oneLess = sum(num) - 1;
			for (int k = num; k >= 0; k--) {
				if (sum(k) == oneLess) {
					System.out.println(k);
					break;
				}
			}

		}
	}
	static int sum(int n) {
		int sum = 0;
		while (n > 0) {
			sum += n % 10;
			n /= 10;
		}
		return sum;
	}

}