from filehandler import FileHandler
from webscrapper import WebScrapper

webscrapper = WebScrapper()
file_handler = FileHandler(webscrapper)

if __name__ == "__main__":
    try:
        webscrapper.scroll()
        webscrapper.write_csv()

        file_handler.connect()
        file_handler.send_file()
        webscrapper.delete_csv()
    except KeyboardInterrupt:
        print("Closing Application...")