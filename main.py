import requests
from bs4 import BeautifulSoup as bs
import random

url = 'https://httpbin.org/headers'

def get_user_agent(url):
  r = requests.get(url)
  soup = bs(r.content, "html.parser")
  user_agent_tag = soup.find_all('td', attrs={'class': 'blob-code blob-code-inner js-file-line'})
  user_agent_list = [user_agent.text for user_agent in user_agent_tag]
  return user_agent_list

def get_free_proxies(url):
  r = requests.get(url)
  soup = bs(r.content, "html.parser")
  div_table = soup.find_all('div', attrs={'class': 'fpl-list'})
  
  tr_list = []

  for div in div_table:
    tr_list = div.find_all('tr')
  
  proxies = []

  for tr in tr_list[1:]: # skip th
    td_list = tr.find_all('td')
    proxies.append(td_list[0].text + ':' + td_list[1].text)
  
  return proxies

def webRequest(url, proxy, user_agent):
  headers = {
    'User-Agent': user_agent
  }
  try:
    web_html = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=3)
    soup = bs(web_html.content, "html.parser")
    title = soup.find('title')
    print(title.text)
    return False
  except:
    return True
  
    
      

user_agent_list = get_user_agent('https://gist.github.com/pzb/b4b6f57144aea7827ae4')
proxies_list = get_free_proxies('https://free-proxy-list.net/')


while webRequest('https://www.jakelonline.com/main', random.choice(user_agent_list), random.choice(proxies_list)):
  print('Proxy Error')







