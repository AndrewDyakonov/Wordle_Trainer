import tkinter as tk


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
