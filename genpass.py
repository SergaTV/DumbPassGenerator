import random
import pyperclip
import os
#это создано сергатв
#что тут объяснять
#пользуйся а не смотри мои коды
#плз)
#
#
#и
#вот
#что
#тут
#надо
#написать?
#я
#не
#знаю)
os.system('clear')
banner = '''

                     _        _                                      _         
                    | |      | |                                    | |        
 _ __ ___   __ _  __| | ___  | |__  _   _   ___  ___ _ __ __ _  __ _| |___   __
| '_ ` _ \\ / _` |/ _` |/ _ \\ | '_ \\| | | | / __|/ _ \\ '__/ _` |/ _` | __\\ \\ / /
| | | | | | (_| | (_| |  __/ | |_) | |_| | \\__ \\  __/ | | (_| | (_| | |_ \\ V / 
|_| |_| |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |___/\\___|_|  \\__, |\\__,_|\\__| \\_/  
                                     __/ |                __/ |                
                                    |___/                |___/                 


'''
print(banner)
i = 111
while i == 111:
	den = input("Генератор паролей вас приветствует! Как у вас проходит день?(хорошо, плохо, никак, отстань, идеально, ужасно, ты задолбал, спасибо что спросил): ")	
	if den == "хорошо" or den == "плохо" or den == "никак" or den == "отстань" or den == "идеально" or den == "ужасно" or den == "ты задолбал" or den == "спасибо что спросил":
		i = 122
	else:
		i = 111
if den == 'хорошо':
	print("Вот и отлично! А теперь за работу!")
elif den == 'плохо':
	print("Я бы спросил почему, но я не умею. :( Ну что же, в любом случае поехали за работу")
elif den == 'никак':
	print("Дерзость я не люблю :/")
	exit()
elif den == 'отстань':
	print("Не отстану) поехали...")
elif den == 'идеально':
	print("Ну так давай начнём.)")
elif den == 'ужасно':
	print("Жалко....")
elif den == 'ты задолбал':
	print("Ага, я такой.")
elif den == 'спасибо что спросил':
	print("Да незачто! Полетели)")
#
bop = ''
i = 111
while i == 111:
	p = input("Использовать специальные знаки?(@#$%^&*): ")
	if p == "да":
		i = 1111
		chars = '~zxZXCVBNMLKJHGFDSAQWERTYUIOPcvbnm,./asdfghjkl;\'qwertyuiop[]\\/*-+0987654321`!@#$%^&*()_-+='
	elif p == "нет":
		i = 1111
		chars = 'zxcvbnmlkjhgfdsaqwertyuiop0987654321ASDFGHJKLMNBVCXZQWERTYUIOP'
	else:
		i = 111
		print("Надо отвечать да\\нет")
#
#
#
aaa = int(input("Введите количество знаков: "))
aaaa = int(input("Введите количество паролей: "))
for x in range(aaaa):
	psd = ''
	for y in range(aaa):
		psd += random.choice(chars)
	print(psd)
	bop = bop + "\n" + psd
i = 111
while i == 111:
	p = input("Скопировать?(да\\нет): ")
	if p == 'да':
		i = 121212
		pyperclip.copy(bop)
	elif p == 'нет':
		i = 1212
		print("")
	else:
		i = 111
		print("Надо отвечать да\\нет")


