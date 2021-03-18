import java.util.Scanner;

class Numbers {
    public static void main(String [] args) {
        int characters = args.length;

        if (characters < 3) 
            System.out.println("You did not type in a calculation!");
        else if (characters % 2 == 0)
            System.out.println("Invalid number of command line parameters.");
        else {
            Calculator counter = new Calculator();
            counter.count(args);
        }
    }
}

class Calculator {
	public void count(String[] args) {		
		int loppuTulos = Integer.parseInt(args[0]);
		String laskuToimitus = args[0] + " ";
		
		for(int i=1; i<args.length-1; i+=2) {			
			if (args[i].equals("+")) {
				loppuTulos += Integer.parseInt(args[i+1]);
				laskuToimitus += "+ " + args[i+1] + " "; 
			} else {
				loppuTulos -= Integer.parseInt(args[i+1]);
				laskuToimitus += "- " + args[i+1] + " ";
			}
		}		
		System.out.println("Result of the calculation " + laskuToimitus + "is " + loppuTulos);
	}
}