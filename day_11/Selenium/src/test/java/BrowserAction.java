import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class BrowserAction {
    WebDriver driver;

    @Test
    void firstTest() {
        driver = new ChromeDriver();
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        navigateToPage("https://automationexercise.com/");
        navigateBack();
        navigateForward();
        refreshPage();

    }

    void navigateToPage(String url) {
        driver.navigate().to(url);
    }

    void navigateBack() {
        driver.navigate().back();
    }

    void navigateForward() {
        driver.navigate().forward();
    }

    void refreshPage() {
        driver.navigate().refresh();
    }

}