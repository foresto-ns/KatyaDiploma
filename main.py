"""Основной файл программы"""
from tkinter import Tk

from ui import Interface


def main():
    root = Tk()
    root.title("Отработка мнемосхемы СОТР ПТК")
    root.geometry('700x700')
    root.resizable(False, False)

    Interface()

    root.mainloop()


if __name__ == '__main__':
    main()
