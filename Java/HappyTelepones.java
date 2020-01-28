import java.util.*;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.Scanner; 
import java.util.StringTokenizer;
public class HappyTelepones {
	public static void main(String[] args) throws IOException{
		  BufferedReader br = new BufferedReader( 
                              new InputStreamReader(System.in)); 
  
		StringBuilder output = new StringBuilder();
		String[] line = br.readLine().split(" ");
		int n = Integer.parseInt(line[0]);
		int m = Integer.parseInt(line[1]);

		while (true) {
			int[] a = new int[100005];
			int[] b = new int[100005];
			for (int i = 0; i < n; i++) {
				String[] info = br.readLine().split(" ");
				int start = Integer.parseInt(info[2]);
				int finish = start + Integer.parseInt(info[3]) - 1;
				a[i] = start;
				b[i] = finish;
			}
			for (int i = 0; i < m; i++) {
				String[] g = br.readLine().split(" ");
				int rangeStart = Integer.parseInt(g[0]);
				int rangeEnd = rangeStart + Integer.parseInt(g[1])  - 1;
				int ans = 0;
				for (int j = 0; j < n; j++) {
					if (!(b[j] < rangeStart || a[j] > rangeEnd)) {
						ans++;
					}
				}
				output.append("\n" + ans);
			}
	line = br.readLine().split(" ");
		n = Integer.parseInt(line[0]);
		m = Integer.parseInt(line[1]);
		if (n == 0 && m == 0) break;
	}
	System.out.println(output);
}
}