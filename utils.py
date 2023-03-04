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
