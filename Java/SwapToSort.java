import java.util.*;
import java.io.*;
public class SwapToSort {
public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int n = Integer.parseInt(st.nextToken());
	int k = Integer.parseInt(st.nextToken());
	boolean works = true;
	int[] uf = new int[n];
	for (int i = 0; i < uf.length; i++) {
		uf[i] = i;
	}
	for (int i = 0; i < k; i++) {
		st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken()) - 1;
		int b = Integer.parseInt(st.nextToken()) - 1;
		union(uf, a, b);
	}
	for (int i = 1; i < n; i++) {
		if (find(uf, i) != find(uf, n - i - 1)) works = false;
	}
	if (works) System.out.println("Yes");
	else System.out.println("No");

}
static void union(int[] parents, int x, int y) {
	int parentX = find(parents, x);
	int parentY = find(parents, y);
	parents[parentY] = parentX;

}
static int find(int[] parents, int child) {
	if (parents[child] == child) {
		return child;
	}
	parents[child] = find(parents, parents[child]);
	return parents[child];
}

}