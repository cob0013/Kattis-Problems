import java.util.*;
public class ReversedBinary {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		String binary = Integer.toBinaryString(n);
		StringBuilder sb = new StringBuilder();
		for (int i = binary.length() - 1; i >= 0; i--) {
			sb.append(binary.charAt(i));
		}
		System.out.println(Integer.parseInt(sb.toString(), 2));

	}
	}