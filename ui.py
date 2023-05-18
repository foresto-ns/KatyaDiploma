"""Модуль отрисовки интерфейса и взаимодействия с ним"""
from tkinter import filedialog as fd, CENTER
from tkinter import Canvas, Frame, BOTH, Button, LEFT

from constants import F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9
from utils import read_file


class Interface(Frame):
    def __init__(self):
        super().__init__()
        self.f_1 = None
        self.f_2 = None
        self.f_3 = None
        self.f_4 = None
        self.f_5 = None
        self.f_6 = None
        self.f_7 = None
        self.f_8 = None
        self.f_9 = None
        self.error_msg = None
        self.canvas = None
        self.coords = [
            (100, 100),
            (260, 100),
            (50, 210),
            (400, 210),
            (100, 320),
            (260, 320),
            (50, 430),
            (400, 430),
            (50, 540),
        ]
        self.width = 100
        self.height = 50
        self.initUI()

    def open_file(self) -> None:
        """Загрузка и обработка файла"""
        filetypes = (
            ('excel files', '*.xlsx'),
            ('All files', '*.*')
        )

        # Открытие файла при помощи проводника
        f = fd.askopenfilename(filetypes=filetypes)

        # Передача название файла во вспомогательную функцию и получение ответа
        info = read_file(f)

        # Изменение цвета и вывод ошибок на основании полученной информации после обработки
        self.change_color(data=info)

    def clear(self) -> None:
        """Очистка мнемосхемы"""
        self.canvas.itemconfig(self.f_1[0], fill='white')
        self.canvas.itemconfig(self.f_2[0], fill='white')
        self.canvas.itemconfig(self.f_3[0], fill='white')
        self.canvas.itemconfig(self.f_4[0], fill='white')
        self.canvas.itemconfig(self.f_5[0], fill='white')
        self.canvas.itemconfig(self.f_6[0], fill='white')
        self.canvas.itemconfig(self.f_7[0], fill='white')
        self.canvas.itemconfig(self.f_8[0], fill='white')
        self.canvas.itemconfig(self.f_9[0], fill='white')
        self.canvas.itemconfig(self.error_msg, text='')

    def change_color(self, data: dict) -> None:
        """Изменение цвета и вывод ошибок на экран"""
        self.canvas.itemconfig(self.f_1[0], fill=data['f_1'][0])
        self.canvas.itemconfig(self.f_2[0], fill=data['f_2'][0])
        self.canvas.itemconfig(self.f_3[0], fill=data['f_3'][0])
        self.canvas.itemconfig(self.f_4[0], fill=data['f_4'][0])
        self.canvas.itemconfig(self.f_5[0], fill=data['f_5'][0])
        self.canvas.itemconfig(self.f_6[0], fill=data['f_6'][0])
        self.canvas.itemconfig(self.f_7[0], fill=data['f_7'][0])
        self.canvas.itemconfig(self.f_8[0], fill=data['f_8'][0])
        self.canvas.itemconfig(self.f_9[0], fill=data['f_9'][0])
        self.canvas.itemconfig(self.error_msg, text='; '.join([x[1] for x in data.values() if x[1] != '']))

    def initUI(self) -> None:
        """Отрисовка интерфейса"""
        self.pack(fill=BOTH, expand=True)

        self.canvas = Canvas(self)

        # Инициализация сообщения об ошибке
        self.error_msg = self.canvas.create_text(350, 50, anchor=CENTER, text='', font=("Helvetica", 16),
                                                 fill='red')

        # Инициализация кнопок
        btn = Button(self.canvas, text="Обработать файл", command=self.open_file)
        btn.pack(side=LEFT, anchor='nw')
        btn_2 = Button(self.canvas, text="Очистить", command=self.clear)
        btn_2.pack(side=LEFT, anchor='nw')

        # Длинные горизонтальные
        self.canvas.create_line(0, self.coords[3][1] + self.height // 2, self.coords[3][0] + self.width + 100,
                                self.coords[3][1] + self.height // 2, width=5)
        self.canvas.create_line(0, self.coords[6][1] + self.height // 2, self.coords[7][0] + self.width + 100,
                                self.coords[7][1] + self.height // 2, width=5)
        # Вертикальные
        self.canvas.create_line((self.coords[0][0] + self.coords[1][0] + self.width) // 2,
                                self.coords[2][1] + self.height // 2,
                                (self.coords[0][0] + self.coords[1][0] + self.width) // 2,
                                self.coords[0][1] + self.height // 2,
                                width=5)
        self.canvas.create_line((self.coords[1][0] + self.coords[3][0] + self.width) // 2,
                                self.coords[2][1] + 2.5,
                                (self.coords[1][0] + self.coords[3][0] + self.width) // 2,
                                self.coords[1][1] + self.height // 2,
                                width=5)
        self.canvas.create_line((self.coords[4][0] + self.coords[5][0] + self.width) // 2,
                                self.coords[6][1] + self.height // 2,
                                (self.coords[4][0] + self.coords[5][0] + self.width) // 2,
                                self.coords[4][1] + self.height // 2,
                                width=5)
        self.canvas.create_line((self.coords[5][0] + self.coords[7][0] + self.width) // 2,
                                self.coords[6][1] + 2.5,
                                (self.coords[5][0] + self.coords[7][0] + self.width) // 2,
                                self.coords[5][1] + self.height // 2,
                                width=5)
        # Короткие горизонтальные
        self.canvas.create_line(self.coords[0][0] + self.width,
                                self.coords[0][1] + self.height // 2,
                                (self.coords[0][0] + self.coords[1][0] + self.width) // 2 + 2.5,
                                self.coords[0][1] + self.height // 2,
                                width=5)
        self.canvas.create_line(self.coords[1][0] + self.width,
                                self.coords[1][1] + self.height // 2,
                                (self.coords[1][0] + self.coords[3][0] + self.width) // 2 + 2.5,
                                self.coords[1][1] + self.height // 2,
                                width=5)
        self.canvas.create_line(self.coords[4][0] + self.width,
                                self.coords[4][1] + self.height // 2,
                                (self.coords[4][0] + self.coords[5][0] + self.width) // 2 + 2.5,
                                self.coords[4][1] + self.height // 2,
                                width=5)
        self.canvas.create_line(self.coords[5][0] + self.width,
                                self.coords[5][1] + self.height // 2,
                                (self.coords[5][0] + self.coords[7][0] + self.width) // 2 + 2.5,
                                self.coords[5][1] + self.height // 2,
                                width=5)
        # Средние горизонтальные
        self.canvas.create_line((self.coords[0][0] + self.coords[1][0] + self.width) // 2,
                                self.coords[2][1],
                                (self.coords[1][0] + self.coords[3][0] + self.width) // 2,
                                self.coords[2][1],
                                width=5)
        self.canvas.create_line((self.coords[4][0] + self.coords[5][0] + self.width) // 2,
                                self.coords[6][1],
                                (self.coords[5][0] + self.coords[7][0] + self.width) // 2,
                                self.coords[6][1],
                                width=5)

        # Отрисовка прямоугольников и сохранение ссылок на фигуры и текст
        self.f_1 = (
            self.canvas.create_rectangle(
                self.coords[0][0], self.coords[0][1], self.coords[0][0] + self.width, self.coords[0][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[0][0] + self.width // 2, self.coords[0][1] + self.height // 2,
                                    text=F_1)
        )

        self.f_2 = (
            self.canvas.create_rectangle(
                self.coords[1][0], self.coords[1][1], self.coords[1][0] + self.width, self.coords[1][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[1][0] + self.width // 2, self.coords[1][1] + self.height // 2,
                                    text=F_2)
        )

        self.f_3 = (
            self.canvas.create_rectangle(
                self.coords[2][0], self.coords[2][1], self.coords[2][0] + self.width, self.coords[2][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[2][0] + self.width // 2, self.coords[2][1] + self.height // 2,
                                    text=F_3)
        )

        self.f_4 = (
            self.canvas.create_rectangle(
                self.coords[3][0], self.coords[3][1], self.coords[3][0] + self.width, self.coords[3][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[3][0] + self.width // 2, self.coords[3][1] + self.height // 2,
                                    text=F_4)
        )

        self.f_5 = (
            self.canvas.create_rectangle(
                self.coords[4][0], self.coords[4][1], self.coords[4][0] + self.width, self.coords[4][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[4][0] + self.width // 2, self.coords[4][1] + self.height // 2,
                                    text=F_5)
        )

        self.f_6 = (
            self.canvas.create_rectangle(
                self.coords[5][0], self.coords[5][1], self.coords[5][0] + self.width, self.coords[5][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[5][0] + self.width // 2, self.coords[5][1] + self.height // 2,
                                    text=F_6)
        )

        self.f_7 = (
            self.canvas.create_rectangle(
                self.coords[6][0], self.coords[6][1], self.coords[6][0] + self.width, self.coords[6][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[6][0] + self.width // 2, self.coords[6][1] + self.height // 2,
                                    text=F_7)
        )

        self.f_8 = (
            self.canvas.create_rectangle(
                self.coords[7][0], self.coords[7][1], self.coords[7][0] + self.width, self.coords[7][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[7][0] + self.width // 2, self.coords[7][1] + self.height // 2,
                                    text=F_8)
        )

        self.f_9 = (
            self.canvas.create_rectangle(
                self.coords[8][0], self.coords[8][1], self.coords[8][0] + self.width, self.coords[8][1] + self.height,
                fill="white"),
            self.canvas.create_text(self.coords[8][0] + self.width // 2, self.coords[8][1] + self.height // 2,
                                    text=F_9)
        )

        self.canvas.pack(fill=BOTH, expand=True)
