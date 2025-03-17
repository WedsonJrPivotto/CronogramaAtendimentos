import customtkinter as ctk
from src.func import *
from templates.login import *
from templates.ERR.err_permission import *

class root_principal(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Principal')
    ctk.set_appearance_mode('dark')
    self.geometry(Functions.MeioTela(self, 1100, 600))
    self.resizable(False, False)

    self.erro_aconteceu = False

    # Frames
    self.Frm_entrys  = ctk.CTkFrame(master=self, width=810, height=400).place(x=30, y=160)
    self.Frm_buttons = ctk.CTkFrame(master=self, width=200, height=400).place(x=870, y=160)
    self.Frm_titulo  = ctk.CTkFrame(master=self, width=1040, height=100).place(x=30, y=30)

    # Labels
    self.Lbl_titulo  = ctk.CTkLabel(master=self.Frm_titulo, text='Cronograma de Atendimentos',bg_color='#2B2B2B', text_color='#1F6AA5',font=('Arial', 50) )
    self.Lbl_titulo.place(x=210, y=50)   
    self.Lbl_cliente = ctk.CTkLabel(master=self.Frm_entrys, text='Cliente',bg_color='#2B2B2B' ,font=('Arial', 20))
    self.Lbl_cliente.place(x=80, y=180)
    self.Lbl_data    = ctk.CTkLabel(master=self.Frm_entrys, text='Data   ',bg_color='#2B2B2B' ,font=('Arial', 20))
    self.Lbl_data.place(x=80, y=300)
    self.Lbl_ini     = ctk.CTkLabel(master=self.Frm_entrys, text='Inicio ',bg_color='#2B2B2B' ,font=('Arial', 20))
    self.Lbl_ini.place(x=340, y=300)
    self.Lbl_fim     = ctk.CTkLabel(master=self.Frm_entrys, text='Final  ',bg_color='#2B2B2B' ,font=('Arial', 20))
    self.Lbl_fim.place(x=590, y=300)
    self.Lbl_descri  = ctk.CTkLabel(master=self.Frm_entrys, text='Descição do atendimento',bg_color='#2B2B2B' ,font=('Arial', 20))
    self.Lbl_descri.place(x=80, y=420)

    # Entrys
    self.Ety_cliente = ctk.CTkEntry(master=self.Frm_entrys, width=710, height=60, font=('Arial', 40),border_color='#414141', fg_color='#2B2B2B'  )
    self.Ety_cliente.place(x=80, y=220)
    self.Ety_data    = ctk.CTkEntry(master=self.Frm_entrys, width=210, height=60, font=('Arial', 40),border_color='#414141', fg_color='#2B2B2B'  )
    self.Ety_data.place(x=80, y=340)
    self.Ety_ini     = ctk.CTkEntry(master=self.Frm_entrys, width=200, height=60, font=('Arial', 40),border_color='#414141', fg_color='#2B2B2B'  )
    self.Ety_ini.place(x=340, y=340)
    self.Ety_fim     = ctk.CTkEntry(master=self.Frm_entrys, width=200, height=60, font=('Arial', 40),border_color='#414141', fg_color='#2B2B2B'  )
    self.Ety_fim.place(x=590, y=340)
    self.Ety_descri  = ctk.CTkEntry(master=self.Frm_entrys, width=710, height=60, font=('Arial', 40),border_color='#414141', fg_color='#2B2B2B'  )
    self.Ety_descri.place(x=80, y=460)

    # Buttons
    self.Btt_inclui  = ctk.CTkButton(master=self.Frm_buttons, width=160, height=50, text='Gravar', font=('Arial', 20), command=self.act_Btt_inclui)
    self.Btt_inclui.place(x=890, y=180)
    self.Btt_limpar  = ctk.CTkButton(master=self.Frm_buttons, width=160, height=50, text='limpar Campos', font=('Arial', 20), command=self.act_Btt_limpar)
    self.Btt_limpar.place(x=890, y=250)
    self.Btt_trocar  = ctk.CTkButton(master=self.Frm_buttons, width=160, height=50, text='Trocar\nusuário/mês', font=('Arial', 18), command=self.act_Btt_troca)
    self.Btt_trocar.place(x=890, y=320)
    self.Btt_sair    = ctk.CTkButton(master=self.Frm_buttons, width=160, height=50, text='Fechar Aplicação', font=('Arial', 18), fg_color='#d20000', hover_color='#7d0000', command=self.act_Btt_sair )
    self.Btt_sair.place(x=890, y=480)
    
    # Binds
      # Formatar horas
    self.Ety_data.bind("<KeyRelease>", lambda event: Functions.formatar_data(event=event, entry=self.Ety_data))
    self.Ety_ini.bind("<KeyRelease>", lambda event: Functions.formatar_hora(event=event, entry=self.Ety_ini))
    self.Ety_fim.bind("<KeyRelease>", lambda event: Functions.formatar_hora(event=event, entry=self.Ety_fim))

      # Focus
    self.update()
    self.Ety_cliente.focus() # Focar no Cliente
    self.Ety_cliente.bind("<Return>", lambda event: Functions.mudar_foco(self.Ety_data)) # Forcar na data
    self.Ety_data.bind("<Return>", lambda event: Functions.mudar_foco(self.Ety_ini))# Forcar na hora inicial 
    self.Ety_ini.bind("<Return>", lambda event: Functions.mudar_foco(self.Ety_fim))# Forcar na hora final
    self.Ety_fim.bind("<Return>", lambda event: Functions.mudar_foco(self.Ety_descri))# Forcar na descrição
    self.Ety_descri.bind("<Return>", lambda event: Functions.mudar_foco(self.Btt_inclui))# Forcar no botão "gravar"
    self.Btt_inclui.bind("<Return>", lambda event: self.Btt_inclui.invoke())

    self.login = root_login()
    self.wait_window(self.login)
    try:
      if self.login.confirma:
        self.Ety_data.insert(0, Functions.DataDeAgora())
        self.mainloop()
    except AttributeError:
      self.destroy()

  def act_Btt_inclui(self):
    self.cliente = self.Ety_cliente.get()
    if self.Ety_cliente.get() == '':
      root_erro = root_permission_error(index_error=5)
      self.wait_window(root_erro)
      self.erro_aconteceu = True

    self.data    = self.Ety_data.get()
    if len(self.Ety_data.get()) >= 10:
      try: # Validações da data                                      mês de 31 dias                                                                                             mês de 30 dias                                                                        fevereiro                                                     Validação do ano
        if not ((int(self.Ety_data.get()[0:2]) <= 31 and self.Ety_data.get()[3:5] in ['01','03','05','07','08','10','12']) or (int(self.Ety_data.get()[0:2]) <= 30 and self.Ety_data.get()[3:5] in ['04','06','09','11']) or (int(self.Ety_data.get()[0:2]) <= 29 and self.Ety_data.get()[3:5] == '02')) and (int(self.Ety_data.get()[6:10]) - int(self.Ety_data.get()[6:10]) == 0):
          root_erro = root_permission_error(index_error=2)
          self.wait_window(root_erro)
          self.erro_aconteceu = True
      except ValueError:
        root_erro = root_permission_error(index_error=2)
        self.wait_window(root_erro)
        self.erro_aconteceu = True
    else:
      root_erro = root_permission_error(index_error=2)
      self.wait_window(root_erro)
      self.erro_aconteceu = True

    self.ini     = self.Ety_ini.get()
    if len(self.Ety_ini.get()) >= 5:
      try:
        if not (int(self.Ety_ini.get()[0:2]) <= 23 and int(self.Ety_ini.get()[0:2]) >= 0 and int(self.Ety_ini.get()[3:5]) <= 59 and int(self.Ety_ini.get()[3:5]) >= 0):
          root_erro = root_permission_error(index_error=3)
          self.wait_window(root_erro)
          self.erro_aconteceu = True
      except ValueError:
        root_erro = root_permission_error(index_error=3)
        self.wait_window(root_erro)
        self.erro_aconteceu = True
    else:
      root_erro = root_permission_error(index_error=3)
      self.wait_window(root_erro)
      self.erro_aconteceu = True

    self.fin     = self.Ety_fim.get()
    if len(self.Ety_fim.get()) >= 5:
      try:
        if not (int(self.Ety_fim.get()[0:2]) <= 23 and int(self.Ety_fim.get()[0:2]) >= 0 and int(self.Ety_fim.get()[3:5]) <= 59 and int(self.Ety_fim.get()[3:5]) >= 0):
          root_erro = root_permission_error(index_error=4)
          self.wait_window(root_erro)
          self.erro_aconteceu = True
      except ValueError:
        root_erro = root_permission_error(index_error=4)
        self.wait_window(root_erro)
        self.erro_aconteceu = True
    else:
      root_erro = root_permission_error(index_error=4)
      self.wait_window(root_erro)
      self.erro_aconteceu = True

    self.desc    = self.Ety_descri.get()
    if not self.erro_aconteceu:
      Planilha.add_atendimento_data(
        cliente=self.cliente,
        date= self.data[:10],
        hr_ini=self.ini,
        hr_fin=self.fin,
        desc=self.desc
      )
      self.act_Btt_limpar()

  def act_Btt_limpar(self):
    self.Ety_cliente.delete(0, "end")
    self.Ety_data.delete(0,"end")
    self.Ety_data.insert(0,Functions.DataDeAgora())
    self.Ety_ini.delete(0, "end")
    self.Ety_fim.delete(0, "end")
    self.Ety_descri.delete(0, "end")
    self.update()
    self.Ety_cliente.focus()

  def act_Btt_troca(self):
    self.login_troca = root_login()  
    self.wait_window(self.login_troca)

  def act_Btt_sair(self):
    self.destroy()