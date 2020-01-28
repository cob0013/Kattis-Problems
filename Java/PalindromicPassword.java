import java.util.*;
public class PalindromicPassword {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		for (int i = 0; i < n; i++) {
			int number = in.nextInt();
			int j = 0;
			int result = -1;

			while (result == -1) {
				if (isPalindrome(number - j)) {
					result = number -j;
				}
				else if (isPalindrome(number + j)) {
					result = number + j;
				}
				j++;
			}
			System.out.println(result);
		}
	}
	static boolean isPalindrome(int num) {
		String s = Integer.toString(num);
		return (s.length() == 6 && s.charAt(5) == s.charAt(0) &&
			s.charAt(4) == s.charAt(1) &&
			s.charAt(3) == s.charAt(2));
	}
}

	