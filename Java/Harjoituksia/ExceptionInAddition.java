import java.util.Scanner;
import java.util.*;

public class ExceptionInAddition {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int testedNumber = 0;
        boolean inputCorrect = true;
        do {
            try {
                System.out.print("Type in the number for testing: ");
                testedNumber = reader.nextInt();
                inputCorrect = true;
            } catch (InputMismatchException e) {
                System.out.println("You did not type in an integer!");
                inputCorrect = false;
                reader.nextLine();
            }
        } while(!inputCorrect);
        
        try {
            testValue(testedNumber);
            System.out.println("Value was between 5 and 10.");
        } catch(SmallException e) {
            System.out.println("SmallException caught!");
            printErrorReport(e);
        } catch(BigException e) {
            System.out.println("BigException caught!");
            printErrorReport(e);
        }   
    }
    private static void testValue(int number) throws SmallException, BigException {
		if (number < 5)
			throw new SmallException("Value is lower than 5");
		if (number > 10)
			throw new BigException("Value is higher than 10");
	}
	private static void printErrorReport(Exception e) {
		System.out.println(e.getMessage());	
	}
}
class SmallException extends Exception {
	public SmallException(String message) {
		super(message);	
	}
}
class BigException extends Exception {
	public BigException(String message) {
		super(message);	
	}
}

