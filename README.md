# bots-twitter-python

* bot_twitter_topics.py: 
* bot_twitter_users.py

#crontab
For execute each bot you need add two lines on the crontab:

* 30 7,17 * * * sh /home/odraudek99/bots/ejecuta_bot_linea12.sh
* 30 9,12,14,19,22 * * * sh /home/odraudek99/bots/ejecuta_bot_users.sh




This project needs a properties file:

bot.properties

Example
```

[twitter]
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET


usuarios=USER1, USER2, USER3, USER_N

twitter.query=linea12 OR linea dorada OR lineaDorada
horas=2
horasusr=4


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
