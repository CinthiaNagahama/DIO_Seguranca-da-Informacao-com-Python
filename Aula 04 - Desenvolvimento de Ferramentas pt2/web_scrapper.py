from bs4 import BeautifulSoup
import requests

site = requests.get(input("Insira o endereço do site a ser verificado (não esqueça de inserir o http:// ou https://): ")).content

soup = BeautifulSoup(site, "html.parser")

print(soup.prettify())

print(soup.title.string)

print(soup.find("admin"))