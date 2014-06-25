import java.lang.Math;
import java.io.*;

public class GravityCalculator {
  
  static double G = 6.67e-11;
  
  static class Planet {
    String name;
    int radius;
    double density;
    double volume;
    double mass;
    
    Planet(String s, int r, double d) {
      name = s;
      radius = r;
      density = d;
      volume = 4.0 / 3 * Math.PI * Math.pow(r, 3);
      mass = volume * density;
    }
    
    double getForce(int m) {
      return G * m * this.mass / Math.pow(this.radius, 2);
    }
  }
  
  public static void main(String[] args) {
    System.out.println("Please enter input file name. Enter '-m' for manual input.");
    System.out.print("> ");
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    try {
      String filename = br.readLine();
      int m1 = 0, n = 0;
      Planet[] planets;
      if ("-m".equals(filename)) {
        System.out.print("Mass: ");
        m1 = Integer.parseInt(br.readLine());
        System.out.print("Number of planets: ");
        n = Integer.parseInt(br.readLine());
        planets = new Planet[n];
        for (int i = 0; i < n; i++) {
          System.out.print("> ");
          String p = br.readLine();
          String[] x = p.split(", ");
          planets[i] = new Planet(x[0], Integer.parseInt(x[1]), Double.parseDouble(x[2]));
        }
      } else {
        BufferedReader fileReader = new BufferedReader(new FileReader(filename));
        m1 = Integer.parseInt(fileReader.readLine());
        n = Integer.parseInt(fileReader.readLine());
        planets = new Planet[n];
        for (int i = 0; i < n; i++) {
          String p = fileReader.readLine();
          String[] x = p.split(", ");
          planets[i] = new Planet(x[0], Integer.parseInt(x[1]), Double.parseDouble(x[2]));
        }
      }
      
      for (int i = 0; i < planets.length; i++) {
        Planet p = planets[i];
        System.out.println(p.name + ": " + p.getForce(m1));
      }
    } catch (Exception e) {  
    }    
    
  }
}
