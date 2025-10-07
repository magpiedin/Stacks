from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Navigate to the homepage and take a screenshot
    page.goto("http://localhost:8080")
    page.screenshot(path="jules-scratch/verification/homepage.png")

    # Navigate to the colors page and take a screenshot
    page.goto("http://localhost:8080/brand/colors")
    page.screenshot(path="jules-scratch/verification/colors.png")

    # Navigate to the logo page and take a screenshot
    page.goto("http://localhost:8080/brand/logo")
    page.screenshot(path="jules-scratch/verification/logo.png")

    # Navigate to the typography page and take a screenshot
    page.goto("http://localhost:8080/brand/typography")
    page.screenshot(path="jules-scratch/verification/typography.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
