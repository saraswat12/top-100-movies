from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

movie_web = response.text

soup = BeautifulSoup(movie_web, "html.parser")

names = soup.find_all(name="h3", class_="title")
#print(names)
movie_name = []
for name in names:
    movie_name.append(name.getText())

movies = movie_name[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for m in movies:
        file.write(f"{m}\n")










#
# for item in movie_name:
#     original_list = item.split()
#     integer_part = int(original_list[0].replace(')', ''))
#     starting_part = ' '.join(original_list[1:])
#
#     original_list = [integer_part, starting_part]
#
#     print(original_list)
# #updated = [i.replace(')', "")  for i in original_list]
#
# #print(updated[0])














#
# articles = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []
# for articale_tag in articles:
#     article_text = articale_tag.getText()
#     article_texts.append(article_text)
#     article_link = articale_tag.get("href")
#     article_links.append(article_link)
#
#
# print(article_links)
#
#
#print(soup.title)
#
# all_anch = soup.find(name="span", class_="titleline")
# print(all_anch.find("a").get("href"))
#print(all_anch.get("a href"))
#link = soup.get("href")
#print(link)



# all_anch = soup.find_all(name="a")
# for p in all_anch:
#     print(p.getText())
# #
# anchor = soup.find(name="span a", class_="titleline")
# print(anchor)

# import lxml

# with open("website.html", encoding="utf-8") as file:
#     content = file.read();
#
# soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
#print(soup.prettify())
# give first anchor tag
#print(soup.a)
#print(soup.find_all(name="p"))

# all_para = soup.find_all(name="a")
# for p in all_para:
#     #print(p.getText())
#     print(p.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# #head3 = soup.find(name="h3", class="heading")
# # give error cause class is reserved word so
# head3 = soup.find(name="h3", class_="heading")
# print(head3)
