import java.util.Scanner;

public class IfStatements {
    void main () {
        Scanner input = new Scanner(System.in);
        int age;
        System.out.println("Please enter your age: ");
        age = input.nextInt();
        if (age < 13) {
            System.out.println("Sorry, but you are too young for social media.");
            System.out.println("Use the mobile app.");
        }
        else
            System.out.println("Welcome to the social media website.");


    }
}
