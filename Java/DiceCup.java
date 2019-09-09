import java.util.*;
public class DiceCup {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int die1 = scan.nextInt();
      int die2 = scan.nextInt();
      int[] values = new int[1000];
      for (int i = 1; i <= die1; i++) {
         for (int j = 1; j <= die2; j++) {
            values[i + j]++;
         }
      }
      int max = 0;
      for (int num: values) {
         if (num > max) {
            max = num; 
         }
      }
      for (int i = 0; i < values.length; i++) {
         if (values[i] == max) {
            System.out.println(i);
         }
      
      }
   	
   }
}