import requests
import string
import json
import csv

# Set the search query and the number of results to collect
query = "site:youtube.com openinapp.co"
num_results = 10000

# Set the ScrappingBee API key and URL to use for making requests
api_key = "your_scrappingbee_api_key"
base_url = f"https://app.scrapingbee.com/api/v1/?api_key={api_key}&url="

# Make the HTTP request with the user-agent string and get the response
channel_urls = []
for start in range(0, num_results, 10):
    url = f"{base_url}https://www.google.com/search?q={query}&num=10&start={start}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        for result in soup.select("div.g > div.rc > div.r > a"):
            href = result.get("href")
            if href.startswith("/url?q=https://www.youtube.com/channel/"):
                channel_urls.append(href.split("/url?q=")[1].split("&")[0])
    else:
        print(f"Error: {response.status_code}")

# Output the results as JSON
with open("youtube_channels.json", "w") as f:
    json.dump(channel_urls, f)

# Output the results as CSV
with open("youtube_channels.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Channel URL"])
    for url in channel_urls:
        writer.writerow([url])
