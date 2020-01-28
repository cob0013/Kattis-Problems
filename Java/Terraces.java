import java.util.*;
public class Terraces {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int c = scan.nextInt();
      int r = scan.nextInt();
      int[][] grid = new int[r][c];
      boolean[][] visited = new boolean[r][c];
      for (int i = 0; i < r; i++) {
         for (int j = 0; j < c; j++) {
            grid[i][j] = scan.nextInt();
         }
      }
      int total = 0;
      for (int i = 0; i < r; i++) {
         for (int j = 0; j < c; j++) {
            GardenCell cell = new GardenCell(i, j);
            boolean check = false;
            int count = 0;
            if (!visited[i][j]) {
      Deque<GardenCell> q = new ArrayDeque<GardenCell>();
               q.addLast(cell);
               while (!q.isEmpty()) {
                  count++;
                  GardenCell curr = q.removeFirst();
                     visited[curr.r][curr.c] = true;
                     for (GardenCell p : curr.getNeigbors()) {
                        if (isInBounds(p.r, p.c, r, c) && !visited[p.r][p.c] && grid[p.r][p.c] == grid[curr.r][curr.c]) {
                           q.addLast(p);
                           visited[p.r][p.c] = true;
                        }
                        if  (isInBounds(p.r, p.c, r, c)  && grid[p.r][p.c] < grid[curr.r][curr.c]) {
                           check = true;
                        }
                     }
                  }
               
               if (!check) {
                  total += count;
               }
            }
         }
      }
      System.out.println(total);
   }
   public static boolean isInBounds(int i, int j, int rMax, int cMax) {
      return (i >= 0 && j >= 0 && i < rMax && j < cMax);
   }
}
class GardenCell {
   int r;
   int c;
   public GardenCell(int i, int j) {
      r = i;
      c = j;
   }
   public ArrayList<GardenCell> getNeigbors() {
      ArrayList<GardenCell> neighbors = new ArrayList<>();
      neighbors.add(new GardenCell(this.r + 1, this.c));
      neighbors.add(new GardenCell(this.r - 1, this.c));
      neighbors.add(new GardenCell(this.r, this.c + 1));
      neighbors.add(new GardenCell(this.r, this.c - 1));
      return neighbors;
   }
}