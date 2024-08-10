from collections import defaultdict
import urllib.parse
import re

# Define the function to generate HTML for grouped data
def generate_html(groups):
    html_content = ''  # Initialize with empty string
    
    for letter, items in sorted(groups.items()):
        html_content += f'<div class="alphabet" id="{letter}">\n'
        html_content += '<div>\n'
        
        # Add the dynamic heading
        html_content += f'<h3>{letter}</h3>\n'
        
        # Add the brands list
        html_content += '<div class="brands">\n'
        for item in items:
            html_content += f'<a href="{item["link"]}">{item["name"]}</a>\n'
        html_content += '</div>\n'
        
        # Close the divs
        html_content += '<hr />\n'
        html_content += '</div>\n'
        html_content += '</div>\n'
    
    return html_content

def format_brand_name(name):
    # Replace specific characters
    name = name.replace('.', '-')  # Replace . with -
    name = name.replace('&', '-')  # Replace & with -
    name = name.replace("'", '')   # Remove '
    name = name.replace('!', '')   # Remove !

    # Replace spaces with hyphens
    name = name.replace(' ', '-')

    # Replace multiple consecutive hyphens with a single hyphen
    name = re.sub(r'-+', '-', name)
    
    # Convert to lowercase
    name = name.lower()
    
    # Strip any leading or trailing hyphens (optional but useful)
    name = name.strip('-')
    
    return name

def fetch_data_from_console():
    base_url = "https://theperfumebox.com/collections/"
    print("Enter the brand names. Type 'done' when you are finished:")
    groups = defaultdict(list)
    while True:
        line = input()
        if line.lower() == 'done':
            break
        if line.strip():
            brand_name = line.strip()
            # Format the brand name
            formatted_name = format_brand_name(brand_name)
            # Create the full URL
            full_url = urllib.parse.urljoin(base_url, formatted_name)
            first_letter = brand_name[0].upper()
            groups[first_letter].append({"name": brand_name, "link": full_url})
    return groups

# Fetch data from console
groups = fetch_data_from_console()

# Generate HTML from grouped data
html_code = generate_html(groups)

# Optionally, you can write the HTML code to a file
with open("output.html", "w") as file:
    file.write(html_code)

print("HTML has been generated and saved to 'output.html'.")
