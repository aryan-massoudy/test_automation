public class ForLoop {
    void main () {
        for (int i = 0; i < 5; i++) {
            System.out.println("The current value of i is: " + i);
            if (i == 4)
                System.out.println("The value of i has reached 4. The loop breaks.");
        }
    }
}
