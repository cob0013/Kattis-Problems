import java.util.*;

public class Qaly {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		double total = 0;
		for (int i = 0; i < n; i++) {
			double left = in.nextDouble();
			double right = in.nextDouble();
			double mult = left * right;
			total += mult;
		}

		System.out.println(total);


	}

}
