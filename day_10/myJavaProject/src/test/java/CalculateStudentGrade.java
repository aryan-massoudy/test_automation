import java.util.Scanner;

public class CalculateStudentGrade {
    void main () {
        int totalObtainablePointsExam = 200;
        int totalObtainablePointsAssignment = 40;

        int studentExamPoints;
        int studentAssignmentPoints;

        Scanner userInput = new Scanner(System.in);
        System.out.println("Please enter your exam score: ");
        studentExamPoints = userInput.nextInt();

        System.out.println("Please enter your assignment score: ");
        studentAssignmentPoints = userInput.nextInt();

        float studentFinalScore = (float) (studentAssignmentPoints + studentExamPoints) / (totalObtainablePointsExam +
                totalObtainablePointsAssignment);
        System.out.println("Your final score is : " + studentFinalScore * 100 +"%");


    }
}
