# Screenshots of site issues when testing locally

See these screenshots and html-files for examples of issues that occur when testing the feat/field-museum-theme branch locally

local link | html | screenshot
-|-|-
  `localhost:8080/` | example_Home_Stacks.html | screenshot_Home_Stacks.png
  `localhost:8080/brand/colors` | example_Colors_Stacks.html | screenshot_Colors_Stacks.png
  `localhost:8080/brand/logo` | example_Logo_Stacks.html | screenshot_Logo_Stacks.png
  `localhost:8080/brand/typography` | example_Typography_Stacks.html | screenshot_Typography_Stacks.png


# Issues:

## 1. Text and other elements are overlapping each other on the page
See the brand pages
- screenshot_Colors_Stacks.png
- screenshot_Logo_Stacks.png
- screenshot_Typography_Stacks.png

Menu-text and sidebar-navigation text is overlapping body text.
The page footer (pale gray banner) is also floating in the midding of the page, overlapping text content

## 2. Basic styling is missing
Font, colors, and other page-styling did not appear to be respecting css styling.

## 3. Home page is displaying a github login screen
See screenshot_Home_Stacks.png

## 4. Missing pages
Trying to access some pages returns an error -- e.g. localhost:8080/product/components should render, but instead returns a blank page with the error: "Cannot GET /product/components"