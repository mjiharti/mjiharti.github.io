import java.util.Scanner;

public class Laskin {

	public static void main(String[] args) { 
        
        Scanner sc = new Scanner(System.in);        
        System.out.print("Choose from the following calculations:\n" +
        	"1: subtraction\n2: addition\n3: multiplication\n4: division\n" +
        	"5: remainder\n\n");
        
        System.out.print("Make your choice: ");
        int valinta = sc.nextInt();
        if (valinta >= 1 && valinta <= 5) {
        	String loppuTulos = "";
        	System.out.print("\nType in the first number: ");
        	int ekaLuku = sc.nextInt();
        	System.out.print("Type in the second number: ");
        	int tokaLuku = sc.nextInt();
        	switch (valinta) {
        	case 1:
        		loppuTulos = ekaLuku + " - " + tokaLuku + " = " + (ekaLuku - tokaLuku);
        		break;
        	case 2:
        		loppuTulos = ekaLuku + " + " + tokaLuku + " = " + (ekaLuku + tokaLuku);
        		break;
        	case 3:
        		loppuTulos = ekaLuku + " * " + tokaLuku + " = " + (ekaLuku * tokaLuku);
        		break;
        	case 4:	        		
        		loppuTulos = ekaLuku + " / " + tokaLuku + " = " + ((double)ekaLuku / tokaLuku);
        		break;
        	case 5:	
        		loppuTulos = ekaLuku + " % " + tokaLuku + " = " + (ekaLuku % tokaLuku);
        		break;
        	}
        	System.out.println("\n" + loppuTulos);
			sc.close();
        } else {
        	System.out.println("\nInvalid choice.");	
        }
    } 
}

/*
Choose from the following calculations:
1: subtraction
2: addition
3: multiplication
4: division
5: remainder

Make your choice: 8

Invalid choice.
*/