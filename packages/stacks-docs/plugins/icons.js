const { Icons, Spots } = require("@stackoverflow/stacks-icons");
const fs = require("fs/promises");

function modifySvg(content, type, name, classes, dimension) {
  var defaultClasses = `svg-${type} ${type}${name}`;

  if (!content) {
    return `<span class="fc-danger">Invalid ${type}: ${name}</span>`;
  }

  // If we have classes, add them
  if (classes != null) {
    content = content.replace(defaultClasses, defaultClasses + " " + classes);
  }

  // If we need to change the size, do that too
  if (dimension != null) {
    content = content.replace('width="18" height="18"', 'width="' + dimension + '" height="' + dimension + '"');
  }

  return content;
}

module.exports = {
  configFunction(eleventyConfig) {
    // Icon shortcode
    eleventyConfig.addLiquidShortcode("icon", function(name, classes, dimension) {
        const iconNameMap = {
            "Clear": "close",
            "Search": "search",
            "GitHub": "code",
            "Theme": "palette",
            "Pencil": "edit",
            "Trash": "delete",
            "Alert": "warning",
            "Checkmark": "done",
            "ChevronDown": "expand_more",
            "ChevronUp": "expand_less",
            "ChevronLeft": "chevron_left",
            "ChevronRight": "chevron_right",
            "Plus": "add",
            "Minus": "remove",
            "ArrowUp": "arrow_upward",
            "ArrowDown": "arrow_downward",
            "ArrowLeft": "arrow_back",
            "ArrowRight": "arrow_forward",
            "Help": "help_outline",
            "Info": "info",
            "Link": "link",
            "Copy": "content_copy",
            "Clock": "history",
            "Calendar": "calendar_today",
            "Location": "location_on",
            "Achievements": "emoji_events",
            "Reputation": "military_tech",
            "Users": "group",
            "User": "person",
            "Question": "help",
            "Answer": "question_answer",
            "Comment": "comment",
            "Tag": "sell",
            "Gear": "settings",
            "Star": "star",
            "Bell": "notifications",
            "ThumbsUp": "thumb_up",
            "ThumbsDown": "thumb_down",
            "EllipsisHorizontal": "more_horiz",
            "EllipsisVertical": "more_vert",
        };

        const materialIconName = iconNameMap[name] || name.toLowerCase().replace(/\s/g, '_');

        let style = "";
        if (dimension != null) {
            style = `font-size: ${dimension}px;`;
        }

        // Base classes for Material Symbols
        let baseClasses = "material-symbols-sharp";

        // Add any additional classes passed in
        if (classes) {
            baseClasses += ` ${classes}`;
        }

        return `<span class="${baseClasses}" style="${style}">${materialIconName}</span>`;
    });

    // Spot shortcode
    eleventyConfig.addLiquidShortcode("spot", function(name, classes, dimension) {
      var svg = Spots["Spot" + name];
      return modifySvg(svg, "spot", name, classes, dimension);
    });

    // embed svgs in the assets folder
    eleventyConfig.addLiquidShortcode("embed", async function(name, classes) {
      const file = await fs.readFile(`assets/img/icons/${name}.svg`, "utf8");
      return modifySvg(file, "icon", name, classes, null);
    });
  }
}
