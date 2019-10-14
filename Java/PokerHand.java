import java.util.*;
public class PokerHand {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int[] count = new int[128];
		String[] line = scan.nextLine().split(" ");
		for (String s: line) {
			count[s.charAt(0)]++;
		}
		int max = count[0];
		for (int i : count)
			max = Math.max(max, i);
		System.out.println(max);
	}

}