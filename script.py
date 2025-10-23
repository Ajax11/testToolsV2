# ruff_test_cases.py
# Archivo de ejemplo con múltiples patrones que Ruff (pyflakes/pycodestyle) puede detectar.
# No todos los casos son errores en tiempo de ejecución, pero sí son malas prácticas que Ruff
# suele señalar (imports no usados, variables sin usar, redefinitions, etc.).

# -----------------------------
# Imports no usados / import wildcard
# -----------------------------
from math import *  # wildcard import (malo)

# -----------------------------
# Variables y asignaciones no usadas
# -----------------------------
UNUSED_GLOBAL = 42

def funcion_con_variable_no_usada():
    x = 10  # variable no usada
    y = 20
    return y

# -----------------------------
# Argumentos no usados
# -----------------------------
def funcion_args_no_usados(a, b, c):
    # solo usamos 'a'
    return a * 2

# -----------------------------
# Asignación a nombre reservado / shadowing
# -----------------------------
list = [1, 2, 3]  # shadowing del builtin 'list'

# -----------------------------
# Mutable default argument
# -----------------------------
def agregar(valor, contenedor=[]):
    contenedor.append(valor)
    return contenedor

# -----------------------------
# Reasignación de nombre de función
# -----------------------------
def ejemplo():
    """Función que más tarde se reasigna a un entero"""
    return "ok"

ejemplo = 123  # reasignación de función a entero (posible error semántico)

# -----------------------------
# Claves duplicadas en dict
# -----------------------------
diccionario = {"a": 1, "b": 2, "a": 3}

# -----------------------------
# Except sin especificar la excepción (bare except)
# -----------------------------
def division_segura(x, y):
    try:
        return x / y
    except:
        # Captura cualquier excepción y la ignora (mala práctica)
        return None

# -----------------------------
# Código inalcanzable
# -----------------------------
def funcion_inalcanzable():
    return 1
    a = 2  # código inalcanzable

# -----------------------------
# Comprensión cuyo resultado no se usa
# -----------------------------
def comprension_no_usada():
    [i * 2 for i in range(5)]  # expresión descartada

# -----------------------------
# Declaración con múltiples sentencias en la misma línea
# -----------------------------
a = 1; b = 2

# -----------------------------
# Línea demasiado larga (pep8 E501)
# -----------------------------
def linea_larga():
    x = "Esta es una línea deliberadamente muy larga para provocar una advertencia de estilo que excede 88 caracteres"  # noqa: E501
    return x

# -----------------------------
# Uso de variable antes de la asignación (NameError estático detectado por Ruff)
# -----------------------------
def uso_antes_asignar():
    try:
        return valor_no_definido  # nombre no definido
    except NameError:
        return "capturado"

# -----------------------------
# Import usado y no usado mezclados
# -----------------------------
import json

def usar_json():
    return json.dumps({"ok": True})

# -----------------------------
# Trailing whitespace (espacio al final de la línea) -> ruff/pycodestyle lo detecta
# -----------------------------
def trailing_space_example():
    x = 1
    return x


# -----------------------------
# Line de codigo muy larga
# -----------------------------
def trailing_len_line_example():
    xStamp = 1
    xxStamp = xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp + xStamp
    return xStamp


# -----------------------------
# Fin del archivo
# -----------------------------
