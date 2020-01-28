import java.util.*;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.Scanner; 
import java.util.StringTokenizer;public class TenKindsOfPeople {
	public static void main(String[] args) throws IOException {
		  BufferedReader scan = new BufferedReader( 
                              new InputStreamReader(System.in));
		 StringBuilder output = new StringBuilder();
		String[] line = scan.readLine().split(" ");
		int r = Integer.parseInt(line[0]);
		int c = Integer.parseInt(line[1]);
		char[][] grid = new char[r][c];
		for (int i = 0; i < r; i++) {
			String l = scan.readLine();
			for (int j = 0; j < c; j++) {
				grid[i][j] = l.charAt(j);
			}
		}
		int n = Integer.parseInt(scan.readLine());
		for (int i = 0; i < n; i++) {
			String[] points = scan.readLine().split(" ");
			Point begin = new Point(Integer.parseInt(points[0]) - 1, Integer.parseInt(points[1]) - 1);
			Point end = new Point(Integer.parseInt(points[2]) - 1, Integer.parseInt(points[3]) - 1);
			char type = grid[begin.r][begin.c];
			if(DFS(grid, begin, r, c , end)) {
				if (type == '1'){
					output.append("decimal" + "\n");
				}
				else {
					output.append("binary" + "\n");
				}

				}
				else {
					output.append("neither" + "\n");
				}
			}
			System.out.println(output);

		}

	
	public static  boolean DFS(char[][] grid, Point start, int r, int c, Point finish) {
		char type = grid[start.r][start.c];
		Deque<Point> stack = new ArrayDeque<Point>();
		boolean[][] visited = new boolean[r][c];
		stack.addFirst(start);
		while (!stack.isEmpty()) {
			Point current = stack.removeFirst();
			if (current.r == finish.r && current.c == finish.c) {
				return true;
			}
			visited[current.r][current.c] = true;
			for (Point neighbor : current.getNeighors()) {
				if (isInBounds(neighbor.r, neighbor.c, r, c) && !visited[neighbor.r][neighbor.c] &&  grid[neighbor.r][neighbor.c] == (type)) {
					stack.addFirst(neighbor);
				}
			}
		}
		return false;
	}
	static boolean isInBounds(int r, int c, int rMax, int cMax) {
		return (r >= 0 &&
		c >= 0
		&& rMax > r
		&& cMax > c);

	}

}
class Point {
	int r;
	int c;
	String type;
	public Point(int i, int j) {
		r = i;
		c = j;
	}
	public ArrayList<Point> getNeighors() {
		ArrayList<Point> output = new ArrayList<Point>();
		output.add(new Point(r + 1, c));
		output.add(new Point(r - 1, c));
		output.add(new Point(r, c + 1));
		output.add(new Point(r, c - 1));
		return output;
	}
	
}
