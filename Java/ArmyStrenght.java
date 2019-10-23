import java.util.*;
public class ArmyStrenght {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		for (int i = 0; i < n; i++) {
			int ng = scan.nextInt();
			int nm = scan.nextInt();
			int [] gs = new int[ng];
			int [] ms = new int[nm];
			for (int j = 0; j < ng; j++) {
				gs[j] = scan.nextInt();
			}
			for (int j = 0; j < nm; j++) {
				ms[j] = scan.nextInt();
			}
		Arrays.sort(gs);
		Arrays.sort(ms);
		if (gs[gs.length - 1] >= ms[ms.length - 1]) {
			System.out.println("Godzilla");
		}
		else {
			System.out.println("MechaGodzilla");
		}
	}
}
}