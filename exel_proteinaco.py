import xlsxwriter
from parsing_proteinaco import array
import os


def writer(parameter):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_file_path = os.path.join(script_dir, "data.xlsx")
    book = xlsxwriter.Workbook(excel_file_path)
    page = book.add_worksheet("butter")

    row = 0
    column = 0

    page.set_column("A:A", 30)
    page.set_column("B:B", 10)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in parameter():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1

    book.close()


writer(array)