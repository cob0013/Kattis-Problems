import java.util.*;
public class AnthonyAndDiablo {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		double area = Double.parseDouble(scan.next());
		double perimeter = Double.parseDouble(scan.next());
		double cal =  Math.pow(perimeter, 2)  / (4 * Math.PI);
		if (area < cal) {
			System.out.println("Diablo is happy!");
		}
		else {
			System.out.println("Need more materials!");
		}

	}
}