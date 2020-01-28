import java.util.*;
public class Platforme {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = Integer.parseInt(scan.nextLine());
		ArrayList<Platforms> platforms = new ArrayList<>();
		int total = 0;
		for (int i = 0; i < n; i++) {
			String[] line = scan.nextLine().split(" ");
			int y = Integer.parseInt(line[0]);
			int x1 = Integer.parseInt(line[1]);
			int x2 = Integer.parseInt(line[2]);
			platforms.add(new Platforms(x1, x2, y));
		}
		Collections.sort(platforms);
		int[] ground = new int[10002];
		for (Platforms p : platforms) {
			total += (p.y - ground[p.x1]) +  (p.y - ground[p.x2 - 1]);
			for (int j = p.x1; j < p.x2; j++) {
				ground[j] = p.y;
			}	
		}
		System.out.println(total);
	}
}
class Platforms implements Comparable<Platforms>{
	int x1, x2, y;
	public Platforms(int x1, int x2, int y) {
		this.x1 = x1;
		this.x2 = x2;
		this.y = y;
	}
	public int compareTo(Platforms that) {
		return this.y - that.y;
	}

}