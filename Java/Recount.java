import java.util.*;
public class Recount {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		while (scan.hasNext()) {

			String name = scan.nextLine();
			if (name.equals("***")) break;
			if (!map.containsKey(name)) {
				map.put(name, 1);
			}
			else  {
				map.put(name, map.get(name) + 1);
			}
		}
		int max = 0;
		String maxName = "";
		for (String key : map.keySet()) {
			if (map.get(key) > max) {
				max = map.get(key);
				maxName = key;
			}

		}
		int maxCount = 0;
		for (String key : map.keySet()) {
			if (map.get(key) == max) {
				maxCount++;
				if (maxCount > 1) break;
			}
		}
		if (maxCount > 1) {
			System.out.println("Runoff!");
		}
		else {
			System.out.println(maxName);
		}

	}

}