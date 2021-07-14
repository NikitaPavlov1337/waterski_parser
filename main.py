import requests
from bs4 import BeautifulSoup
import xlsxwriter


rating_list = ['Women','Men','U21_Women','U21_Men','U17_Women','U17_Men','U14_Women',
               'U14_Men','U12_Women','U12_Men','U10_Women','U10_Men','Vet_Women','Vet_Men',
               'Vet2_Women','Vet2_Men','Vet3_Women','Vet3_Men','Vet4_Women','Vet4_Men']

def get_table():
    workbook = xlsxwriter.Workbook('test.xlsx')
    base_url = 'http://www.iwwfed-ea.org/classic/rl2021/eame/index.php?page=RL&categ='
    for rating in rating_list:
        url = base_url+rating
        response = requests.get(url).text
        parser = BeautifulSoup(response,"lxml")
        table = parser.find("table",attrs={"class": "Data"})
        headings = []
        for th in table.find_all("th"):
            headings.append(str(th.text))
        content = []
        for row in table.find_all("tr"):
            if not row.find_all("th"):
                content.append([element.text for element in row.find_all('td')])
        for list in content:
            list.remove('\xa0')


        worksheet = workbook.add_worksheet(f'{rating}')

        for index, word in enumerate(headings):
            worksheet.write_string(0,index,word)
        for row_num, row_data in enumerate(content):
            for col_num, col_data in enumerate(row_data):
                worksheet.write_string(row_num+1, col_num, col_data)

    workbook.close()


if __name__ == '__main__':
    get_table()