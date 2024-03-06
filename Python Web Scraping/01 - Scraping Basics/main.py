from bs4 import BeautifulSoup

# pip install lxml for more robust parsing of the HTML

# read the home.html file, name the file: 
with open('home.html', 'r') as html_file: 
    content = html_file.read()
    
    # create new instance of the soup library
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # print the h5 tags to the terminal
    # tags = soup.find('h5')
    # print(tags)


    # Print all h5 tags
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    # Prints all of the course titles.
    # course_cards = soup.find_all('div', class_='card')
    # for course in course_cards: 
    #     print(course.h5.text)
    
    
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards: 
        # print course name and price
        course_name = course.h5.text
        course_price = course.a 

        print(course_name, course_price)