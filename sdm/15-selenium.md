---
layout: default
title: Selenium
---

# Selenium

[← Back to Home](../index.md)

---

## What is Selenium?

> **Selenium** is an open-source framework for automating web browser interactions across multiple browsers and platforms.

### History
- Created in 2004 by Jason Huggins at ThoughtWorks
- Named Selenium as an antidote to Mercury (commercial testing tool)
- Selenium 2.0 merged with WebDriver in 2011

### Why Selenium?
- **Open Source**: Free to use and modify
- **Cross-Browser**: Chrome, Firefox, Safari, Edge, IE
- **Cross-Platform**: Windows, macOS, Linux
- **Multi-Language**: Java, Python, C#, JavaScript, Ruby
- **Large Community**: Extensive support and plugins

---

## Selenium Components

| Component | Definition | Use Case |
|-----------|------------|----------|
| **Selenium WebDriver** | API for direct browser control | Automated test scripts |
| **Selenium IDE** | Browser extension for record and playback | Quick test prototyping |
| **Selenium Grid** | Distributed test execution | Parallel testing across machines |

### Selenium IDE vs WebDriver vs Grid

| Aspect | IDE | WebDriver | Grid |
|--------|-----|-----------|------|
| **Learning Curve** | Easy | Medium | Hard |
| **Programming** | No coding | Code required | Code required |
| **Flexibility** | Low | High | High |
| **Parallel Execution** | No | No (single) | Yes |

---

## WebDriver Architecture

```
┌──────────────────┐    ┌────────────────────┐    ┌─────────────────┐    ┌─────────────┐
│   Test Script    │───►│   WebDriver API    │───►│  Browser Driver │───►│   Browser   │
│   (Java/Python)  │    │   (Selenium)       │    │  (ChromeDriver) │    │   (Chrome)  │
└──────────────────┘    └────────────────────┘    └─────────────────┘    └─────────────┘
```

### WebDriver Protocol
> WebDriver uses **W3C WebDriver Protocol** (formerly JSON Wire Protocol) to communicate with browsers via HTTP REST API.

### Browser Drivers

| Browser | Driver |
|---------|--------|
| Chrome | chromedriver |
| Firefox | geckodriver |
| Edge | msedgedriver |
| Safari | Built-in (safaridriver) |

---

## Element Locators

> **Locators** are strategies used to identify elements on a web page.

| Locator | Description | Speed | Reliability |
|---------|-------------|-------|-------------|
| **ID** | Unique element identifier | Fastest | Best |
| **Name** | Element's name attribute | Fast | Good |
| **Class Name** | Element's CSS class | Fast | Moderate |
| **Tag Name** | HTML tag type | Fast | Low |
| **Link Text** | Exact text of hyperlink | Fast | Moderate |
| **Partial Link Text** | Partial hyperlink text | Fast | Moderate |
| **CSS Selector** | CSS-based selection | Fast | Good |
| **XPath** | XML path expression | Slower | Best (flexible) |

### Locator Priority (Best Practice)
1. ID (most reliable)
2. Name
3. CSS Selector
4. XPath (most flexible, but slower)

### XPath Types

| Type | Description | Example |
|------|-------------|---------|
| **Absolute** | Full path from root | `/html/body/div/form/input` |
| **Relative** | Starts anywhere with `//` | `//input[@id='username']` |
| **Contains** | Partial attribute match | `//input[contains(@class,'btn')]` |
| **Text** | Match by text content | `//button[text()='Submit']` |

---

## Python Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()
driver.get("https://example.com")
driver.maximize_window()

# Find and interact with elements
username = driver.find_element(By.ID, "username")
username.send_keys("testuser")

password = driver.find_element(By.ID, "password")
password.send_keys("password123")

login_btn = driver.find_element(By.ID, "login")
login_btn.click()

# Wait and assert
WebDriverWait(driver, 10).until(
    EC.title_contains("Dashboard")
)
assert "Dashboard" in driver.title

