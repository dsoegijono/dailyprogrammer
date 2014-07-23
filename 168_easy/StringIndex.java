import java.io.*;

public class StringIndex {

  static String str = "...You...!!!@!3124131212 Hello have this is a --- string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ Congratz this!!!!!!!!!!!!!!!!one ---Problem\n\n";
  static int[] positions = { 12, -1, 1, -100, 4, 1000, 9, -1000, 16, 13, 17, 15 }; //TODO: user input?

  public static void main(String[] args) {
    String[] words = str.split("[^a-zA-Z0-9]+");
    for (int i : positions) {
      if (i >= 0 && i < words.length) {
        System.out.print(words[i] + " ");
      }
    }
    System.out.println();
  }
}
