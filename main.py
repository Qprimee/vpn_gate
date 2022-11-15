import requests
from bs4 import BeautifulSoup

URL = "https://www.vpngate.net/en/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

vpn_elements = soup.find_all("td", class_="vg_table_row_1")
vpn_ip = vpn_elements[31].find("span");
print(vpn_ip.text)