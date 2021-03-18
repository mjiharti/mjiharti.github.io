public class Joku {

    public static void main(String[] args) {
    	Object thing = "I am thing!";
    	//Integer intThing = (String)thing;

		Object thing1 = " I am thing!";
		Integer intThing2 = (Integer) thing1;

		Object thing2 = "I am thing!";
		((String) thing2).length();

		Object thing3 = "I am thing!";
		thing3.toString();
    } 
}