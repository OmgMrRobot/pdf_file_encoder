from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass
from pyfiglet import Figlet
from tkinter import filedialog





def pdf_coder(file_name: str, password: str):
    """Функция получает на вход pdf файл, перезаписывает и защищает его паролем """

    pdfwriter = PdfWriter() 
    pdf = PdfReader(file_name)

    for page in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page])

    password = getpass(prompt='Input password: ')
    pdfwriter.encrypt(password)

    with open(file_name[:-4]+"c.pdf", 'wb') as file:
        pdfwriter.write(file)


if __name__ == '__main__':

    prew_text = Figlet('slant')
    print('\33[32m' + prew_text.renderText("PDf CODER") + '\033[0m')

    file_name = filedialog.askopenfilename()

    if file_name:
        password = getpass(prompt='Input password: ')
        pdf_coder(file_name, password)
        print('\x1b[6;30;42m' + '\tSuccess!\t' + '\x1b[0m')
    else:
        print('\x1b[1;37;41m' + '\tError! Check existence file\t' + "\x1b[0m")