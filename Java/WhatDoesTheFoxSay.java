  
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;

/**
 * Template for "What does the fox say?"
 * Problem ID: whatdoesthefoxsay
 * https://open.kattis.com/problems/whatdoesthefoxsay
 */
public class WhatDoesTheFoxSay {
  public static void main(String[] args) {
    // We need to create and scanner and get the number of cases to be read in.
    Scanner in = new Scanner(System.in);
    int cases = Integer.parseInt(in.nextLine());

    for (int x = 0; x < cases; x++) {
      // Order matters for this problem, so we will use an ArrayList to store the second line of input.
      ArrayList<String> allSoundsHeard = new ArrayList<String>(Arrays.asList(in.nextLine().split(" ")));
          while (in.hasNext()) {

            String sound = in.nextLine();
            if (sound.equals("what does the fox say?")) {
              break;
            }
            sound = sound.split(" ")[2];
            allSoundsHeard.removeAll(Collections.singleton(sound));
          }
        

      // This will output what is left in the ArrayList after filtering out the other sounds.
      System.out.println(String.join(" ", allSoundsHeard));
    }
  }
}