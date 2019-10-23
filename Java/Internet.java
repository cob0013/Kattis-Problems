import java.util.*;

import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.StringTokenizer;
public class Internet {
    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
        int houses = Integer.parseInt(st.nextToken());
        int cables = Integer.parseInt(st.nextToken());
        int[] parents = new int[houses];
        for (int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }
        for (int i = 0; i < cables; i++) {
            st = new StringTokenizer(br.readLine());
            union(parents, Integer.parseInt(st.nextToken())- 1, Integer.parseInt(st.nextToken())-1);
        }
        boolean works = true;
        int check = find(parents, 0);
        for (int i = 1; i < parents.length; i++) {
            if (check != find(parents, i)) {
                System.out.println(i + 1);
                works = false;
            }
            
        }
        if (works) {
        
        System.out.println("Connected");
    }
    }
    static void union(int[] parents, int x, int y) {
        int parentX = find(parents, x);
        int parentY = find(parents, y);
        parents[parentY] = parentX;
    }
    static boolean connected(int[] parents,int x, int y) {
        return find(parents, x) == find(parents, y);
    }
    static  int find(int[] parents, int child) {
        if (parents[child] == child) {
            return child;
        }
        parents[child] = find(parents, parents[child]);
        return parents[child];
    }
}