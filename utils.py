"""Модуль со вспомогательными функциями для рабоыт программы"""
import pandas as pd

from constants import F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9


def field_1(inp: float) -> tuple[str, str]:
    """Обработка параметра 1ДД1П"""
    if inp <= 350:
        return 'red', 'Разгерм. КВА1'
    return 'green', ''


def field_2(inp: float) -> tuple[str, str]:
    """Обработка параметра 1ДД2П"""
    if inp <= 350:
        return 'red', 'Разгерм. КВА1'
    return 'green', ''


def field_3(inp: float) -> tuple[str, str]:
    """Обработка параметра 1ДПДП"""
    if inp < 0.1:
        return 'red', ''
    return 'green', ''


def field_4(inp: float) -> tuple[str, str]:
    """Обработка параметра ДПД1СПНП"""
    if inp < 0.2:
        return 'red', ''
    return 'green', ''


def field_5(inp: float) -> tuple[str, str]:
    """Обработка параметра 2ДД1П"""
    if inp <= 350:
        return 'red', 'Разгерм. КВА2'
    return 'green', ''


def field_6(inp: float) -> tuple[str, str]:
    """Обработка параметра 2ДД2П"""
    if inp <= 350:
        return 'red', 'Разгерм. КВА2'
    return 'green', ''


def field_7(inp: float) -> tuple[str, str]:
    """Обработка параметра 2ДПДП"""
    if inp < 0.1:
        return 'red', ''
    return 'green', ''


def field_8(inp: float) -> tuple[str, str]:
    """Обработка параметра ДПД2СПНП"""
    if inp < 0.2:
        return 'red', ''
    return 'green', ''


def field_9(inp: float) -> tuple[str, str]:
    """Обработка параметра 5ДД1"""
    if inp > 0.95:
        return 'green', ''
    if 0.95 > inp > 0.04:
        return 'yellow', ''
    return 'red', ''


def read_file(file: str) -> dict:
    """Чтение файла и его обработка"""
    data = pd.read_excel(io=file)

    f_1 = data.loc[:, F_1][0]
    f_2 = data.loc[:, F_2][0]
    f_3 = data.loc[:, F_3][0]
    f_4 = data.loc[:, F_4][0]
    f_5 = data.loc[:, F_5][0]
    f_6 = data.loc[:, F_6][0]
    f_7 = data.loc[:, F_7][0]
    f_8 = data.loc[:, F_8][0]
    f_9 = data.loc[:, F_9][0]

    result = {
        'f_1': field_1(f_1),
        'f_2': field_2(f_2),
        'f_3': field_3(f_3),
        'f_4': field_4(f_4),
        'f_5': field_5(f_5),
        'f_6': field_6(f_6),
        'f_7': field_7(f_7),
        'f_8': field_8(f_8),
        'f_9': field_9(f_9),
    }

    return result
