import customtkinter as ctk
from templates.ERR.err_permission import *
from src.func import *
from src.data import *

class root_login(ctk.CTkToplevel):
  def __init__(self):
    super().__init__()
    self.title('Login')
    self.geometry(Functions.MeioTela(self, 550, 315))
    self.resizable(False, False)
    self.grab_set()

    self.erro_ocorreu = False
    self.v_novo = False 

    self.Frm_login_principal = ctk.CTkFrame(master=self, width=490, height=255)
    self.Frm_login_principal.place(x=30, y=30)

    self.Lbl_credenciais = ctk.CTkLabel(master=self.Frm_login_principal, text='Credenciais', font=('Arial', 30), text_color='#1F6AA5')
    self.Lbl_credenciais.place(x=245, y=40, anchor='center')
    self.Lbl_atendente   = ctk.CTkLabel(master=self.Frm_login_principal, text='Atendente :', font=('Arial', 18))
    self.Lbl_atendente.place(x=30, y=85)
    self.Lbl_mes         = ctk.CTkLabel(master=self.Frm_login_principal, text='Mês :', font=('Arial', 18))
    self.Lbl_mes.place(x=77, y=145)
    self.Lbl_usuNovo     = ctk.CTkLabel(master=self.Frm_login_principal, text='Novo Usuário?', font=('Arial', 16))
    self.Lbl_usuNovo.place(x=30, y=205)

    self.Ety_atendente = ctk.CTkEntry(master=self.Frm_login_principal, width=320, height=40, font=('Arial', 18),border_color='#414141', fg_color='#2B2B2B')
    self.Opt_atendente = ctk.CTkOptionMenu(master=self.Frm_login_principal, width=320, height=40,font=('Arial', 18),values=Planilha.buscar_usuários(), fg_color='#414141', button_color='#414141', button_hover_color='#414141')
    self.Opt_atendente.place(x=140, y=80)
    self.Opt_mes       = ctk.CTkOptionMenu(master=self.Frm_login_principal, width=320, height=40,font=('Arial', 18),values=Functions.Mes(), fg_color='#414141', button_color='#414141', button_hover_color='#414141')
    self.Opt_mes.place(x=140, y=140)

    self.Cbx_usuNovo = ctk.CTkCheckBox(master=self.Frm_login_principal, text='', bg_color="transparent", height=30)
    self.Cbx_usuNovo.place(x=140, y=205)

    self.Btt_entrar = ctk.CTkButton(master=self.Frm_login_principal, width=280, height=30, text='Entrar', font=('Arial', 17), command=self.act_Btt_entrar)
    self.Btt_entrar.place(x=180, y=205)

    self.Opt_atendente.bind('<Return>', lambda event: Functions.mudar_foco(self.Ety_mes))
    self.Opt_mes.bind('<Return>', lambda event: Functions.mudar_foco(self.Btt_entrar))
    self.Btt_entrar.bind("<Return>", lambda event: self.Btt_entrar.invoke())
    self.Cbx_usuNovo.configure(command=self.act_Cbx_usuNovo)

    self.confirma = False

  def act_Btt_entrar(self):
    if self.Cbx_usuNovo.get() == 1:
      self.v_atendente_login = self.Ety_atendente.get()
    else:
      self.v_atendente_login = self.Opt_atendente.get()

    self.v_mes_login = self.Opt_mes.get()
    try:
      Planilha.credenciais_data(self.v_atendente_login, self.v_mes_login, self.v_novo)
    except PermissionError:
      root_erro = root_permission_error(index_error=1)
      self.wait_window(root_erro)
      self.erro_ocorreu = True
    except CredentialsError:
      root_erro = root_permission_error(index_error=6)
      self.wait_window(root_erro)
      self.erro_ocorreu = True
    except Exception as e:
      self.erro_ocorreu = True

    if not self.erro_ocorreu:
      self.confirma = True
      self.destroy()
      
  def act_Cbx_usuNovo(self):
    if self.Cbx_usuNovo.get() == 1:
      self.v_novo = True   
      self.Opt_atendente.place_forget()
      self.Ety_atendente.place(x=140, y=80)
    else:
      self.v_novo = False 
      self.Ety_atendente.place_forget()
      self.Opt_atendente.place(x=140, y=80)