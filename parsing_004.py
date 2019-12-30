import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
   r = requests.get(url)
   if r.ok: #200
      return r.text
   print(r.status_code)

def refind_cy(s):
   return s.split(' ')[-1]#последний элемент по индексу -1

def write_csv(data):
   with open('cmd.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow((data['name'],
                      data['url']))


def get_data(html):
   soup = BeautifulSoup(html, 'lxml')
   lis = soup.find_all('a', class_='article-title')
   
   for li in lis:
      try:
         name = li.find('h2').text
      except:
         name = ''
      try:
         url = 'https://kolobok.ua'+ li.get('href')
      except:
         url = ''

      data = {
         'name':name,
         'url':url       
         }
      write_csv(data)
   
   print(len(lis))
 

def main():
   pattern = 'https://kolobok.ua/search/index?s=%D0%BF%D0%B0%D0%BC%D0%BF%D0%B5%D1%80%D1%81%D1%8B&page={}'
   for i in range(1, 4):
      url = pattern.format(str(i))
      get_data(get_html(url))

if __name__ == '__main__':
   main()
