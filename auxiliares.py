"""
.. module:: auxiliares
   :platform: Linux, Windows
   :synopsis: Generación de tablas en Jupyter Notebook.

.. moduleauthor:: Alejandro Araneda <eloscurodeefeso@gmail.com>

    El presente módulo :mod:`auxiliares` contiene las funciones
    auxiliares para la generación de tablas en una Jupyter Notebook.

"""
from itertools import takewhile, count
from IPython.display import display, Markdown


def tabla(filas, encabezados, funciones=None):
    """
    Genera una tabla en Markdown y ordena su visualización

    Se espera que los valores de *filas* respondan a la función
    :func:`str` y la cantidad de columnas coincida con la cantidad
    de elementos en *encabezados*. Las *funciones* deben recibir
    un solo argumento. Se creará un salida del tipo
    :class:`IPython.core.display.Markdown`

    :param filas: valores por filas y luego por columnas
    :type filas: list[list]
    :param encabezados: encabezados de las columnas
    :type encabezados: list[str]
    :param funciones: generadores de las columnas, defaults to None
    :type funciones: list[function], optional
    """
    if funciones:
        filas = [[fun(valor) for fun in funciones] for valor in filas]
    display(
        Markdown(
            "|"
            + "|".join(encabezados)
            + "|\n"
            + "".join(["|:-:" for _ in encabezados])
            + "\n"
            + "".join(["|" + "|".join(map(str, f)) + "|\n" for f in filas])
        )
    )