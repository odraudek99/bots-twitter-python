'''
Created on May 5, 2016

@author: odraudek99
'''
import logging
import tweepy
import ConfigParser
import smtplib

from datetime import datetime, timedelta


logging.basicConfig(filename='log_bot_users.log',level=logging.INFO)
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
horas=config.get('twitter','horas')
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

mensaje_correo=""

try:
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    for usr in usuarios.split(","):
    
        usr = usr.strip()
        print(usr)
        mensaje_correo +='------> '+usr+'\n'
        usuario = api.get_user(usr)   
        status_list = api.user_timeline(screen_name = usr, include_rts = True, count=13)
        nine_hours_from_now = datetime.now() - timedelta(hours=int(horas))
        
        for status in status_list:
            
            if status.created_at >= nine_hours_from_now:
            
                print (str(status.created_at)+':\n'+status.text)
                mensaje_correo +=(str(status.created_at)+':\n'+status.text)+'\n\n'
           
        print('\n') 

    print (mensaje_correo)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(correoSalida,password)
    
    mensaje_correo=mensaje_correo.encode('utf-8') 
    
    message = 'Subject: %s\n\n%s' % ('USUARIOS', mensaje_correo)
    
    server.sendmail('Eduardo G', correoDestino, message)
    server.quit()

except tweepy.TweepError as e:
    print (e)
    print ('Error! Failed to get request token.')
    
    
    
    
