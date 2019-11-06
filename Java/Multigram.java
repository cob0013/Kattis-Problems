import java.util.*;
public class Multigram {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String line = scan.nextLine();
		int j = 2;

		
			boolean works = true;
			String output = "-1";
			while (works) {
			if (line.length() % j != 0)	{
				works = false;
				break;
			}
			int[] count1 = new int[128];
			int[] count2 = new int[128];
			String firstHalf = line.substring(0, line.length() / 2);
			String secondHalf = line.substring(line.length() / 2, line.length());
			for (int i = 0; i < firstHalf.length(); i++) {
				count1[firstHalf.charAt(i)]++;
			}
			for (int i = 0; i < secondHalf.length(); i++) {
				count2[secondHalf.charAt(i)]++;
			}
			for (int i = 0; i < count1.length; i++) {
				if (count1[i] != count2[i]) {
					works = false;
					break;
				}
			}
			if (works) {
			line = firstHalf;
			output = firstHalf;
		}
	}
		System.out.println(output);
	}

}
