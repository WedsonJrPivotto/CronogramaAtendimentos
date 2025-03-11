import customtkinter as ctk
from src.func import *

class root_permission_error(ctk.CTkToplevel):
  def __init__(self):
    super().__init__()

    self.title('Permition error')
    self.geometry(Functions.MeioTela(main=self, x=300 ,y=130))
    self.resizable(False, False)
    self.focus_force()
    self.grab_set()

    self.Lbl_msg = ctk.CTkLabel(master=self, text='Feche a planilha "Atendimentos.xlsx"!', font=('Arial', 15))
    self.Lbl_msg.place(x=30, y= 30)

    self.Btt_ok  = ctk.CTkButton(master=self, text='Ok', command=self.act_Btt_ok)
    self.Btt_ok.place(x=80, y=70)
    
    self.mainloop()

  def act_Btt_ok(self):
    self.destroy()