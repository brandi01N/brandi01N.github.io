from pywebio.platform.flask import start_server
from pywebio.input import *
from pywebio.output import *


def bmi():
    height = input("Введите ваш рост:", type=FLOAT)
    weight = input("Введите ваш вес:", type=FLOAT)

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        put_text("У вас недостаточная масса тела.")
    elif bmi >= 18.5 and bmi < 25:
        put_text("У вас нормальная масса тела.")
    elif bmi >= 25 and bmi < 30:
        put_text("У вас избыточная масса тела.")
    else:
        put_text("У вас ожирение.")


start_server(bmi, port=80)
