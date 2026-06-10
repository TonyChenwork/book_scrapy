from playwright.sync_api import sync_playwright
import csv


BASE_URL = "https://books.toscrape.com/catalogue/"


def get_book_links(page, page_num):
    page.goto(f"{BASE_URL}page-{page_num}.html", wait_until="domcontentloaded")

    books = []
    items = page.locator("article.product_pod").all()

    for item in items:
        book_title = item.locator("h3 a").get_attribute("title")
        book_link = item.locator("h3 a").get_attribute("href")
        full_link = BASE_URL + book_link
        books.append([book_title, full_link])

    return books


def scrape_book_detail(page, book_title, book_link):
    page.goto(book_link, wait_until="domcontentloaded")

    x_items = page.locator(".product_main")

    price = x_items.locator("p.price_color").text_content().strip()
    stock = x_items.locator("p.instock").text_content().strip()
    rating = x_items.locator("p.star-rating").get_attribute("class").split()[-1]

    if page.locator("#product_description + p").count() > 0:
        description = page.locator("#product_description + p").text_content().strip()
    else:
        description = ""

    return [book_title, book_link, price, stock, rating, description]


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            start_page = int(input("start page: "))
            end_page = int(input("end page: "))
        except ValueError:
            print("Please enter valid numbers.")
            browser.close()
            return

        if start_page < 1 or end_page < start_page or end_page > 50:
            print("Invalid page range. Please enter pages between 1 and 50.")
            browser.close()
            return

        with open("data.csv", "w", newline="", encoding="UTF-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([
                "book_title",
                "book_link",
                "price",
                "stock",
                "rating",
                "description"
            ])

            for page_num in range(start_page, end_page + 1):
                print(f"Scraping list page {page_num}...")

                books = get_book_links(page, page_num)

                for book_title, book_link in books:
                    try:
                        row = scrape_book_detail(page, book_title, book_link)
                        writer.writerow(row)
                        print(f"Scraped: {book_title}")

                    except Exception as e:
                        print(f"Failed: {book_title} | {book_link} | Error: {e}")

        browser.close()


run()