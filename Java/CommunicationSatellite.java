import java.util.*;
public class CommunicationSatellite {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = Integer.parseInt(scan.nextLine());
		ArrayList<Satelite> list = new ArrayList<Satelite>();
		for (int i = 0; i < n; i++) {
			String[] line = scan.nextLine().split(" ");
			double x = Double.parseDouble(line[0]);
			double y = Double.parseDouble(line[1]);
			int r = Integer.parseInt(line[2]);

			list.add(new Satelite(x, y, r));
		}
		ArrayList<Edges> weighted = new ArrayList<Edges>(n);
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < list.size(); j++) {
				double distance = list.get(i).distance(list.get(j));
				if (distance < 0) {
					distance = 0;
				}
				weighted.add(new Edges(i, j, distance));
			}
		}
		Collections.sort(weighted);
		int[] parents = new int[n];
		for (int i = 0; i < parents.length; i++) {
			parents[i] = -1;
		}
		double ans = 0;
		for (int i = 0; i < weighted.size(); i++) {
			if (Satelite.find(parents, weighted.get(i).s1) != Satelite.find(parents, weighted.get(i).s2)){
				Satelite.union(parents, weighted.get(i).s1, weighted.get(i).s2);
				ans += weighted.get(i).distance;
			}
		}
		System.out.println(ans);

	}
}

class Satelite {
	double x;
	double y;
	int r;

	public Satelite(double xIn, double yIn, int rIn) {
		x = xIn;
		y = yIn;
		r = rIn;
	}
	public double distance(Satelite that) {
		double distance =  Math.hypot(this.x - that.x, this.y - that.y);
		return distance - this.r  - that.r;
	}
	public static int find(int[] parents, int child) {
		if (parents[child] == -1) return child;
		return parents[child] = find(parents, parents[child]);
	}
	public static void union(int[] parents, int childX, int childY) {
		int parentX = find(parents, childX);
		int parentY = find(parents, childY);
		parents[parentX] = parentY;
	}
			
}
class Edges implements Comparable<Edges>{
		int s1;
		int s2;
		double distance;
		public Edges(int s1In, int s2In, double distanceIn) {
			s1 = s1In;
			s2 = s2In;
			distance = distanceIn;
		}
		public int compareTo(Edges that) {
			if (this.distance < that.distance) return -1;
			if (this.distance > that.distance) return 1;
			else {
				return 0;
			}
		}
	}
