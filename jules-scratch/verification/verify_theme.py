import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the index.html file
        # The script is run from the root of the repo
        file_path = os.path.abspath("packages/stacks-docs/_site/index.html")

        page.goto(f"file://{file_path}")
        page.screenshot(path="jules-scratch/verification/homepage.png")
        browser.close()

if __name__ == "__main__":
    run()