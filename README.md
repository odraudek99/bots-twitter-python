# bots-twitter-python

Modules: 
* tweepy
* configparser
* smtplib

bot_twitter_topics.py: 
bot_twitter_users.py

This project needs a properties file:

bot.properties

Example
```

[twitter]
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET


usuarios=USER1, USER2, USER3, USER_N

twitter.query=linea12 OR linea dorada OR lineaDorada


#bot
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

resultados=20



[correo]
password=PASSWORD
correoSalida=EMAIL_FROM@gmail.com
correoDestino=EMAIL_TO@gmail.com
internetAddress=InfoNotificacionestwitter

```
