//https://open.kattis.com/problems/grid
import java.util.*;
public class Grid {
   static int[]A = {0, 0, -1, 1};
   static int[] B = {-1, 1, 0, 0};
   public static void main(String[] args) {
   
   
      Scanner scan = new Scanner(System.in);
     
      int R = scan.nextInt();
      int C = scan.nextInt();
      int grid[][] = new int[R][C];
      int dist[][] = new int[R][C];
      for (int i = 0 ; i < R; i++) {
         String line = scan.next();
         for (int j = 0; j < C; j++) {
            grid[i][j] = Integer.parseInt(line.substring(j, j + 1));
            dist[i][j] = -1;
         }
      }
   
      Queue<Coordinates> q = new LinkedList<Coordinates>();
   
      Coordinates s = new Coordinates(0, 0);
      q.add(s);
      dist[0][0] = 0;
      while (!q.isEmpty()) {
         Coordinates current = q.poll();
         int c = current.c;
         int r = current.r;  
         for (int i = 0; i < 4; i++) {
            if (isInBounds(r + grid[r][c]*A[i] , c + grid[r][c]*B[i] , R , C))
               if (dist[r + grid[r][c]*A[i]][c + grid[r][c]*B[i]] == -1)
               {
                  q.add(new Coordinates(r + grid[r][c]*A[i] , c + grid[r][c]*B[i]));
                  dist[r + grid[r][c]*A[i]][c + grid[r][c]*B[i]] = dist[r][c] + 1;
               }
         
         }
      
      }
      System.out.println(dist[R -1][C -1]);
   
   
   }
   static boolean isInBounds(int y, int x, int yMax, int xMax) {
      return (x >= 0 && x < xMax && y >= 0 && y < yMax);
   }
   

}
class Coordinates {
   int r, c;
   public Coordinates(int xIn, int yIn) {
      r = xIn;
      c = yIn;
     
   }
}
