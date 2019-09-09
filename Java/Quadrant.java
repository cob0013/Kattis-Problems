import java.util.*;
public class Quadrant {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	int x = scan.nextInt();
	int y = scan.nextInt();
	boolean xPositive = x > 0;
	boolean yPositive = y > 0;
	if (xPositive && yPositive) System.out.println(1);
	 else if (xPositive) {
		  System.out.println(4).;
		}
	else if (yPositive) System.out.println(2);
	else System.out.println(3);
		}
}
