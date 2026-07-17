import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

import java.util.List;

public class FindElementsByTableTags {
    WebDriver driver;

    @Test
    void firstTest() {
        driver = new ChromeDriver();
        driver.get("https://the-internet.herokuapp.com/");
        sleep(1);
        driver.manage().window().maximize();
        sleep(1);
        driver.findElement(By.linkText("Sortable Data Tables")).click();
        WebElement table = driver.findElement(By.id("table1"));
        List<WebElement> tableRows = table.findElements(By.tagName("tr"));
        for (int i = 0; i < tableRows.size(); i++) {
            System.out.println(tableRows.get(i).getText());
        }
        sleep(1);
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

