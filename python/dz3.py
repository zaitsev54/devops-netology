#!/usr/bin/env python3

import socket as s
import time as t
import datetime as dt

# set variables 
i = 1
wait = 2 # интервал проверок в секундах
srv = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
init=0

print('*** start script ***')
print(srv)
print('********************')

while 1 == 1 : #отладочное число проверок 
  for host in srv:
    ip = s.gethostbyname(host)
    if ip != srv[host]:
      if i==1 and init !=1:
        print(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + str(host) +' IP mistmatch: '+srv[host]+' '+ip)
      srv[host]=ip
  #print(i)
  i+=1 # счетчик итераций для отладки, закомментировать для бесконечного цикла
  if i >=50 :
    break
  t.sleep(wait)