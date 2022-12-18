#packages imported to help in scraping
import requests
from bs4 import BeautifulSoup
#packages to connect to db and add/remove/update data
import pymysql
pymysql.install_as_MySQLdb()
import mysql.connector



#db = mysql.connector.connect(host="34.176.191.95", user="root", passwd="Davito1989.", database ="paris")
db = mysql.connector.connect(host="localhost", user="root", passwd="", database ="lapolar")

# cursor to read the query results
cur = db.cursor()

 #truncamos la tabla para obtener nuevos links
#query="TRUNCATE paris.accesorios_computacion_details"
#cur.execute(query)
 
pagina = 0
while pagina <= 1800:
#se especifica catagoria de television
 url = "https://www.lapolar.cl/hogar/?start=%s&sz=36"%pagina
 #print(url)

 #connecting to the db with default values and table created

 #base url to append specific mobile phone page links
 base_url = "https://www.lapolar.cl"
 #creating url1[] array to store url's
 url1=[0]*1000
 #x here corresponds to the particular page in the search results eg if x=1,then it is appended to the "url" string to display the first page
 x=1
 #traversing x number of pages for retreiving all link in the x-th page
 
 while x <= 1:
 
  query = str(x)
  #Concept used here is simple;The url has the base url of the flipkart mobile section with query having the page number appended in the end. Therefore, we get the display results of the x-th page
  url1[x] = url + query
  source = requests.get(url1[x]).content
  #cooking the soup/parsing html into DOM
  soup = BeautifulSoup(source,'html.parser')    

    #extracting via tags , a function present in "Beautiful soup" 
  links = soup.findAll("input",{"class":"js-pdp-url"})
    #links contains all the links present contained in the <a> tag 
    #print("coooooooooorteeeeeeeeeee")

  #print(links)
  #count = 1
  for a in links:
   #print(count)
   if "https://www.lapolar.cl" in a.get('value'):
    url_final = (a.get('value')[20:])
    all_links = base_url+url_final
    #print("====links====",a.get('href'))
    #print(url_final)
    query="select count(urls) from hogar_details where urls='%s'"%all_links
    #executing query with the cursor
    #print(query)
    cur.execute(query)
    a=cur.fetchall()
    #print(a)
    for row in a:
     #URLs being stored in the first column of the table is being fetched
     link=row[0]
     #print(link)
    
     ###reviso si el link existe en la base de datos
     if int(link) == 0:
      #print (link)
      query= "insert into hogar_details(urls) values('%s')"%(all_links)
      print(query)
      cur.execute(query)
      db.commit()
      
      
   else: 

    all_links = base_url+a.get('value')
    #print("====links====",a.get('value'))
    #print(url_final)
    query="select count(urls) from hogar_details where urls='%s'"%all_links
    #executing query with the cursor
    #print(query)
    cur.execute(query)
    a=cur.fetchall()
    #print(a)
    for row in a:
     #URLs being stored in the first column of the table is being fetched
     link=row[0]
     #print(link)
    
     ###reviso si el link existe en la base de datos
     if int(link) == 0:
      #print (link)
      query= "insert into hogar_details(urls) values('%s')"%(all_links)
      print(query)
      cur.execute(query)
      db.commit()  
      
   #count= count +1
  x =x+1
 pagina = pagina + 36

db.close()
