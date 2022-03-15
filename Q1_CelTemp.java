import java.util.Scanner; // import scanner to take input from user

public class Q1_CelTemp { // set class
    static double celsius(double far) { // set method celsius
        return ((5.0 / 9.0) * (far - 32)); //convert from fahrenheit to celsius
    }


    public static void main(String[] args) { // declare main method to run program
        Scanner input = new Scanner(System.in); // get user input
        System.out.print("Enter temperature in Fahrenheit: "); //get temp in fahrenheit
        double F = input.nextDouble(); // set F to user input
        System.out.println("The temp in Celsius is: " + celsius(F)); // display temp in celsius and call celsius method
        System.out.println(""); // format space
        System.out.println("Table of the Fahrenheit temps 0-20 and their Celsius equivalents"); //display table of conversions
        for (int counter = 0; counter <= 20; counter++) { //run loop to display results
            System.out.printf("%s%d%s%f%n", "Fahrenheit ", counter, " Celsius ", celsius(counter)); //proper formatting and display

        }

    }
}
