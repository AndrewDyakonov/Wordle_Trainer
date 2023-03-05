import tkinter as tk
from tkinter import scrolledtext


def create_form():
    """
    Создание формы
    win.geometry  - Размер формы. Начальное расположение при инициализации
    win.title     - Имя в заголовке
    win.resizable - Запрет изменения размера
    :return:      - Возвращает готовую форму
    """

    win = tk.Tk()
    win.geometry('300x350+1000+100')
    win.title('Wordle Trainer')
    win.resizable(False, False)
    return win


def create_frame(window):
    """
    Создание фреймов на форме
    :param window: форма
    :return:       кортеж с двумя фреймами
    """
    frame_1 = tk.Frame(window, bg='red', width=300, height=250)
    frame_2 = tk.Frame(window, bg='yellow', width=300, height=100)

    frame_1.pack(expand=True, anchor='w')
    frame_2.pack(expand=True)
    return frame_1, frame_2


def create_scrolledtext(frame_1):
    """
    Создание окна вывода
    :param frame_1: фрейм для отображения
    :return: окно вывода слов
    """
    listbox = scrolledtext.ScrolledText(frame_1, width=10, height=11)

    listbox.place(x=200, y=3)
    return listbox


def create_entry(frame_2):
    """
    Создание поля ввода слова
    :param frame_2: фрейм для отображения
    :return: поле ввода слова
    """
    entry = tk.Entry(frame_2, width=10)

    entry.place(x=50, y=40)
    return entry
