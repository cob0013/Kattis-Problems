import java.util.*;
public class CoastLength {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int R = scan.nextInt();
		int C = scan.nextInt();
		int[][] grid = new int[R + 2][C + 2];
		boolean[][] seen = new boolean[R + 2][C + 2];
		for (int i = 0; i < R; i++) {
			String line = scan.next();
			for (int j = 0; j < C; j++) {
				grid[i + 1][j + 1] = Integer.parseInt(line.substring(j, j + 1));
			}
		}
		for (int i = 0; i < grid.length; i++) {
			grid[i][C + 1] = 0;
		}
		for (int i = 0; i < grid.length; i++) {
			grid[i][0] = 0;
		}
		for (int i = 0; i < grid[0].length; i++) {
			grid[0][i] = 0;
		}
		for (int i = 0; i < grid[0].length; i++) {
			grid[R + 1][i] = 0;
		}

		Queue<Coordinates> q = new LinkedList<Coordinates>();
		int coastLines = 0;
		q.add(new Coordinates(0, 0));
		while (!q.isEmpty()) {
			Coordinates current = q.poll();
			if (seen[current.row][current.col] == false) {
				seen[current.row][current.col] = true;
				if (grid[current.row][current.col] == 0) {
					ArrayList<Coordinates> adj = Coordinates.getVerts(current);
					for (Coordinates next : adj) {
						if (isInBounds(next.row, next.col, R + 2, C  + 2)) {
							if (grid[next.row][next.col] == 0) {
								q.add(next);
							}
							else {
								coastLines++;
							}
						} 
					}

				}
			}
		}
		System.out.println(coastLines);

	}
	static boolean isInBounds(int r, int c, int rMax, int cMax) {
		if (r >= 0 && r < rMax && c >= 0 && c < cMax) return true;
		return false;
	}
}
	class Coordinates {
		int row;
		int col;
		
		 Coordinates(int rowIn, int colIn) {
			row = rowIn;
			col = colIn;
		}
		static ArrayList<Coordinates> getVerts(Coordinates in) {
			ArrayList<Coordinates> output = new ArrayList<Coordinates>();
			output.add(new Coordinates(in.row + 1, in.col));
			output.add(new Coordinates(in.row - 1, in.col));
			output.add(new Coordinates(in.row, in.col + 1));
			output.add(new Coordinates(in.row, in.col -1));
			return output;
		}
	}
