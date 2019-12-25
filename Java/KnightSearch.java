import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class KnightSearch {
	// python was not fast enough rewrote in java

	public static void main(String[] args) throws IOException {

		boolean found = false;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String line = br.readLine();
		String goal = "ICPCASIASG";
		for (int i = 0; i < n * n; i++) {
			if (line.charAt(i) == 'I') {
				// enter dfs
				Stack<Node> stack = new Stack<Node>();
				// int c = i / n;
				// int r = i - (c * n);
				int count = 0;
				stack.push(new Node(i, count));
				while (stack.size() != 0) {
					Node curr = stack.pop();
					int r =  curr.index / n;
					int c = curr.index - (r * n);

					 count = curr.count;
					if ((line.charAt(curr.index)) == (goal.charAt(count))){
						count += 1;
					}
					if (count == goal.length()) {
						System.out.println("YES");
						return;
					}
					ArrayList<Integer> neig = getNeighbors(r, c, n);
					for (int ne : neig) {
						int cprime = ne / n;
						int rprime = ne - (cprime * n);
						if (line.charAt(ne) == goal.charAt(count)) {
							stack.push(new Node(ne, count));
						}
					}
				}
			}
		}
		System.out.println("NO");
	} 
	static ArrayList<Integer> getNeighbors(int i, int j, int n) {
		int max = n * n;
		ArrayList<Integer> neighbors = new ArrayList<Integer>();
		int n1 = (i + 2) * n + j + 1;
		if (n1 >= 0 && n1 < max) {
			neighbors.add(n1);
		}
		int n2 = (i + 1) * n + j + 2;
		if (n2 >= 0 && n2 < max) {
			neighbors.add(n2);
		}
		int n3 = (i - 2) * n + j - 1;
		if (n3 >= 0 && n3 < max) {
			neighbors.add(n3);
		}
		int n4 = (i - 1) * n + j - 2;
		if (n4 >= 0 && n4 < max) {
			neighbors.add(n4);
		}
		int n5 = (i + 2) * n + j - 1;
		if (n5 >= 0 && n5 < max) {
			neighbors.add(n5);
		}
		int n6 = (i + 1) * n + j - 2;
		if (n6 >= 0 && n6 < max) {
			neighbors.add(n6);
		}
		int n7 = (i - 2) * n + j + 1;
		if (n7 >= 0 && n7 < max) {
			neighbors.add(n7);
		}
		int n8 = (i - 1) * n + j + 2;
		if (n8 >= 0 && n8 < max) {
			neighbors.add(n8);
		}

		return neighbors;

	}

}
	 class Node {
		int index;
		int count;
		public Node(int indexIn, int countIn) {
			index = indexIn;
			count = countIn;
		}
	}
