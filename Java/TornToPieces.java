import java.util.*;
public class TornToPieces {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		HashMap<String, Set<String>> graph = new HashMap<>();
		int n = Integer.parseInt(scan.nextLine());
		//intitialize graph
		for (int i = 0; i < n; i++) {
			String[] line = scan.nextLine().split(" ");
			graph.putIfAbsent(line[0], new HashSet<>());
			for (int j = 1; j < line.length; j++) {
				graph.putIfAbsent(line[j], new HashSet<>());
				graph.get(line[0]).add(line[j]);
				graph.get(line[j]).add(line[0]);
			}
		}
		Set<String> visited = new HashSet<>();
		String[] last = scan.nextLine().split(" ");
		String start = last[0];
		String finish = last[1];
		boolean found = false;
		HashMap<String, String> backTrack = new HashMap<>();
		Deque<String> q = new ArrayDeque<>();
		q.addLast(start);
		visited.add(start);
		while (!q.isEmpty()) {
			String curr = q.removeFirst();
			if (curr.equals(finish)) {
				found = true;
				break;
			}
			Set<String> nbrs = graph.get(curr);
			if (nbrs != null) {
			for (String p : nbrs) {
				if (!visited.contains(p)) {
					q.addLast(p);
					visited.add(p);
					backTrack.put(p, curr);
				}
			}
		}
		}
		if (!found) {
			System.out.println("no route found");
		}
		else {
			Deque<String> stack = new ArrayDeque<>();
			String pointer = finish;
			String output = "";
			while (pointer != null) {
				stack.addFirst(pointer);
				pointer = backTrack.get(pointer);
			}
			while (!stack.isEmpty()) {
				output +=  stack.removeFirst() + " ";
			}
			System.out.println(output);

		}
	}
}