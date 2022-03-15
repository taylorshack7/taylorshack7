import java.util.Scanner; // call scanner to take user input

public class Q3_Conversion { //start class
    public static void main(String[] args){ //main method declaration

        int j; // set counter j var
        double meter; // set meter var
        Scanner input = new Scanner(System.in); // get me that input

        do { // checks for positive value in meter
            System.out.print("Enter a positive number for meters: "); // prompt user for input
            //System.out.println(""); //format spacing
            meter = input.nextDouble(); //set meter to input
        } while (meter < 0); //if true, keep asking until positive

        do { // checks if user wants to terminate prorgam
            menu(); // print menu options
            System.out.print("Enter your choice (1-4): "); // enter choice 1-4
            j = input.nextInt(); // set counter j to make life easy

            while (j > 5 || j < 1){
                System.out.print("Error: please enter number 1-4");
                j = input.nextInt();
            }

            switch (j) { //execute case in which j is true
                case 1: //case 1 converts meters to kilometers
                    showKilometers(meter); //call method showKilometers
                    break; // break that bad boy to start again w/o residual outputs
                case 2: //case 2 converts meters to inches
                    showInches(meter); // call method to convert meters to inches
                    break; //break to avoid excess output
                case 3: // converts meters to feet
                    showFeet(meter); // call method to convert
                    break;//break to avoid excess output
                case 4: // ends our program in the do while loop
                    System.out.print("Program terminated"); // let the user know prorgram is done
                    break;//break to avoid excess output
                    // no default case needed

                }
        } while (j != 4); // if j == 4, terminate program
        }



    public static void showKilometers(double meter) { //method for meters to kilometers
        System.out.print(meter + " meters is "+ (meter * .001) + " kilometers\n"); //print our results
    }
    public static void showInches(double meter){ //method for meters to inches
        System.out.print(meter + " meters is "+ (meter * 39.37 + " inches\n")); //print our results
    }
    public static void showFeet(double meter){ //method for meters to feet
        System.out.print(meter + " meters is "+ (meter * 3.28084 + " feet\n")); //print our results
    }
    public static void menu() { // method to display menu options for user
        System.out.print("Enter a number 1-4 if you would like to:\n" + // print out options
                "1. Convert to kilometers\n" +
                "2. Convert to inches\n" +
                "3. Convert to feet\n" +
                "4. Quit the program\n");
    }
    } // end program
