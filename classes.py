from tkinter import Button


class ButtonWord:
    def __init__(self, frame_1):
        """
        Инициализация кнопок
        :param frame_1: Фрейм для отображения
        """
        self.btn_1 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_2 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_3 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_4 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_5 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_6 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_7 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_8 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_9 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_10 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_11 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_12 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_13 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_14 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_15 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_16 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_17 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_18 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_19 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_20 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_21 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_22 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_23 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_24 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_25 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_26 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_27 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_28 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_29 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_30 = Button(frame_1, height=1, width=1, padx=10, pady=4)
        # кнопка выбора цвета
        self.btn_31 = Button(frame_1, height=1, width=1, padx=10, pady=4, bg='yellow')
        self.btn_32 = Button(frame_1, height=1, width=1, padx=10, pady=4, bg='green')

        self.__draw_field()
        self.__add_command_button()

    def __draw_field(self):
        """отрисовать поле для ввода"""
        self.btn_1.place(x=5, y=5)
        self.btn_2.place(x=40, y=5)
        self.btn_3.place(x=75, y=5)
        self.btn_4.place(x=110, y=5)
        self.btn_5.place(x=145, y=5)
        self.btn_6.place(x=5, y=37)
        self.btn_7.place(x=40, y=37)
        self.btn_8.place(x=75, y=37)
        self.btn_9.place(x=110, y=37)
        self.btn_10.place(x=145, y=37)
        self.btn_11.place(x=5, y=69)
        self.btn_12.place(x=40, y=69)
        self.btn_13.place(x=75, y=69)
        self.btn_14.place(x=110, y=69)
        self.btn_15.place(x=145, y=69)
        self.btn_16.place(x=5, y=101)
        self.btn_17.place(x=40, y=101)
        self.btn_18.place(x=75, y=101)
        self.btn_19.place(x=110, y=101)
        self.btn_20.place(x=145, y=101)
        self.btn_21.place(x=5, y=134)
        self.btn_22.place(x=40, y=134)
        self.btn_23.place(x=75, y=134)
        self.btn_24.place(x=110, y=134)
        self.btn_25.place(x=145, y=134)
        self.btn_26.place(x=5, y=167)
        self.btn_27.place(x=40, y=167)
        self.btn_28.place(x=75, y=167)
        self.btn_29.place(x=110, y=167)
        self.btn_30.place(x=145, y=167)
        self.btn_31.place(x=5, y=200)
        self.btn_32.place(x=40, y=200)

    def __add_command_button(self):
        """Назначить действие кнопке"""
        self.btn_1.config(command=lambda btn=self.btn_1: self.__choise_field(btn))
        self.btn_2.config(command=lambda btn=self.btn_2: self.__choise_field(btn))
        self.btn_3.config(command=lambda btn=self.btn_3: self.__choise_field(btn))
        self.btn_4.config(command=lambda btn=self.btn_4: self.__choise_field(btn))
        self.btn_5.config(command=lambda btn=self.btn_5: self.__choise_field(btn))
        self.btn_6.config(command=lambda btn=self.btn_6: self.__choise_field(btn))
        self.btn_7.config(command=lambda btn=self.btn_7: self.__choise_field(btn))
        self.btn_8.config(command=lambda btn=self.btn_8: self.__choise_field(btn))
        self.btn_9.config(command=lambda btn=self.btn_9: self.__choise_field(btn))
        self.btn_10.config(command=lambda btn=self.btn_10: self.__choise_field(btn))
        self.btn_11.config(command=lambda btn=self.btn_11: self.__choise_field(btn))
        self.btn_12.config(command=lambda btn=self.btn_12: self.__choise_field(btn))
        self.btn_13.config(command=lambda btn=self.btn_13: self.__choise_field(btn))
        self.btn_14.config(command=lambda btn=self.btn_14: self.__choise_field(btn))
        self.btn_15.config(command=lambda btn=self.btn_15: self.__choise_field(btn))
        self.btn_16.config(command=lambda btn=self.btn_16: self.__choise_field(btn))
        self.btn_17.config(command=lambda btn=self.btn_17: self.__choise_field(btn))
        self.btn_18.config(command=lambda btn=self.btn_18: self.__choise_field(btn))
        self.btn_19.config(command=lambda btn=self.btn_19: self.__choise_field(btn))
        self.btn_20.config(command=lambda btn=self.btn_20: self.__choise_field(btn))
        self.btn_21.config(command=lambda btn=self.btn_21: self.__choise_field(btn))
        self.btn_22.config(command=lambda btn=self.btn_22: self.__choise_field(btn))
        self.btn_23.config(command=lambda btn=self.btn_23: self.__choise_field(btn))
        self.btn_24.config(command=lambda btn=self.btn_24: self.__choise_field(btn))
        self.btn_25.config(command=lambda btn=self.btn_25: self.__choise_field(btn))
        self.btn_26.config(command=lambda btn=self.btn_26: self.__choise_field(btn))
        self.btn_27.config(command=lambda btn=self.btn_27: self.__choise_field(btn))
        self.btn_28.config(command=lambda btn=self.btn_28: self.__choise_field(btn))
        self.btn_29.config(command=lambda btn=self.btn_29: self.__choise_field(btn))
        self.btn_30.config(command=lambda btn=self.btn_30: self.__choise_field(btn))
        self.btn_31.config(command=lambda btn=self.btn_31: self.__change_color(btn))
        self.btn_32.config(command=lambda btn=self.btn_32: self.__change_color(btn))

    def __choise_field(self, btn):
        """выбор поля для ввода"""
        self.classes_key = btn

    def __change_color(self, btn):
        """сменить цвет кнопки"""
        color_button = btn.cget('bg')
        self.classes_key.config(bg=color_button)
