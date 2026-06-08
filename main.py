from playwright.sync_api import sync_playwright
import csv

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        with open("data.csv","w",newline="",encoding="UTF-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["book_title","book_link","price","stock","rating","description"])

            start_page = int(input("start page: "))
            end_page = int(input("end page: "))

            for page_num in range(start_page,end_page + 1):

                page.goto(f"https://books.toscrape.com/catalogue/page-{page_num}.html")
                
                books = []

                items = page.locator("article.product_pod").all()
                for item in items:

                    book_title = item.locator("h3 a").get_attribute("title")
                    book_link = item.locator("h3 a").get_attribute("href")
                    full_link = "https://books.toscrape.com/catalogue/" + book_link

                    books.append([book_title,full_link])
                
                for book_title,book_link in books:
                    page.goto(book_link)
                    
                    x_items = page.locator(".product_main")

                    price = x_items.locator("p.price_color").text_content()
                    stock = x_items.locator("p.instock").text_content()
                    rating = x_items.locator("p.star-rating").get_attribute('class').split()[-1]
                    description = page.locator("#product_description + p").text_content()

                    writer.writerow([book_title,book_link,price,stock,rating,description])

    
        browser.close()
run()