# Cleanup
driver.quit()
```

## Java Example

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import java.time.Duration;

public class LoginTest {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        driver.get("https://example.com");
        driver.manage().window().maximize();
        
        // Interact with elements
        driver.findElement(By.id("username")).sendKeys("user");
        driver.findElement(By.id("password")).sendKeys("pass");
        driver.findElement(By.id("login")).click();
        
        // Explicit wait
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.titleContains("Dashboard"));
        
        driver.quit();
    }
}
```

---

## Waits in Selenium

> **Waits** handle synchronization between test script and browser.

### Types of Waits

| Wait Type | Definition | Scope |
|-----------|------------|-------|
| **Implicit Wait** | Wait for element to appear (global) | Entire session |
| **Explicit Wait** | Wait for specific condition | Single element |
| **Fluent Wait** | Explicit wait with polling interval | Single element |

### Wait Examples

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implicit Wait (global)
driver.implicitly_wait(10)  # Wait up to 10 seconds

# Explicit Wait (specific condition)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "id")))
element = wait.until(EC.element_to_be_clickable((By.ID, "btn")))
element = wait.until(EC.visibility_of_element_located((By.ID, "id")))

# Fluent Wait (with polling)
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 10, poll_frequency=0.5,
                     ignored_exceptions=[NoSuchElementException])
```

### Expected Conditions

| Condition | Description |
|-----------|-------------|
| `presence_of_element_located` | Element is in DOM |
| `visibility_of_element_located` | Element is visible |
| `element_to_be_clickable` | Element is visible and enabled |
| `text_to_be_present_in_element` | Text is in element |
| `alert_is_present` | Alert popup exists |

---

## Common Selenium Actions

```python
# Navigation
driver.get("url")
driver.back()
driver.forward()
driver.refresh()

# Window Management
driver.maximize_window()
driver.get_screenshot_as_file("screenshot.png")
driver.current_url
driver.title

# Element Interactions
element.click()
element.send_keys("text")
element.clear()
element.text
element.get_attribute("href")
element.is_displayed()
element.is_enabled()
element.is_selected()

# Dropdowns
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_visible_text("Option")
select.select_by_value("value")
select.select_by_index(1)

# Alerts
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
alert.text
alert.send_keys("input")

# Frames
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()

# Windows/Tabs
main_window = driver.current_window_handle
all_windows = driver.window_handles
driver.switch_to.window(window_handle)
```

---

## Page Object Model (POM)

> **POM** is a design pattern that creates an object repository for web UI elements, separating test logic from page elements.

### Benefits of POM
- **Reusability**: Page objects reused across tests
- **Maintainability**: Element changes in one place
- **Readability**: Clean, readable test code
- **Reduced Duplication**: DRY principle

### POM Example

```python
# page_objects/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login")
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

# tests/test_login.py
def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.login("user", "pass")
    assert "Dashboard" in driver.title
    driver.quit()
```

---

## Selenium Grid

> **Selenium Grid** enables parallel test execution across multiple machines and browsers.

### Grid Architecture

```
┌─────────────────────┐
│        Hub          │  ← Central server
│  (manages sessions) │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼     ▼     ▼
┌──────┐┌──────┐┌──────┐
│Node 1││Node 2││Node 3│  ← Execute tests
│Chrome││Firefox││Safari│
└──────┘└──────┘└──────┘
```

### Benefits
- Parallel execution reduces test time
- Cross-browser testing on different machines
- Centralized configuration

---

## Test Frameworks with Selenium

| Framework | Language | Features |
|-----------|----------|----------|
| **pytest** | Python | Fixtures, assertions, plugins |
| **unittest** | Python | Built-in, xUnit style |
| **TestNG** | Java | Annotations, parallel, data-driven |
| **JUnit** | Java | Assertions, test lifecycle |

---

[← Previous: Manual & Automation Testing](14-manual-automation-testing.md) | [Next: Jenkins →](16-jenkins.md)
