import java.util.*;
public class AlphabetSpam {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		char[] line = scan.nextLine().toCharArray();
		double total = line.length;
		double white = 0;
		double lowerCase = 0;
		double upperCase = 0;
		double symbol = 0;
		for (int i = 0; i < line.length; i++) {
			if (line[i] == '_') white++;
			else if (Character.isLowerCase(line[i])) lowerCase++;
			else if (Character.isUpperCase(line[i])) upperCase++;
			else symbol++;
		}
		System.out.println(white / total);
		System.out.println(lowerCase / total);
		System.out.println(upperCase / total);
		System.out.println(symbol / total);

	}
}