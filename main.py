import requests
from bs4 import BeautifulSoup
import xlsxwriter


def get_table(url):
    response = requests.get(url).text
    parser = BeautifulSoup(response,"lxml")
    data = {}
    table = parser.find("table",attrs={"class": "Data"})

    headings = []
    for th in table.find_all("th"):
        headings.append(str(th.text))
    content = []
    for row in table.find_all("tr"):
        if not row.find_all("th"):
            content.append([element.text for element in row.find_all('td')])
    print(headings)
    print(content)
    for word in headings:
        print(type(word))

    rown = 0
    column = 0
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()
    for index, word in enumerate(headings):
        worksheet.write_string(0,index,word)
    for row_num, row_data in enumerate(content):
        for col_num, col_data in enumerate(row_data):
            worksheet.write_string(row_num+1, col_num, col_data)

    workbook.close()



get_table('http://www.iwwfed-ea.org/classic/rl2021/eame/index.php?page=RL&categ=Men')