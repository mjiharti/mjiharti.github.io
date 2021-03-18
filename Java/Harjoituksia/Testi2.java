import java.util.Scanner;

public class Testi2 {
	
	public static void main(String[] args) {
		int rows = 3;
		int columns = 2;
		
		int[][] matrix = new int[rows][columns]; 
		matrix = askInfo(rows, columns);
		printMatrix(matrix);
		countSum(matrix);
	}
	private static int[][] askInfo(int rows, int columns) {
		int[][] matrix = new int[rows][columns];
		Scanner sc = new Scanner(System.in);
		
		for (int i=0; i<rows; i++) {
			for (int j=0; j<columns; j++) {
				System.out.print("Type in the element " + (j+1) + " of the row " + (i+1) + ": ");
				int luku = sc.nextInt();
				matrix[i][j] = luku;
			}
		}
		return matrix;
	}
	private static void printMatrix(int[][] matrix) {
		System.out.println("\nMatrix:");
		for (int i=0; i<matrix.length; i++) {
			for (int j=0; j<matrix[i].length; j++) {
				System.out.print(matrix[i][j] + "\t");
			}
			System.out.print("\n");
		}
	}
	private static void countSum(int[][] matrix) {
		int summa = 0;
		for (int i=0; i<matrix.length; i++) {
			for (int j=0; j<matrix[i].length; j++) {
				summa += matrix[i][j];
			}
		}
		System.out.println("\nSum of the elements of the matrix: " + summa);
	}
}