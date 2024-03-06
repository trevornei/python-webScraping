from bs4 import BeautifulSoup

# pip install lxml for more robust parsing of the HTML

# read the home.html file, name the file: 
with open('home.html', 'r') as html_file: 
    content = html_file.read()
    print(content)

