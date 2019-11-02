import java.util.*;
public class TornToPieces {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		Graph graph = new Graph(n, scan);



	}
}

class Graph {
	private Map<Vertex, List<Vertex>> adjVertices;
	public Graph(int n, Scanner s) {
		adjVertices = new HashMap<>();
		for (int i = 0; i < n; i++) {
			String[] line = s.nextLine().split(" ");
			adjVertices.putIfAbsent(new Vertex(line[0]), new ArrayList<>());
			for (int j = 1; j < line.length; j++) {
			adjVertices.putIfAbsent(new Vertex(line[i]), new ArrayList<>());
			adjVertices.get(line[0]).add(new Vertex(line[i]));
			adjVertices.get(line[i]).add(new Vertex(line[0]));
			}
		}
	}
}
class  Vertex {
	String label;
	Vertex(String label) {
		this.label = label;
	}
}
class BFS {
	private Map<String, String> backTrack;
	private String goal;
	public BFS() {
		goal = null;
		backTrack = new HashMap<>();
	}
	
	void search(Graph g, String start, String finish) {
		Deque<Vertex> q = new ArrayDeque<Vertex>();
		Set<Vertex> visited = new HashSet<>();
		q.addLast(new Vertex(start));
		while (!q.isEmpty()) {
			Vertex
		}


	}



}

	