import java.util.Scanner;

public class IfStatementExercise {

    void main () {
        Scanner input = new Scanner(System.in);

        System.out.println("------------------------------------");
        System.out.println("Enter 1 for subtraction.");
        System.out.println("Enter 2 for addition.");
        System.out.println("Enter 3 for multiplication.");
        System.out.println("------------------------------------");

        System.out.println("Please enter you choice: ");
        int userChoice = input.nextInt();

        System.out.println("Enter the first number: ");
        int firstNum = input.nextInt();

        System.out.println("Enter the second number: ");
        int secondNum = input.nextInt();

        switch(userChoice) {
            case 1:
                System.out.println("The result is: " + (firstNum - secondNum));
                break;

            case 2:
                System.out.println("The result is: " + (firstNum + secondNum));
                break;

            case 3:
                System.out.println("The result is: " + (firstNum * secondNum));
                break;

            default:
                System.out.println("You have entered an invalid value.");


        }
    }
}
