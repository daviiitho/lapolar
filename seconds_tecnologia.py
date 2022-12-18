#packages imported to help in scraping
import requests
from bs4 import BeautifulSoup
#packages to connect to db and add/remove/update data
import pymysql
pymysql.install_as_MySQLdb()
import mysql.connector
import re
from datetime import datetime
import codecs


encabezados = {
  "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

def telegram_bot_sendtext(bot_message):
            bot_token  = '5213011783:AAFrz4Zxl04baZyFVt9CXHp6yAackLSaQRQ'
            bot_chatID = '938945400'
            idGrupo = '-1001798489895'
            enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + idGrupo + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(enviar_text)
            #creating arrays
            column_name = []
            #displaying the already present columns in the table
            cur.execute("SHOW COLUMNS FROM tecnologia_details")
            b=cur.fetchall()
            return response.json()
            
            
def telegram_bot_sendtext_mayor70(bot_message):
            bot_token  = '5213011783:AAFrz4Zxl04baZyFVt9CXHp6yAackLSaQRQ'
            bot_chatID = '938945400'
            idGrupo = '-1001795793832'
            enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + idGrupo + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(enviar_text)
            #creating arrays
            column_name = []
            #displaying the already present columns in the table
            cur.execute("SHOW COLUMNS FROM tecnologia_details")
            b=cur.fetchall()
            return response.json()     

def telegram_bot_sendtext_tecnologia(bot_message):
            bot_token  = '5213011783:AAFrz4Zxl04baZyFVt9CXHp6yAackLSaQRQ'
            bot_chatID = '938945400'
            idGrupo = '-1001690235284'
            enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + idGrupo + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(enviar_text)
            #creating arrays
            column_name = []
            #displaying the already present columns in the table
            cur.execute("SHOW COLUMNS FROM tecnologia_details")
            b=cur.fetchall()
            return response.json()      

#connecting to the db with default values and table created
#db = mysql.connector.connect(host="localhost", user="root", passwd="", database ="lapolar")
db = mysql.connector.connect(host="lapolar.cnh6u52zzc0v.us-east-1.rds.amazonaws.com", user="admin", passwd="Davito1989", database ="lapolar")

#db = mysql.connector.connect(host="34.176.191.95", user="root", passwd="Davito1989.", database ="paris")
#cursor to read the query results
cur = db.cursor()
#this is the format of forming and executing queries using mySQLdb , see documentation in 'readme' file for further knowledge
query="select urls,status, oferta from tecnologia_details"
#executing query with the cursor
print(query)
cur.execute(query)
a=cur.fetchall()
for row in a:
    #URLs being stored in the first column of the table is being fetched
    link= row[0]
    #stautus =1/0 , where flag 1 means it has been crawled for data and 0 flag means its yet to be checked;Default value in DB is 0
    status=row[1] 
    ofertabd=row[2]
    #tarjetabd=row[3]

    #print("\nlink=%s\nstatus=%s\n"%(link,status))
    #creating arrays
    column_name = []
    #displaying the already present columns in the table
    
        #print(column_name)
    #obtaining each links and crawling specs only if status is 0
    #print("jkajajjaj")
    #try:
    #print(status)
    respuesta = requests.get(link, headers=encabezados)

    #soup = BeautifulSoup(respuesta.text)
    #soup = BeautifulSoup(respuesta,'html.parser')
    soup = BeautifulSoup(respuesta.content, "html.parser")

    #precio = soup.find_all('span',class_="price-span internet-price")
    #print(precio)

    #for pregunta in precio:
    #try:








    ############precio interneeeeettttttttt####

    if soup.find('span',class_="price-value" )  != None and soup.find('p',class_="lp-badge promotion-badge lp-font--barlow-medium" ) != None:
     internetoferta = soup.find('span',class_="price-value" ).text 

     x = internetoferta.find("$")
     oferta_limpia = internetoferta[x:]
     ofertaurlcompara = re.sub("\'","",oferta_limpia)
     #print(ofertaurlcompara.strip())


     
     porcentaje_limpio = soup.find('p',class_="lp-badge promotion-badge lp-font--barlow-medium" ).text 
     y = porcentaje_limpio.find("%")
     porcentaje = porcentaje_limpio[:y]
     #ofertaurlcompara = re.sub("\'","",oferta_limpia)
     #print(porcentaje)
     #print(porcentaje+"lalalala")

     #ofertaurlcompara = pregunta.find('span',class_="price-wrapper" ).text

         

     titulo = soup.find('h1',class_="product-name lp-font--barlow-light ms-no-margin" ).text
     titulolimpio = re.sub("\!|\'|\?|\"","",titulo)
     #print(titulolimpio)



     #if soup.find('span',class_="price-span card-price" )  != None:
     #oferta_tarjeta = soup.find('span',class_="price-span card-price" ).text 
     #p = oferta_tarjeta.find("$")
     #tarjeta_final  = oferta_tarjeta[p:]

     #print( soup.find('button',class_="add-to-cart lp-button lp-button--medium lp-button--inverted lp-button--borderless lp-button--no-hover lp-font--uppercase lp-font--barlow ms-full-width" ).text)



     if "Agregar" in soup.find('button',class_="add-to-cart lp-button lp-button--medium lp-button--inverted lp-button--borderless lp-button--no-hover lp-font--uppercase lp-font--barlow ms-full-width" ).text:



         
         if ofertaurlcompara.strip() != ofertabd:
                if porcentaje != None:
                    print("##LAPOLAR.CL##")
                    print(titulolimpio.strip())
                    print(ofertaurlcompara.strip())
                    print(porcentaje.strip())
                    print(link)
                    print(" \n ")

                    #print(titulolimpio.strip())
                    #print(ofertaurlcompara)
                    #print(porcentaje)
                    #print(tarjeta_final)
                    #print(" \n ")
                    if(int(porcentaje.strip()) >= 60 and int(porcentaje.strip()) < 100):
                        #print(porcentaje)
                        link_soicos1 = link.replace("/", "%2F")
                        link_soicos2 = link_soicos1.replace(":", "%3A")
                        link_soico_final = 'https://ad.soicos.com/-1lcE?dl='+ link_soicos2
                        link2 = "[VER PRODUCTO]"+ "("+link_soico_final+")"

                        fecha_actualizacion = datetime.today().strftime('%Y-%m-%d %H:%M')
                        query='UPDATE tecnologia_details SET oferta="%s", titulo="%s", porcentaje="%s", fecha_actualizacion="%s" where urls="%s";'%(ofertaurlcompara.strip(),titulolimpio.strip(),porcentaje.strip(), fecha_actualizacion,link)
                        print(query)
                        cur.execute(query)
                        db.commit()  
                        #print ('UPDATE tecnologia_details SET oferta="%s", titulo="%s", porcentaje="%s", fecha_actualizacion="%s"  where urls="%s" ;'%(ofertaurlcompara.strip(),titulolimpio.strip(),porcentaje.strip(), fecha_actualizacion,link))
                        #cur.execute('UPDATE tecnologia_details SET oferta="%s", titulo="%s", porcentaje="%s", fecha_actualizacion="%s"  where urls="%s"; '%(ofertaurlcompara.strip(),titulolimpio.strip(),porcentaje.strip(), fecha_actualizacion,link))
                        #db.commit()
                        test1 = telegram_bot_sendtext(f" ¡ATENCION! Hay oferta, \n{(titulolimpio.strip())} \nEsta con {(porcentaje.strip())}% de descuento. \nPrecio Oferta:  {'$'+str(ofertaurlcompara.strip())}\nEnlace: \U0001F449 {(link2)}")
                        #test = telegram_bot_sendtext_tecnologia(f" ¡ATENCION! Hay oferta, \n{(titulolimpio.strip())} \nEsta con {(porcentaje.strip())}% de descuento. \nPrecio Oferta:  {'$'+str(ofertaurlcompara.strip())}\nEnlace: \U0001F449 {(link2)}")

                   
                
                    #elif(int(porcentaje.strip()) >= 70):

                    #    link_soicos1 = link.replace("/", "%2F")
                    #    link_soicos2 = link_soicos1.replace(":", "%3A")
                    #    link_soico_final = 'https://ad.soicos.com/-1lcE?dl='+ link_soicos2
                    #   link2 = "[VER PRODUCTO]"+ "("+link_soico_final+")"
                    #    fecha_actualizacion = datetime.today().strftime('%Y-%m-%d %H:%M')
                    #    print ('UPDATE tecnologia_details SET oferta="%s", titulo="%s", porcentaje="%s", fecha_actualizacion="%s"  where urls="%s" '%(ofertaurlcompara.strip(),titulolimpio.strip(),porcentaje.strip(), fecha_actualizacion,link))
                    #    cur.execute('UPDATE tecnologia_details SET oferta="%s", titulo="%s", porcentaje="%s", fecha_actualizacion="%s"  where urls="%s" '%(ofertaurlcompara.strip(),titulolimpio.strip(),porcentaje.strip(), fecha_actualizacion,link))
                    #    db.commit()
                    #    test1 = telegram_bot_sendtext_mayor70(f" ¡ATENCION! Hay oferta, \n{(titulolimpio.strip())} \nEsta con {(porcentaje.strip())}% de descuento. \nPrecio Oferta:  {'$'+str(ofertaurlcompara.strip())}\nEnlace: \U0001F449 {(link2)}")



#except:
           #pass;           
db.close()
