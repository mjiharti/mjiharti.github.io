import java.util.Scanner;

public class PrintThis {
    public static void main(String args[]) {   
        int answer = 1;
        boolean valueCorrect = true;
        GasMeter meter = new GasMeter();

		Scanner reader = new Scanner(System.in);
        while (valueCorrect) {            
            
            System.out.print("What do you want: 1=95, 2=98, 3=Diesel " + 
                "(type any other number to quit): ");
            answer = reader.nextInt();
           
            if(answer >= 1 && answer <= 3) {
                System.out.print("How much do you want to refuel: ");
                double amount = reader.nextDouble();
                meter.refuel(answer, amount);
            } else {
                valueCorrect = false;
            }									
        }
       
		reader.close();

        GasMeter.totalUsed();
        GasMeter.totalUsed95();
        GasMeter.totalUsed98();
        GasMeter.totalUsedDi();
   }
}

class GasMeter {
	private static double totalUsed = 0;
	private static double total95Used = 0;
	private static double total98Used = 0;
	private static double totalDiUsed = 0;
	
	public void refuel(int laatu, double maara) {
		switch (laatu) {
		case 1:
			totalUsed += maara;
			total95Used += maara;
			break;
		case 2:
			totalUsed += maara;
			total98Used += maara;
			break;
		case 3:
			totalUsed += maara;
			totalDiUsed += maara;
			break;
		}
	}
	public static void totalUsed() {
		System.out.println("Total used fuel: " + totalUsed);
	}
	public static void totalUsed95() {
		System.out.println("Total used 95 octane fuel: " + total95Used);
	}
	public static void totalUsed98() {
		System.out.println("Total used 98 octane fuel: " + total98Used);
	}
	public static void totalUsedDi() {
		System.out.println("Total used diesel fuel: " + totalDiUsed);
	}
}