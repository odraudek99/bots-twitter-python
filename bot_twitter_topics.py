'''
Created on May 5, 2016

@author: odraudek99
'''
import logging
import tweepy
import configparser
import smtplib
#from tweepy.auth import OAuthHandler

logging.basicConfig(filename='log_bot_topics.log',level=logging.INFO)

logging.info('Init: bot_twitter_topics.py')

config = configparser.RawConfigParser()
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

query =config.get('twitter','query')

logging.info('query: '+query)

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

mensaje_correo=""

try:
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    search_results = api.search(q=query, count=resultados)
    
    for i in search_results:
        mensaje_correo+=(str(i.created_at)+'\n')
        mensaje_correo+=(i.user.screen_name+'\n')
        mensaje_correo+=(i.text+'\n\n')
    
    #print (mensaje_correo)
    
    mensaje_correo=mensaje_correo.encode('utf-8') 
    
    message = 'Subject: %s\n\n%s' % ('SUBJECT', mensaje_correo)
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(correoSalida,password)
    
    
    server.sendmail('Eduardo G', correoDestino, message)
    server.quit()

except tweepy.TweepError as e:
    logging.error('error: '+ e)
    logging.error ('Error! Failed to get request token.')
    
    
    
    
