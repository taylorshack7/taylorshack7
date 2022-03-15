import java.util.Scanner;

public class Q2_TestAvg { // declare class
    static double calcAverage(double one, double two, double three, double four, double five){ //set calcAverage method with five paramters
        return ((one + two + three + four +five)/5.0); //return average
    }

    static double determineGrade(double testScore){ // set determineGrade method with one parameter
        if (testScore >= 90.0 && testScore != average){ //check letter grade is A
            System.out.println("Your test grade " + testScore +" is an A!"); // display letter grade w/ results
        }
        else if (testScore >=80.0 && testScore != average){ //check letter grade is B
            System.out.println("Your test grade " + testScore +" is a B!"); // display letter grade w/ results

        }
        else if (testScore >=70.0 && testScore != average){  //check letter grade is C
            System.out.println("Your test grade " + testScore +" is a C!"); // display letter grade w/ results
        }
        else if (testScore >=60.0 && testScore != average){  //check letter grade is D
            System.out.println("Your test grade " + testScore +" is a D!"); // display letter grade w/ results

        }
        else if (testScore < 60. && testScore != average){  //check letter grade is F
            System.out.println("Your test grade " + testScore +" is an F!"); // display letter grade w/ results
        }
        if (testScore == average){ // check if our testscore is actually average
            if (testScore >= 90.0){ //check average letter grade is A
                System.out.println("Your average grade " + testScore +" is an A!"); // display letter grade w/ result
            }
            else if (testScore >=80.0){ //check average letter grade is B
                System.out.println("Your average grade " + testScore +" is a B!"); // display letter grade w/ result

            }
            else if (testScore >=70.0){ //check average letter grade is C
                System.out.println("Your average grade " + testScore +" is a C!"); // display letter grade w/ result
            }
            else if (testScore >=60.0){ //check average letter grade is  D
                System.out.println("Your average grade " + testScore +" is a D!"); // display letter grade w/ result

            }
            else{ //check average letter grade is F
                System.out.println("Your average grade " + testScore +" is an F!"); // display letter grade w/ result
            }
        }
        return average; //had to return something
    }

    public static void main(String[] args){ //declare method main to run program
        System.out.print("Enter First Test Score: "); // get test score
        Scanner input1 = new Scanner(System.in); // input from user
        double inp1 = input1.nextDouble(); // set aside for further use
        System.out.print(""); // formatting space
        System.out.print("Enter Second Test Score: ");// get test score
        Scanner input2 = new Scanner(System.in);// input from user
        double inp2 = input2.nextDouble(); // set aside for further use
        System.out.print(""); // formatting space
        System.out.print("Enter Third Test Score: ");// get test score
        Scanner input3 = new Scanner(System.in);// input from user
        double inp3 = input3.nextDouble(); // set aside for further use
        System.out.print(""); // formatting space
        System.out.print("Enter Fourth Test Score: ");// get test score
        Scanner input4 = new Scanner(System.in);// input from user
        double inp4 = input4.nextDouble(); // set aside for further use
        System.out.print(""); // formatting space
        System.out.print("Enter Fifth Test Score: ");// get test score
        Scanner input5 = new Scanner(System.in);// input from user
        double inp5 = input5.nextDouble(); // set aside for further use
        System.out.print(""); // formatting space

        average = calcAverage(inp1, inp2, inp3, inp4, inp5); // calc average


        testScore = determineGrade(inp1); //run all user inputs
        testScore = determineGrade(inp2);
        testScore = determineGrade(inp3);
        testScore = determineGrade(inp4);
        testScore = determineGrade(inp5);
        determineGrade(average); //get average letter grade


    }
    static double average; // set vars
    static double testScore;


}
