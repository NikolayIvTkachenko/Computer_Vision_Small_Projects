# CREATE TABLE stocks(ticker VARCHAR(10), data VARCHAR(10), price DECIMAL(15, 2));


import yfinance as yf
import mysql.connector

data = []
tickers = ['TSLA', 'FB', 'ORCL', 'AMZN']
for ticker in tickers:
    tkr = yf.Ticker(ticker)
    hist = tkr.history(period='5d').reset_index()
    records = hist[['Date','Close']].to_records(index=False)
    records = list(records)
    records = [(ticker, str(elem[0])[:10], round(elem[1],2)) for elem in records]
    data = data + records

print(data)




# Инициализируем переменные до try, чтобы они были видны в finally
cnx = None
cursor = None


try:
    cnx = mysql.connector.connect(user='root', password='toor', host='localhost', port=3316, database='db_science')
    cursor = cnx.cursor()

    query_add_stocks = ("""INSERT INTO stocks (ticker, date, proce) VALUES (%s, %s, %s)""")

    cursor.executemany(query_add_stocks, data)
    cnx.commit()



except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
    # Если транзакция начала записываться, но упала на середине — откатываем
    if cnx and cnx.is_connected():
        cnx.rollback()

    print(f"Ошибка MySQL [{err.errno}]: {err.msg}")
finally:
    if cursor:
        cursor.close()
    if cnx and cnx.is_connected():
        cnx.close()
        print("Соединение с БД закрыто.")