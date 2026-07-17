import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class FirstNgClass {

    WebDriver driver;

    @BeforeTest
    public void prepareDriver () {
        driver = new ChromeDriver();
    }

    @AfterTest
    public void tearDown () {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    public void OpenWebsite() throws InterruptedException {
        driver.get("https://the-internet.herokuapp.com/");
        System.out.println("Opening the browser");
        Thread.sleep(3000);
    }

    @Test(dependsOnMethods = "OpenWebsite")
    public void SignUp() {
        System.out.println("Signing up");
    }

    @Test(dependsOnMethods = "SignUp")
    public void SignIn() {
        System.out.println("Signing in");
    }

    @Test(dependsOnMethods = "SignIn")
    public void AddItemToCart() {
        System.out.println("Adding item to the cart");
    }

    @Test(dependsOnMethods = "AddItemToCart")
    public void LoggingOut() {
        System.out.println("Logging out");
    }

    @Test
    public void myTest() {
        System.out.println("This is an independent test");
    }
}