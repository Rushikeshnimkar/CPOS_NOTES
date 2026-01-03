---
layout: default
title: Selenium
---

# Selenium

[← Back to Home](../index.md)

---

## What is Selenium?

> **Selenium** is an open-source framework for automating web browser interactions.

## Components

| Component | Description |
|-----------|-------------|
| **Selenium WebDriver** | Direct browser control |
| **Selenium IDE** | Record and playback tool |
| **Selenium Grid** | Parallel test execution |

## WebDriver Architecture

```
Test Script → WebDriver API → Browser Driver → Browser
```

## Locators

| Locator | Example |
|---------|---------|
| ID | `driver.find_element(By.ID, "username")` |
| Name | `driver.find_element(By.NAME, "email")` |
| Class | `driver.find_element(By.CLASS_NAME, "btn")` |
| XPath | `driver.find_element(By.XPATH, "//input[@id='user']")` |
| CSS | `driver.find_element(By.CSS_SELECTOR, "#login")` |

## Python Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup
driver = webdriver.Chrome()
driver.get("https://example.com")

# Find and interact
username = driver.find_element(By.ID, "username")
username.send_keys("testuser")

password = driver.find_element(By.ID, "password")
password.send_keys("password123")

login_btn = driver.find_element(By.ID, "login")
login_btn.click()

# Assertions
assert "Dashboard" in driver.title

# Cleanup
driver.quit()
```

## Java Example

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;

public class LoginTest {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        
        driver.get("https://example.com");
        
        driver.findElement(By.id("username")).sendKeys("user");
        driver.findElement(By.id("password")).sendKeys("pass");
        driver.findElement(By.id("login")).click();
        
        driver.quit();
    }
}
```

## Common Commands

```python
# Navigation
driver.get("url")
driver.back()
driver.forward()
driver.refresh()

# Window
driver.maximize_window()
driver.get_screenshot_as_file("screenshot.png")

# Waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "id")))
```

---

[← Previous: Manual & Automation Testing](14-manual-automation-testing.md) | [Next: Jenkins →](16-jenkins.md)
