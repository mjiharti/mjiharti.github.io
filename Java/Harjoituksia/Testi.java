import java.util.Scanner;

public class Testi {

	public static void main(String[] args) { 
        
        Scanner sc = new Scanner(System.in);        
        System.out.print("Amount of days: ");
        double totalTunnit = 0;
        double kaPaiva = 0;
        String kaikkiTunnit = "";
        int paivia = sc.nextInt();
        double[] tunnit = new double[paivia];
        for (int i=0; i < paivia; i++) {
        	System.out.print("Type in work hours of day " + (i+1) + ": ");
        	double annetutTunnit = sc.nextDouble();
        	tunnit[i] = annetutTunnit;
        }       
        
        for (int j=0; j<tunnit.length; j++) {
        	totalTunnit += tunnit[j];
        	kaikkiTunnit += " " + tunnit[j]; 
        }   
        System.out.println("Total of work hours: " + totalTunnit);
        System.out.println("average work day length: " + (totalTunnit / paivia));
        System.out.println("Inputted work hours:" + kaikkiTunnit);
    }   
}
/*
Amount of days: 3
Type in work hours of day 1: 5
Type in work hours of day 2: 2,6
Type in work hours of day 3: 5

Total of work hours: 12.6
average work day length: 4.2
Inputted work hours: 5.0 2.6 5.0
*/