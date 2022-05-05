# PIP INSTALL SQLITE3

import sqlite3
con = sqlite3.connect('list.sqlite') # НАЗВАНИЕ БАЗЫ ДАННЫХ ДЛЯ ПОДКЛЮЧЕНИЯ



c = con.cursor()


# ЗАПРОС БАЗЕ ДАННЫХ SQLITE3
# СТАВИТЕ ФИЛЬТР ЧТОБ СОРТИРОВАЛОСЬ ИЗ БД, СЕЙЧАС СТОИТ ПРОМЕЖУТОК: ДАННОЕ ВРЕМЯ NOW + 1 МЕСЯЦ
c.execute('''
SELECT  adress, datefn
FROM `test`
where  strftime('%Y-%m-%d',datetime(substr(datefn, 7, 4) || '-' || substr(datefn, 4, 2) || '-' || substr(datefn, 1, 2))) between strftime('%Y-%m-%d', date('now','+7 days'))  and strftime('%Y-%m-%d', date('now','+1 month'))
''')

data=c.fetchall()
separator='-------------------------\n'
output=separator
if data !=None:
      for row in data:
         adress=row[0]
         datefn=row[1]
         output+="| {} | {} | \n".format(adress,datefn)
         output+=separator


#print(output)


