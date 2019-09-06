import java.util.Scanner;

public class Autori {

public static void main(String[] args) {
Scanner scan = new Scanner(System.in);
String input = scan.nextLine();
String output = "";

for (int i = 0; i < input.length(); i++) {
	if (Character.isUpperCase(input.charAt(i))) {
		output += input.charAt(i);
		}
	}


	System.out.println(output);
		}
}
