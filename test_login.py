from pytest_bdd import given

@given("Given the user is on the OrangeHRM login page")
def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.get_by_role("button").click()

    # Option 1: Wait for a dashboard-specific element
    page.wait_for_selector("h6:has-text('Dashboard')", timeout=5000)
    assert page.locator("h6:has-text('Dashboard')").is_visible()

    page.screenshot(path="images/playwright_successful_login.png")


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
    page.screenshot(path="images/login_failed.png")

    # Optional: confirm URL has not changed to dashboard
    assert "/dashboard" not in page.url


def test_forgot_password_redirect(page):
    # Step 1: Navigate to login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Click "Forgot your password?" link
    forgot_password_link = page.get_by_text("Forgot your password?")
    forgot_password_link.click()

    # Step 3: Wait for the reset password page
    page.wait_for_selector("h6:has-text('Reset Password')", timeout=5000)
    page.locator("input[name='username']").fill("Admin")
    page.click("button[type='submit']")
    page.wait_for_selector("h6:has-text('Reset Password link sent successfully')", timeout=5000)



    # Step 4: Validate that the page URL contains "requestPasswordResetCode"
    # assert "requestPasswordResetCode" in page.url

    # Step 5: Optional: take a screenshot for verification
    page.screenshot(path="images/forgot_password_page.png")

