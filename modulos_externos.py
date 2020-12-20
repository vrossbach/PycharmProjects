"""
Módulos Externos

--> Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

https://pypi.org --> pacotes externos oficiais

"""

# colorama --> usado para permitir impressão de textos coloridos no terminal

# pip install colorama --> digitar no terminal
"""
from colorama import init, Fore

init()

print(Fore.CYAN + 'Geek University')
print(Fore.LIGHTCYAN_EX + 'Geek University')
print(Fore.LIGHTGREEN_EX + 'Geek University')
print(Fore.LIGHTRED_EX + 'Geek University')
print(Fore.LIGHTMAGENTA_EX + 'Geek University')
print(Fore.MAGENTA + 'Geek University')
"""
from colorama import init, Fore

import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

