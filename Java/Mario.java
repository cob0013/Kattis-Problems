import java.util.*;
public class Mario {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] line = scan.nextLine().split(" ");
		int n = Integer.parseInt(line[0]);
		int num = Integer.parseInt(line[1]);
		HashSet<Integer> set = new HashSet<Integer>();
		for (int i = 0; i < num; i++) {
			set.add(Integer.parseInt(scan.nextLine()));
		}
		for (int i = 0; i < n; i++) {
			if (!set.contains(i)) {
				System.out.println(i);
			}
		}
		System.out.println("Mario got " + set.size() +  " of the dangerous obstacles.");

	}
}