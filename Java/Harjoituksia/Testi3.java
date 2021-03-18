import java.util.Scanner;

public class Testi3 {
	
	public static void main(String[] args) {
      
        int[] tempArray = new int[100];
        System.out.println("Type in numbers. Type zero to quit.");
        int amountOfNumbers = askInfo(tempArray);
       
        int[] realArray = new int[amountOfNumbers];
        copyInfo(realArray, tempArray);
      
        setArray(realArray);
        
        printArray(realArray);
    }

    private static int askInfo(int[] tempArray) {
    	int annettujaNumeroita = 0;
    	Scanner sc = new Scanner(System.in);
    	int numero = 0;
    	for (int i=0; i<tempArray.length; i++) {
    		System.out.print((i+1) + ". number: ");
    		numero = sc.nextInt();
    		if (numero != 0) {
    			tempArray[i] = numero;
    			annettujaNumeroita += 1;
    		} else {
    			return annettujaNumeroita;	
    		}
    	}  
    	return annettujaNumeroita;
    }
    
    private static void copyInfo(int[] realArray, int[] tempArray) {
    	for (int i=0; i<realArray.length; i++) {
    		realArray[i] = tempArray[i];	
    	}
    }
    
    private static void setArray(int[] realArray) {
    	for (int i=0; i<realArray.length; i++) {
    		for (int j=i+1; j<realArray.length; j++) {
    		//System.out.println("i=" + realArray[i] + " j=" + realArray[j]);
    			if (realArray[i] < realArray[j]) {
    				int temp = realArray[i];
    				realArray[i] = realArray[j];
    				realArray[j] = temp;	
    			}
    		}    			
    	}
    }
    
    public static void printArray(int[] realArray ) {
        System.out.println("\nOrdered array: ");
        for(int i = 0; i < realArray.length; i++) {
            System.out.println(realArray [i]);
        }
    }
}