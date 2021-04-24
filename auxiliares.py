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


def format_vec(vec):
    """
    Da formato a un vector de flotantes para su visualización

    :param vec: iterable de tres elementos
    :type vec: list[float]
    :return: cadena de caracteres conteniendo tres flotantes
	con hasta 3 decimales, todo entre corchetes
    :rtype: str
    """
    return "[{0:.3f}, {1:.3f}, {2:.3f}]".format(*vec)


def format_err(e):
    """
    Da formato a un flotantes con notación científica

    :param e: el número flotante a formatear
    :type e: float
    :return: cadena de caracteres conteniendo el flotante
	con hasta 3 decimales en notación científica
    :rtype: str
    """
    return "{0:.3E}".format(e)
