import requests
from bs4 import BeautifulSoup

url = input("Enter website URL (with https://): ")

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Page title
print("\nPage Title:")
print(soup.title.text if soup.title else "No title found")

# All links
print("\nLinks found:")
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)
