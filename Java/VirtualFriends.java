import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class VirtualFriends{
    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(in.readLine());
        for (int i = 0; i < n; i++) {
            int friends = Integer.parseInt(in.readLine());
            UnionFind uf = new UnionFind(100004);
            HashMap<String, Integer> map = new HashMap<String, Integer>();
                int count = 0;
            for (int j = 0; j < friends; j++) {
                st = new StringTokenizer(in.readLine());

                String first = st.nextToken();
                String second = st.nextToken( );

                if (!map.containsKey(first)) {
                    map.put(first , count);
                    count++;

                }
                
                if (!map.containsKey(second)) {
                    map.put(second , count);
                    count++;
                }
                
                int x = map.get(first);
                int y = map.get(second);
                uf.union(x, y);
                System.out.println(uf.size[uf.find(y)]);
            }
        }
        
    }

}
class UnionFind {
    int[] size;
    int[] parents;
    public UnionFind(int n) {
        size = new int[n];
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
            size[i] = 1;
        }
    }
    public int find(int child) {
        if (parents[child] == child) {
            return child;
        }
         parents[child] = find(parents[child]);
         return parents[child];

        }
    public void union(int childX, int childY) {
        int parentX = find(childX);
        int parentY = find(childY);
        if (parentX != parentY) {
            size[parentY] += size[parentX];
            size[parentX] = size[parentY];
        }

        parents[parentY] = parentX;
    }
}