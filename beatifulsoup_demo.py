from bs4 import BeautifulSoup


with open(file="website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for i in all_anchor_tags:
#     # print(i.getText())
#     print(i.get("href"))

# print(soup.find(name="h1",id="name"))

# print(soup.find(name="h3",class_="heading"))

company_url = soup.select_one("p a")
# print(company_url)

name = soup.select(".heading")
print(name)
