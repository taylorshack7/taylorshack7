import java.util.Scanner; // call scanner for user input
import java.lang.Math; // call math package for exponent function
public class Q4_PV { // set class
    public static void main(String[] args){ // declare main method to run program
    presentValue(); // call present value method to compute PV

    }
    public static void presentValue(){ // set PV method
        double FV; //set FV
        double rate; //set rate
        double n; // set time periods
        double denom; // set denom to make my life easy
        Scanner input = new Scanner(System.in); // get input for each
        System.out.println("Enter values as instructed... decimal not needed if not wanted"); // instructions
        System.out.println(""); //format space
        System.out.print("Enter Future Value (i.e. $10,000.89 -> 10000.89): "); // prompt user for FV
        FV = input.nextDouble(); // set future value
        System.out.print("Enter annual interest rate (i.e. 9.3% -> .093): "); // prompt user for rate
        rate = input.nextDouble(); // set rate
        System.out.print("Enter number of years (i.e. 10 years & 6 months -> 10.5): "); // prompt user for time
        n = input.nextDouble(); // set time
        denom = Math.pow((1+rate), n); // set
        System.out.print("Present Value = " +(FV/denom)); //display result

    }
    }