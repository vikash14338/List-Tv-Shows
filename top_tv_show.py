import requests
from bs4 import BeautifulSoup

url='https://www.imdb.com/chart/toptv/'
data=requests.get(url)
html=data.text #get html file as text
html_soup=BeautifulSoup(html,'html.parser')
#containers store all tbody whose class name is lister-list
containers=html_soup.findAll("tbody",{"class":"lister-list"})
#print(len(containers))
list_data=containers[0].findAll("tr")
print(len(list_data))
file_name="./top_tv_show.csv"
file=open(file_name,"w+")
header="Id,Title,Imdb_Rating\n"
file.write(header)
for i in range(250):
    t_data=list_data[i];
    title=t_data.find("td",{"class":"titleColumn"}).text[12:]
    rating=t_data.find("td",{"class":"ratingColumn imdbRating"}).text
    rating=rating.replace("\n","")
    title=title.replace(",","-")
    title=title.replace(" ","")
    title=title.replace("\n","")
    file.write(str(i+1)+","+title+","+rating+"\n")
file.close
    






