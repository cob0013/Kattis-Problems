import java.util.*;
public class BirthdayBoy{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = Integer.parseInt(scan.nextLine());
		int[] days = {31,28,31,30,31,30,31,31,30,31,30,31};
		HashSet<Date> all = new HashSet<Date>();
		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < days[i]; j++) {
				all.add(new Date(i + 1, j + 1));
			}
		}

		HashSet<Date> coworkers = new HashSet<Date>();
		for (int i = 0; i < n; i++) {
			String date = scan.nextLine().split(" ")[1];
			String[] dateBroken = date.split("-");
			coworkers.add(new Date(Integer.parseInt(dateBroken[0]), Integer.parseInt(dateBroken[1])));
		}
	}
}
class Date implements Comparable<Date> {
	int m;
	int d;
	public Date(int mIn, int dIn)  {
		m = mIn;
		d = dIn;
	}
	public int compareTo(Date that) {
		if (this.m == that.m) {
			return that.d - this.d;
		}
		else {
			return that.m - this.m;
		}
	}
}