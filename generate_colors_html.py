import re

def parse_color_palette(markdown_content):
    """Parses the color palette markdown file and returns a dictionary of colors."""
    colors = {}
    current_category = None

    for line in markdown_content.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith('**') and line.endswith('**'):
            current_category = line.strip('**').lower().replace(' ', '-')
            colors[current_category] = []
        elif ':' in line and line.startswith('color/'):
            parts = line.split(':')
            name_parts = parts[0].split('/')
            name = name_parts[-1].strip()
            hex_code = parts[1].strip().split('–')[0].strip().replace('\\', '')

            # Handle names with descriptions
            if '–' in parts[1]:
                description = parts[1].split('–')[1].strip()
                name = f"{name} – {description}"

            if current_category:
                colors[current_category].append({'name': name, 'hex': hex_code})

    return colors

def generate_color_html(colors):
    """Generates HTML for the color palette."""
    html = """---
layout: page
title: Colors
description: This palette defines the Field Museum’s core brand and functional colors for digital use. Each color has been tested for accessibility and is organized into categories that support clear, consistent visual communication across digital platforms. Use these colors as the foundation for UI elements, backgrounds, text, and emphasis, ensuring contrast guidelines are met for an inclusive user experience.
---
"""

    for category, color_list in colors.items():
        if not color_list:
            continue
        html += f'<section class="stacks-section">\n'
        html += f'    {{% header "h2", "{category.replace("-", " ").title()}" %}}\n'
        html += '    <div class="d-flex flex__allitems4 g32 ff-row-wrap">\n'
        for color in color_list:
            text_color = 'white' if int(color['hex'].lstrip('#'), 16) < 0x888888 else 'black'
            html += f"""        <div class="flex--item s-card wmn2 bs-sm p0 mb24" style="background-color: {color['hex']}; color: {text_color};">
            <div class="h96 mln1 mrn1 mtn1 btr-sm" style="background:{color['hex']}"></div>
            <div class="p12">
                <h3 class="fs-body3 lh-sm mb12">{color['name']}</h3>
                <div class="fs-body1 bt bc-white py8 d-flex">
                    <span>Hex</span>
                    <span class="stacks-code js-clipboard h:bg-black-225 c-pointer ml-auto">{color['hex']}</span>
                </div>
            </div>
        </div>
"""
        html += '    </div>\n'
        html += '</section>\n\n'

    html += """<!-- Additional javascript -->
<script src="{{ "/assets/dist/entry.brand.colors.js" | url }}" defer></script>

{% include 'toast-clipboard.html' %}
"""
    return html

if __name__ == "__main__":
    with open('fmnh_assets/fm_brand_color_palette.md', 'r') as f:
        markdown_content = f.read()

    parsed_colors = parse_color_palette(markdown_content)
    html_content = generate_color_html(parsed_colors)

    with open('packages/stacks-docs/brand/colors.html', 'w') as f:
        f.write(html_content)

    print("Successfully generated colors.html")
