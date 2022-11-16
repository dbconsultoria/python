# https://www.geeksforgeeks.org/how-to-take-screenshot-using-selenium-in-python/
# importing webdriver from selenium
from selenium import webdriver
from PIL import Image

# Here Chrome will be used
driver = webdriver.Chrome()

# URL of website
url = "https://www.uol.com.br"

# Opening the website
driver.get(url)

driver.save_screenshot(R"C:\\Users\\Rodrigo\\Documents\\GitHub\\python\\image.png")


# Loading the image
image = Image.open("C:\\Users\\Rodrigo\\Documents\\GitHub\\python\\image.png")

# Showing the image
image.show()
