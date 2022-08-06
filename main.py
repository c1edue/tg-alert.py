import schedule
import time
import selenium
import telebot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from telebot import types
options = Options()
options.headless = True
token = 'bot token'
browser = webdriver.Chrome(options = options)
bot = telebot.TeleBot(token, parse_mode=None)
tg_id = 'There must be your tg id'
print('system load')
condition = ''
wind_condition = ''
def surrounding_alert():
	print('start scraping')
	try:
		browser.get('https://www.google.com/search?q=погода&client=opera-gx&hs=3G8&sxsrf=ALiCzsaTd4ihkNP5KDe6SIshBGrzfgI5TA%3A1659732664626&ei=uILtYvfoJaWrrgThh6_gBw&ved=0ahUKEwj3pJb_ybD5AhWllYsKHeHDC3wQ4dUDCA0&uact=5&oq=погода&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEEMyDQgAELEDEIMBEMkDEEMyBQgAEJIDMgsIABCABBCxAxCDATIECAAQQzIECAAQQzIECAAQQzIECAAQQzIKCAAQsQMQgwEQQzIECAAQQzoECCMQJ0oECEEYAEoECEYYAFAAWOgFYNwIaABwAXgAgAFniAGYBJIBAzUuMZgBAKABAcABAQ&sclient=gws-wiz')
		temp = browser.find_element(By.XPATH,'//*[@id="wob_tm"]').text
		print(f'Температура: {temp}')
		precipitation = browser.find_element(By.XPATH,'//*[@id="wob_pp"]').text
		print(f'Вероятность осадков: {precipitation}')
		wet = browser.find_element(By.XPATH,'//*[@id="wob_hm"]').text
		print(f'Влажность: {wet}')
		wind = browser.find_element(By.XPATH,'//*[@id="wob_ws"]').text
		wind = wind.replace(' км/ч', '')
		print(f'Ветер: {wind}')
		geo = browser.find_element(By.XPATH,'//*[@id="wob_loc"]').text
		print(f'Местоположение: {geo}')
		try:
			if float(temp) < 17:
				condition = 'прохладно'
			elif float(temp) > 30:
				condition = ' жарко'
			else:
				condition = 'классная погода'

			if float(wind) < 10:
				wind_condition = 'слабый'
			if float(wind) > 17:
				wind_condition = 'сильный'
			else:
				wind_condition = 'отсутствует'
		except Exception as e:
			print(e)
	except Exception as e:
		print(e)
	try:
		browser.get('https://mixnews.lv/anekdoty/')
		joke = browser.find_element(By.XPATH,'//*[@id="post-2192567"]/div[2]/p').text
		print(joke)
		print(f'Доброе утро!\n Сейчас 9 часов утра,{condition}-{temp}℃\n Вероятность дождя: {precipitation},\n Влажность: {wet}\n Ветер {wind_condition},{wind}км/ч,гео: {geo}\n\n\n Шуточки: {joke}')
	except Exception as e:
		print(e)
	try:

		bot.send_message(tg_id, f'Доброе утро!\n Сейчас 9 часов утра,{condition}-{temp}℃\n Вероятность дождя: {precipitation},\n Влажность: {wet}\n Ветер {wind_condition},{wind}км/ч,гео: {geo}\n\n\n Шуточки: {joke}')
		bot.polling()
		browser.close()
	except Exception as e:
		print(e)
schedule.every().day.at('09:00').do(surrounding_alert)
while True:
    schedule.run_pending()
    time.sleep(1)
