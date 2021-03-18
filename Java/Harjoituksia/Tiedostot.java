import java.io.*;

public class Tiedostot {
    public static void main(String[] args) throws IOException {    	
        BufferedReader reader = new BufferedReader(new FileReader("grades.txt"));
        boolean rowsLeft = true;
        String readRow = null;                
        String incrementedGrades = "";
        while(rowsLeft) {
            readRow = reader.readLine();
            if(readRow == null) {
                rowsLeft = false;
            } else {
                int grade = Integer.parseInt(readRow);
                int newGrade = grade + 1;
                if (newGrade > 10)
                	newGrade = 10;
                incrementedGrades += "" + newGrade + "\n";
            }
        }
        reader.close();
        PrintWriter result = new PrintWriter("results.txt");
        result.println(incrementedGrades);
        result.close();        
        printResults("results.txt");
    }
    
    public static void printResults(String file) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(file));
        boolean rowsLeft = true;
        String readRow = null;
        
        System.out.println("Updated grades: ");

        while(rowsLeft) {
            readRow = reader.readLine();
            if(readRow == null) {
                rowsLeft = false;
            } else {
                System.out.print(readRow);
                System.out.println(" ");
            }
        }
        reader.close();
    }
}
/*import java.io.*;
import java.util.Scanner;

public class Tiedostot {
	public static void main(String[] args) throws IOException {
		int counter = 0;
		double sum = 0;
		String fileName = "grades.txt";
		String readRow = null;							
		FileReader file = new FileReader(fileName);		
		BufferedReader reader = new BufferedReader(file);
		boolean rowsLeft = true;
		System.out.println("Grades:");
		while (rowsLeft) {
			readRow = reader.readLine();
			if (readRow == null) {
				rowsLeft = false;				
			} else {
				int grade = Integer.parseInt(readRow);
				System.out.println("" + grade);
				sum += grade;
				counter++;
			}	
		}
		System.out.println("Average: " + ((double)sum/counter));
	}
}*/
