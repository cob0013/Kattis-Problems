import java.util.*;
public class Kitten {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();	
		int n = scan.nextInt();

		String line = scan.nextLine();
		while (!line.equals("-1")) {
			String []  nums = line.split(" ");
			for (int i = 1; i < nums.length; i++) {
				m.put(Integer.parseInt(nums[i]), Integer.parseInt(nums[0]));
			}
			line = scan.nextLine();
		}
		while (m.containsKey(n)) {
			System.out.print(n + " ");
			n = m.get(n);
		}
		System.out.print(n);
	}
}



