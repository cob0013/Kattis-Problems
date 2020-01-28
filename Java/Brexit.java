import java.util.*;
public class Brexit{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String[] line = s.nextLine().split(" ");
		int numberOfCountries = Integer.parseInt(line[0]);
		int tradingPartnerships = Integer.parseInt(line[1]);
		int homeCountry = Integer.parseInt(line[2]);
		int first = Integer.parseInt(line[3]);
		Country[] list = new Country[numberOfCountries + 1];
		for (int i = 0; i < numberOfCountries + 1; i++) {
			Country country = new Country();
			list[i] = country;
		}
		for (int i = 0; i < tradingPartnerships; i++) {
			String[] input = s.nextLine().split(" ");
			int countryA = Integer.parseInt(input[0]);
			int countryB = Integer.parseInt(input[1]);
			list[countryA].incoming++;
			list[countryA].neighborsLeft++;
			list[countryA].neighbors.add(countryB);
			list[countryB].incoming++;
			list[countryB].neighborsLeft++;
			list[countryB].neighbors.add(countryA);			
		}
		list[first].left = true;
		Deque<Integer> q = new ArrayDeque<Integer>();
		for (int i : list[first].neighbors) {
			list[i].neighborsLeft--;
			q.addLast(i);	
		}
		while (!q.isEmpty()) {
			int pos = q.removeFirst();
			if (!list[pos].left) {
				if (list[pos].neighborsLeft <= list[pos].incoming / 2) {
					list[pos].left = true;
					for (int i : list[pos].neighbors) {
						list[i].neighborsLeft--;
						q.addLast(i);
					}
				}
		}
	}
	

		if (list[homeCountry].left) {
			System.out.println("leave");
		}
		else {
			System.out.println("stay");
		}


	}
}
class Country {
	boolean left;
	int incoming;
	ArrayList<Integer> neighbors;
	int neighborsLeft;
	public Country() {
		left = false;
		neighbors = new ArrayList<Integer>();
		neighborsLeft = 0;
		incoming = 0;
	}
}