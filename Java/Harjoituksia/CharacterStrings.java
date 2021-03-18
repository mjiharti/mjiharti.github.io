import java.util.Scanner;

public class CharacterStrings {
    public static void main(String args[]) {
        String characterString;
        Scanner reader = new Scanner(System.in);

        Printer printerObject = new Printer();

        System.out.print("Type in a character string: ");
        characterString = reader.nextLine();		
        characterString = printerObject.bigSmall(characterString, reader);
        printerObject.reverseSpace(characterString, reader);
		reader.close();	
    }
}

class Printer {

	public String bigSmall(String merkkiJono, Scanner sc) {		
		System.out.print("Do you want upper case or lower case? (upper/lower): ");
		String toiminto = sc.nextLine();

		if(toiminto.equals("upper")) {
			return merkkiJono.toUpperCase(); 
		}
		if(toiminto.equals("lower")) {
			return merkkiJono.toLowerCase();
		}
		return "";
	}
	
	public void reverseSpace(String merkkiJono, Scanner sc) {
		String muokattu = "";
		System.out.print("How would you like the string to be printed? (reverse/separated): ");		
		String toiminto = sc.nextLine();		
		if(toiminto.equals("reverse")) {
			for (int j=merkkiJono.length()-1; j>=0; j--) {
				muokattu += merkkiJono.charAt(j);
			}
		}
		if(toiminto.equals("separated")) {
			for (int i=0; i<merkkiJono.length(); i++) {
				if (i == 0)
					muokattu += merkkiJono.charAt(i);
				else
					muokattu += " " + merkkiJono.charAt(i);
			}
		}
		System.out.println("Here is your character string: " + muokattu);
	}
}