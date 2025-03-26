import customtkinter as ctk
from src.func import *

class root_permission_error(ctk.CTkToplevel):
  def __init__(self, index_error=0):
    super().__init__()

    self.title(self.Erro(index_error)[0])
    self.geometry(Functions.MeioTela(main=self, x=300 ,y=130))
    self.resizable(False, False)
    self.focus_force()
    self.grab_set()

    self.Lbl_msg = ctk.CTkLabel(master=self, text=self.Erro(index_error)[1], font=('Arial', 15))
    self.Lbl_msg.place(x=150, y= 30, anchor='center')

    self.Btt_ok  = ctk.CTkButton(master=self, text='Ok', command=self.act_Btt_ok)
    self.Btt_ok.place(x=80, y=70)
    
    self.mainloop()

  def Erro(self, err_index:int):
    match err_index:
      case 1: self.err = ['Permition_error' , 'Feche a planilha "Atendimentos.xlsx"!']
      case 2: self.err = ['Sintax_error','Data inválida!']
      case 3: self.err = ['Sintax_error','Hora inicial inválida!']
      case 4: self.err = ['Sintax_error','Hora final inválida!']
      case 5: self.err = ['Sintax_error','Cliente em branco!']
      case 6: self.err = ['credentials_error', 'Selecione um usuário ou cadastre um']
      case 7: self.err = ['Sintax_error', 'Descrição do atendimento em branco!']
      case 8: self.err = ['Logic_error', 'Hora inicial maior que hora final!']
      case _: self.err = ['Not_log','Erro não catalogado!']
    return self.err
 
  def act_Btt_ok(self):
    self.destroy()