import java.util.*;

public class grasshopper {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
   
      while (true) {
         int dx[] = {-2, -1, 1, 2, -2, -1, 1, 2};  
         int dy[] = {-1, -2, -2, -1, 1, 2, 2, 1};
         int r = scan.nextInt();
         int c = scan.nextInt();
         int gr = scan.nextInt();
         int gc= scan.nextInt();
         int lr = scan.nextInt();
         int lc = scan.nextInt();
         boolean found = false;
         int[][] distances = new int[r][c];
         Deque<Position> queue = new ArrayDeque<>();
         queue.addLast(new Position(gr - 1, gc - 1));
         while (!queue.isEmpty()) {
            Position position = queue.removeFirst();
            int currR = position.r;
            int currC = position.c;
            if (currR == lr - 1 && currC == lc - 1) {
               System.out.println(distances[currR][currC]);
               found = true;
               break;
            }
            for (int i = 0; i < 8; i++) {
               int nextR = currR + dx[i];
               int nextC = currC + dy[i];
               if (isInBounds(nextR, nextC, r, c) && distances[nextR][nextC] == 0) {
                  distances[nextR][nextC] = distances[currR][currC] + 1;
                  queue.addLast(new Position(nextR, nextC));
               }
            }
         }
      
         if (!found) {
            System.out.println("impossible");
         }
         if (!scan.hasNextInt()) {
            return;
         }
        
      }
      
   }
   static boolean isInBounds(int r, int c, int rMax, int cMax) {
      return r < rMax && c < cMax && r >= 0 && c >= 0;
   }

   private static class Position {
      int r;
      int c;
   
      public Position(int r, int c) {
         this.r = r;
         this.c = c;
      }
   }
}


