import requests
from operator import itemgetter

def get_sorted_regions():
    url = 'https://api.worldbank.org/v2/region?format=json'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            regions = data[1]  # The actual data is in the second item of the response JSON
            return sorted(regions, key=itemgetter('iso2code'))[:5]
        else:
            print(f"Failed to retrieve data: Status code {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def create_html_file(sorted_regions):
    html_content = "<html><body><h1>Sorted Regions</h1><ul>"
    
    for region in sorted_regions:
        html_content += f"<li>{region['name']} - {region['iso2code']}</li>"
    
    html_content += "</ul></body></html>"

    try:
        with open("sorted_regions.html", "w") as file:
            file.write(html_content)
        print("HTML file created successfully.")
    except Exception as e:
        print(f"Error writing file: {e}")

sorted_regions = get_sorted_regions()

if sorted_regions:
    create_html_file(sorted_regions)
else:
    print("No data to create HTML file.")

