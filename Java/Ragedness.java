import java.util.*;
public class Ragedness {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int max = 0;
		int output = 0;
		int[] arr = new int[101];
		int count = 0;
		String line = "";

		while (scan.hasNext()){
			line = scan.nextLine();
			int length = line.length();
			if (length > max) {
				max = length;
			}
			arr[count] = length;
			count++; 
		}
		for (int i = 0; i < count - 1; i++) {
			if (arr[i] != 0) {
				output += Math.pow(max - arr[i], 2);
			}
		}
		System.out.println(output);
	}
}