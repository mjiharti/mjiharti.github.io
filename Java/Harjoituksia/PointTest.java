import java.util.Scanner;
 
public class PointTest {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Type in the first values of the coordinates:");
        System.out.print("x: ");
        int x = reader.nextInt();
        System.out.print("y: ");
        int y = reader.nextInt();
        
        Point point = new Point(x, y);
         
        System.out.println("Point is now at : " + point);
        System.out.println("Type in the change of x and y coordinates");
        System.out.print("x: ");
        x = reader.nextInt();
        System.out.print("y: ");
        y = reader.nextInt();
        
        point.move(x, y);
        System.out.println("Point is now at: " + point);
    }
}

class Point {
	private int x;
	private int y;
	
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
		this.validateXandY();
	}
	
	public void move(int x, int y) {
		this.x += x;
		this.y += y;
		this.validateXandY();
	}
	
	public String toString() {
		return ("(" + x + "," + y + ")");
	}	
	private void validateXandY() {
		if (this.x < 0)
			this.x = 0;
		if (this.x > 100)
			this.x = 100;
		
		if (this.y < 0)
			this.y = 0;
		if (this.y > 100)
			this.y = 100;
	}
}