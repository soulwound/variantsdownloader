from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter.ttk import *
import threading


def download_chosen():
    print(choise.get())
    if choise.get() == 'ЕГЭ':
        ege_thread = threading.Thread(target=ege_download, daemon=True)
        ege_thread.start()
    elif choise.get() == 'ОГЭ':
        oge_thread = threading.Thread(target=oge_download, daemon=True)
        oge_thread.start()


def oge_download():
    status.config(text='Загрузка вариантов ОГЭ началась', font='Arial 15')
    browser = webdriver.Chrome()
    browser.get('https://rus-oge.sdamgia.ru/')
    sleep(5)
    links = browser.find_elements(By.TAG_NAME, 'a')
    variants_id = []
    i = 1
    for link in links:
        if 'test?id' in link.get_attribute('href'):
            variants_id.append(link.get_attribute('href').partition('?id=')[2])
    for variants in variants_id:
        name = f'oge-{i} вариант'
        i += 1
        print(name)
        f = open(f'C:\Programming\Projects\egedowloader\{name}.pdf', "wb")# открываем файл для записи, в режиме wb
        ufr = requests.get(f'https://rus-oge.sdamgia.ru/test?id={variants}&print=true&pdf=z&num=true&attr8=true&attr7=true&tt=&td=')# делаем запрос
        f.write(ufr.content)# записываем содержимое в файл; как видите - content запроса
        print('success!')
        f.close()
    i = 1
    for variants in variants_id:
        name = f'oge-{i} вариант ответы'
        i += 1
        print(name)
        f = open(f'C:\Programming\Projects\egedowloader\{name}.pdf', "wb")# открываем файл для записи, в режиме wb
        ufr = requests.get(f'https://rus-oge.sdamgia.ru/test?id={variants}&print=true&pdf=z&sol=true&num=true&ans=true&key=true&attr8=true&attr7=true&tt=&td=')# делаем запрос
        f.write(ufr.content)# записываем содержимое в файл; как видите - content запроса
        print('success!')
        f.close()
    status.config(text='Варианты ОГЭ успешно загружены', font='Arial 15')


def ege_download():
    status.config(text='Загрузка вариантов ЕГЭ началась', font='Arial 15')
    browser = webdriver.Chrome()
    browser.get('https://rus-ege.sdamgia.ru/')
    sleep(5)
    links = browser.find_elements(By.TAG_NAME, 'a')
    variants_id = []
    i = 1
    for link in links:
        if 'test?id' in link.get_attribute('href'):
            variants_id.append(link.get_attribute('href').partition('?id=')[2])
    for variants in variants_id:
        name = f'ege-{i} вариант'
        i += 1
        print(name)
        f = open(f'C:\Programming\Projects\egedowloader\{name}.pdf', "wb")# открываем файл для записи, в режиме wb
        ufr = requests.get(f'https://rus-ege.sdamgia.ru/test?id={variants}&print=true&pdf=z&num=true&tt=&td=')# делаем запрос
        f.write(ufr.content)# записываем содержимое в файл; как видите - content запроса
        print('success!')
        f.close()
    i = 1
    for variants in variants_id:
        name = f'ege-{i} вариант ответы'
        i += 1
        print(name)
        f = open(f'C:\Programming\Projects\egedowloader\{name}.pdf', "wb")# открываем файл для записи, в режиме wb
        ufr = requests.get(f'https://rus-ege.sdamgia.ru/test?id={variants}&print=true&pdf=z&sol=true&num=true&ans=true&key=true&attr5=true&tt=&td=')# делаем запрос
        f.write(ufr.content)# записываем содержимое в файл; как видите - content запроса
        print('success!')
        f.close()
    status.config(text='Варианты ЕГЭ успешно загружены', font='Arial 15')


window = Tk()
window.title('Загрузчик вариантов')
window.geometry('400x400')
choise = Combobox(window)
choise['values'] = ('Выберите, что нужно скачать', 'ЕГЭ', 'ОГЭ')
choise.current(0)
choise.pack(fill='x', padx=10, pady=10)
download_button = Button(window, text='Скачать', command=download_chosen, padding=5)
download_button.pack(padx=10, pady=10)
status = Label(text='Ожидание...', font='Arial 30')
status.pack(padx=10, pady=10)


window.mainloop()
