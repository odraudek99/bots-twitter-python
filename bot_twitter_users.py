'''
Created on May 5, 2016

@author: odraudek99
'''
import traceback
import logging
import tweepy
import ConfigParser
import smtplib
import unicodedata

from datetime import datetime, timedelta


def getString (status) :
	try:
		msgUnicode = unicodedata.normalize('NFKD', status.text).encode('ascii','ignore')
		mensaje=str(status.created_at)+':\n'+ str(msgUnicode) +'\n\n'
		return mensaje.encode('utf-8')
	except Exception as e:
		logging.error(e)
    		traceback.print_exc()
    		traceback.print_exc(file=open("errlog.txt","a"))
		return ""


logging.basicConfig(filename='log_bot_users.log',format = "%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s",level=logging.INFO)
logging.info('init bot users')

config = ConfigParser.RawConfigParser()
config.read('bot.properties')

password= config.get('correo', 'password')
correoSalida= config.get('correo', 'correoSalida')
correoDestino= config.get('correo', 'correoDestino')
internetAddress= config.get('correo', 'internetAddress')

consumer_key = config.get('twitter', 'consumer_key')
consumer_secret = config.get('twitter', 'consumer_secret')
access_token = config.get('twitter', 'access_token')
access_token_secret = config.get('twitter', 'access_token_secret')
resultados = config.get('twitter', 'resultados')

usuarios = config.get('twitter', 'usuarios')
horas=config.get('twitter','horasusr')
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

mensaje_correo=""
mensaje=""
try:
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    for usr in usuarios.split(","):
    
        usr = usr.strip()
        print(usr)
	mensaje = '------> '+usr+'\n'
        mensaje_correo +=mensaje.encode('utf-8')
        usuario = api.get_user(usr)   
        status_list = api.user_timeline(screen_name = usr, include_rts = True, count=13)
        hours_from_now = datetime.now() - timedelta(hours=int(horas))
        
        for status in status_list:
            
            if status.created_at >= hours_from_now:
            
                logging.info (str(status.created_at)+':\n'+status.text)
		mensaje=getString(status)
                mensaje_correo +=mensaje.encode('utf-8')
           
        print('\n') 

    print (mensaje_correo)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(correoSalida,password)
    
    mensaje_correo=mensaje_correo.encode('utf-8') 
    #mensaje_correo=unicode(mensaje_correo.decode('utf-8'))
    #mensaje_correo=mensaje_correo.decode('unicode_escape').encode('ascii','ignore')
    
    message = 'Subject: %s\n\n%s' % ('USUARIOS '+str(datetime.now()), mensaje_correo)
    
    server.sendmail('Eduardo G', correoDestino, message)
    server.quit()

except tweepy.TweepError as e:
    logging.error(e)
    print ('Error! Failed to get request token.')
    
except Exception as e:
    logging.error(e)    
    traceback.print_exc()    
    traceback.print_exc(file=open("errlog.txt","a"))
    
