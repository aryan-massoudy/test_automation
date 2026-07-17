import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

import java.util.Set;

public class BrowserAction {
    WebDriver driver;

    @Test
    void firstTest() {
        driver = new ChromeDriver();
        driver.get("https://the-internet.herokuapp.com/");
        sleep(3);
        maximizeWindow();
        sleep(3);
        driver.findElement(By.linkText("Form Authentication")).click();
        sleep(2);
        driver.findElement(By.id("username")).sendKeys("tomsmith");
        sleep(2);
        driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");
        sleep(2);
        driver.findElement(By.cssSelector(".fa.fa-2x.fa-sign-in")).click();
        sleep(2);
        quitTheBrowser();

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

    void maximizeWindow() {
        driver.manage().window().maximize();
    }

    void minimizeWindows() {
        driver.manage().window().minimize();
    }

    void setToIphone12Dimensions() {
        Dimension myWindowDimension = new Dimension(390, 844);
        driver.manage().window().setSize(myWindowDimension);
    }

    void getCurrentUrl() {
        String currentPageURL = driver.getCurrentUrl();
        System.out.println("Current URL is: " + currentPageURL);
    }

    void getPageTitle() {
        String currentPageTitle = driver.getCurrentUrl();
        System.out.println("Current Page Title is: " + currentPageTitle);
    }

    void getWindowHandle() {
        String windowHandle = driver.getWindowHandle();
        System.out.println("The current window handle is: " + windowHandle);
    }

    void getWindowHandles() {
        Set windowHandle = driver.getWindowHandles();
        System.out.println("Window handles are: " + windowHandle);
    }

    void quitTheBrowser() {
        driver.quit();
    }

    void sleep(int seconds) {
        try {
            Thread.sleep(seconds * 1000L); // Thread.sleep takes milliseconds
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Restore interrupted status
        }
    }
}