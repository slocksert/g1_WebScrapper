from filehandler import FileHandler
from webscraper import WebScraper

webscraper = WebScraper()
file_handler = FileHandler(webscraper)

if __name__ == "__main__":
    try:
        webscraper.scroll()
        webscraper.write_csv()

        file_handler.connect()
        file_handler.send_file()
        webscraper.delete_csv()
    except KeyboardInterrupt:
        print("Closing Application...")