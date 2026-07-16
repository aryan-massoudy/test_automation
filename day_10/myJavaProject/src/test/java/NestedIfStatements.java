import java.util.Scanner;

public class NestedIfStatements {
    void main () {
        Scanner userInput= new Scanner(System.in);
        System.out.println("Please enter your age:");

        int age = userInput.nextInt();
        if (age > 0) {
            if (age > 18)
                System.out.println("You are allowed to the website");
            else
                System.out.println("You are NOT allowed to the website");

        }
        else
            System.out.println("You have entered an invalid age");


    }
}
