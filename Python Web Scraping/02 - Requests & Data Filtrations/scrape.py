from bs4 import BeautifulSoup
import requests

# url endpoint GET request ---> Missoula Country Jail Roster.
jail_roster_html = requests.get('https://webapps.missoulacounty.us/jailroster/Inmates')
# Create an instance of beautiful soup
soup = BeautifulSoup(jail_roster_html.content, 'lxml')
table = soup.find('table')

table_rows = table.find_all('tr')

# Find the table data
for tr in table_rows: 
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
