from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_daily_news():
    # Path to your WebDriver. Make sure to change this according to your system's configuration
    today = []
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # URL of the news website you want to scrape
    news_url = 'https://www.thehindu.com/news/national/'  # Replace this with the URL of the news website you want to scrape

    # Navigate to the news website
    driver.get(news_url)

    # Find the elements containing the news headlines
    # Replace these locators with the specific ones on the website you're scraping
    headlines = driver.find_elements(By.XPATH, '/html/body/section[3]') 

    # Extract and print the headlines
    for headline in headlines:
        
        data= headline.text.split('\n')
        for st in data:
            if len(st)> 25:
                 today.append(st)
              
    with open("dailynews.txt", "w") as filenews:
                        for item in today:
                            filenews.write(item+"\n")
    # Close the browser
    
    
    driver.quit()

# Call the function to get daily news headlines
get_daily_news()
