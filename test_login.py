def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")

    page.screenshot(path="playwright_screenshot.png")

    page.get_by_role("button").click()

    # Option 1: Wait for a dashboard-specific element
    page.wait_for_selector("h6:has-text('Dashboard')", timeout=5000)
    assert page.locator("h6:has-text('Dashboard')").is_visible()

    page.screenshot(path="playwright_screenshot.png")


def test_login_wrong_credentials(page):
    # Go to login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Fill in wrong credentials
    page.get_by_placeholder("Username").fill("WrongUser")
    page.get_by_placeholder("Password").fill("WrongPass")

    # Click the login button
    page.get_by_role("button", name="Login").click()

    # Wait for error message to appear
    error_locator = page.locator("p:has-text('Invalid credentials')")
    error_locator.wait_for(timeout=5000)

    # Assert that the error message is visible
    assert error_locator.is_visible()

    # Optional: take a screenshot for verification
    page.screenshot(path="login_failed.png")

    # Optional: confirm URL has not changed to dashboard
    assert "/dashboard" not in page.url

