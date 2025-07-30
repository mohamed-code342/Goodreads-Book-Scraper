from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

def initialize_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.goodreads.com/")
    time.sleep(2)
    return driver

def search_books(driver, user_input):
    Books_list = []
    search_box = driver.find_element(By.ID,'sitesearch_field')
    search_box.send_keys(user_input)
    search_box.submit()
    time.sleep(3)
    
    for i in range(11):
        time.sleep(5)
        books= driver.find_elements(By.XPATH, "//tr[@itemtype='http://schema.org/Book']")
        for book in books:
            try:
                title=book.find_element(By.XPATH, ".//a[@class='bookTitle']").text.strip()
            except:
                title='No title found'
            try:
                author=book.find_element(By.XPATH, ".//a[@class='authorName']").text.strip()
            except:
                author='No author found'
            try:
                pub_info = book.find_element(By.CSS_SELECTOR, "span[class='greyText smallText uitext']").text
                pub_parts = pub_info.split('—')
                puplication_year = 'No publication year found'
                for part in pub_parts:
                    if 'published' in part.lower():
                        puplication_year = part.lower().replace('published', '').strip()
                        break
            except:
                puplication_year = 'No publication year found'

            try:
                rating=book.find_element(By.XPATH, ".//span[@class='minirating']").text.strip()
            except:
                rating='No rating found'
            try:
                edition=book.find_element(By.CSS_SELECTOR, "a[class='greyText']").text.strip()
            except: 
                edition='No edition found'
            try:
                link=book.find_element(By.XPATH, ".//a[@class='bookTitle']").get_attribute('href')
            except:
                link='No link found'

            Books_list.append({
                'title': title,
                'author': author,
                'puplication_year': puplication_year,
                'rating': rating,
                'edition': edition,
                'link': link
            })
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a[class='next_page']")
            if "disabled" in next_button.get_attribute("class"):
                break
            else:
                next_button.click()
        except:
            print("No more pages found.")
            break

    return Books_list

def print_books(Books_list):
    if not Books_list:
        print("No books found to save!")
        return
        
    path = "C:\\Users\\maham\\Downloads\\Selenium\\Books_details.csv"
    keys = Books_list[0].keys()
    with open(path,'w',newline='',encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f,fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(Books_list)
    print("Books details are saved in Books_details.csv")

if __name__ == "__main__":
    try:
        user_input = input("Enter book category to search: ")
        driver = initialize_driver()
        books = search_books(driver, user_input)
        print_books(books)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()