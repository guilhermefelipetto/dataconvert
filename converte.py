import os
import csv

from time import sleep
from openpyxl import Workbook


def csv_to_xlsx(csv_dir_path, xlsx_file):
    wb = Workbook()
    ws = wb.active

    try:
        with open(csv_dir_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ws.append(row)

        wb.save(xlsx_file)
        print(f'O arquivo {xlsx_file} foi criado com sucesso!')

        sleep(3)
        os.system('cls')
    
    except Exception as e:
        print(f'Ocorreu um erro ao converter {csv_dir_path}: {e}')


def files(directory):
    if not os.path.exists('appsave_xlsx'):
        os.makedirs('appsave_xlsx')

    for file in os.listdir(f'./{directory}'):
        print(f'Lendo arquivo {file}')
        if file.endswith('.csv'):
            name_xlsx = file[:-4] + '.xlsx'
            try:
                csv_to_xlsx(f'./{directory}/{file}', f'./appsave_xlsx/{name_xlsx}')
                print(f'Arquivo {file} foi convertido com sucesso!')
            except Exception as e:
                print(f'Erro ao processar o arquivo {file}: {e}')
