from collections import defaultdict

# Define the function to generate HTML for grouped data
def generate_html(groups):
    html_content = ''  # Initialize with empty string
    
    for letter, items in sorted(groups.items()):
        html_content += '<div class="alphabet">\n'
        html_content += '<div>\n'
        
        # Add the dynamic heading
        html_content += f'<h3>{letter}</h3>\n'
        
        # Add the brands list
        html_content += '<div class="brands">\n'
        for item in items:
            html_content += f'<span>{item}</span>\n'
        html_content += '</div>\n'
        
        # Close the divs
        html_content += '<hr>\n'
        html_content += '</div>\n'
        html_content += '</div>\n'
    
    return html_content

def fetch_data_from_console():
    print("Enter the brands, one per line. Type 'done' when you are finished:")
    groups = defaultdict(list)
    while True:
        line = input()
        if line.lower() == 'done':
            break
        if line.strip():
            # Determine the starting letter
            first_letter = line[0].upper()
            groups[first_letter].append(line.strip())
    return groups

# Fetch data from console
groups = fetch_data_from_console()

# Generate HTML from grouped data
html_code = generate_html(groups)

# Optionally, you can write the HTML code to a file
with open("output.html", "w") as file:
    file.write(html_code)

print("HTML has been generated and saved to 'output.html'.")
