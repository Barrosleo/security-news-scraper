import requests
from bs4 import BeautifulSoup

# Web Scraping Function
def scrape_security_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')  # Adjust this based on the website's structure
        news = []
        for article in articles:
            title = article.find('h2').get_text()  # Adjust this based on the website's structure
            link = article.find('a')['href']
            news.append({'title': title, 'link': link})
        return news
    else:
        print(f"Failed to retrieve content from {url}")
        return []

# Test the Function
if __name__ == "__main__":
    urls = [
        "https://example.com/security-news",  # Replace with actual URLs
        "https://anotherexample.com/security"
    ]
    for url in urls:
        news = scrape_security_news(url)
        for item in news:
            print(f"Title: {item['title']}\nLink: {item['link']}\n")
