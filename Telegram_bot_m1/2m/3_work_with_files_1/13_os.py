"""
Также существует огромное количество модулей, которые как поставляются вместе с python,
так и устанавливаются отдельно и позволяют расширить возможности языка.

Например, встроенный в язык модуль os позволяет работать с файлами и директориями в операционной системе.
Функция rename() используется для переименования файлов в Python. Для ее использования сперва нужно импортировать модуль os.

import os
os.rename(src,dest)


src = файл, который нужно переименовать
dest = новое имя файла

"""

import os
os.rename("Pyshkin.txt", "text.txt")
