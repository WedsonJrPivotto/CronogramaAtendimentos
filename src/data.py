from openpyxl import load_workbook
from openpyxl.styles import Font
import shutil
import os


class Planilha:
  @staticmethod
  def cnx_data():
    caminho_original = './data/Atendimentos.xlsx'
    caminho_backup = './data/backup/Atendimentos.xlsx'
    try:
      wb = load_workbook(filename=caminho_original)
    except FileNotFoundError:
      if os.path.exists(caminho_backup):
        shutil.copy(caminho_backup, caminho_original)
        wb = load_workbook(filename=caminho_original)
    return wb

  @staticmethod
  def credenciais_data(nome:str, mes:str):
    wb = Planilha.cnx_data()
    sheet = wb['Planilha1']
    sheet['A1'] = f"Atendente: {nome}"
    sheet['D1'] = f"Mês: {mes}"

    fonte = Font(bold=True, underline='single')  # 'single' para sublinhado simples
    sheet['A1'].font = fonte
    sheet['D1'].font = fonte
    
    wb.save('./data/Atendimentos.xlsx')

  @staticmethod
  def add_atendimento_data(cliente:str, date:str, hr_ini:str, hr_fin:str, desc:str):
    wb = Planilha.cnx_data()
    sheet = wb['Planilha1']
    linha = 3
    while sheet[f'A{linha}'].value is not None:
      linha += 1

    # Adicionar os valores na linha encontrada
    sheet[f'A{linha}'] = cliente
    sheet[f'B{linha}'] = date
    sheet[f'C{linha}'] = hr_ini
    sheet[f'D{linha}'] = hr_fin
    sheet[f'E{linha}'] = desc

    wb.save('./data/Atendimentos.xlsx')