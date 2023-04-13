import os
import requests
from PIL import Image

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar
import customtkinter as ctk

from crud import * 

# Constants
PATH = os.path.dirname(os.path.realpath(__file__))

class TabFormInfo(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # ========== create tab 1 - ER ===========
        self.add("Embaixador do Rei")        

        # ======== add widgets on tabs ===========
        self.label = ctk.CTkLabel(master=self.tab("Embaixador do Rei"))

        # ============ frame_top_info ============
        self.frame_top_info = ctk.CTkFrame(master=self.tab("Embaixador do Rei"))
        self.frame_top_info.grid(row=0, column=0, sticky="nwse", padx=(20, 20), pady=(20, 10))

        # ==== configure grid layout (8x2) ======
        self.frame_top_info.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.frame_top_info.columnconfigure((0, 1), weight=1)

        # ======= Basic information form ========        
        self.label_informacoes = ctk.CTkLabel(master=self.frame_top_info, text="Informações Básicas")
        self.label_informacoes.grid(row=0, column=0, columnspan=2, pady=10, padx=0, sticky="nwse")

        # Name 
        self.label_nome = ctk.CTkLabel(master=self.frame_top_info, text="Nome Completo:")
        self.label_nome.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        TabFormInfo.entry_nome = ctk.CTkEntry(master=self.frame_top_info, width=320)
        TabFormInfo.entry_nome.grid(row=1, column=1, columnspan=2, pady=5, padx=15, sticky="ew")

        # Parents name
        self.label_resp = ctk.CTkLabel(master=self.frame_top_info, text="Nome do Responsável:")
        self.label_resp.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        TabFormInfo.entry_resp = ctk.CTkEntry(master=self.frame_top_info, width=320)
        TabFormInfo.entry_resp.grid(row=2, column=1,  columnspan=2, pady=5, padx=15, sticky="ew")

        # Adress information
        self.label_cep = ctk.CTkLabel(master=self.frame_top_info, text="CEP:")
        self.label_cep.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        TabFormInfo.entry_cep = ctk.CTkEntry(master=self.frame_top_info, width=145)
        TabFormInfo.entry_cep.grid(row=3, column=1, pady=5, padx=15, sticky="w")
        
        self.button_end = ctk.CTkButton(master=self.frame_top_info, width=125, text="Buscar endereço", command=lambda: self.find_localization())
        self.button_end.grid(row=3, column=1, pady=5, padx=15, sticky="e")
       
        self.label_endereco = ctk.CTkLabel(master=self.frame_top_info, text="Endereço:")
        self.label_endereco.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        TabFormInfo.entry_logradouro = ctk.CTkEntry(master=self.frame_top_info, placeholder_text="Logradouro", width=265)
        TabFormInfo.entry_logradouro.grid(row=4, column=1, pady=5, padx=15, sticky="w")

        TabFormInfo.entry_numero = ctk.CTkEntry(master=self.frame_top_info, placeholder_text="Nº", width=30)
        TabFormInfo.entry_numero.grid(row=4, column=1, pady=5, padx=15, sticky="e")

        self.label_bairro = ctk.CTkLabel(master=self.frame_top_info, text="Bairro:")
        self.label_bairro.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        TabFormInfo.entry_bairro = ctk.CTkEntry(master=self.frame_top_info, width=320)
        TabFormInfo.entry_bairro.grid(row=5, column=1, pady=5, padx=15, sticky="ew")

        self.label_cidade = ctk.CTkLabel(master=self.frame_top_info, text="Cidade:")
        self.label_cidade.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        TabFormInfo.entry_cidade = ctk.CTkEntry(master=self.frame_top_info, width=265)
        TabFormInfo.entry_cidade.grid(row=6, column=1, pady=5, padx=15, sticky="w")

        TabFormInfo.entry_UF = ctk.CTkEntry(master=self.frame_top_info, placeholder_text="UF", width=30)
        TabFormInfo.entry_UF.grid(row=6, column=1, pady=5, padx=15, sticky="e")

        self.label_complemento = ctk.CTkLabel(master=self.frame_top_info, text="Complemento:")
        self.label_complemento.grid(row=7, column=0, pady=(5, 15), padx=10, sticky="w")

        TabFormInfo.entry_complemento = ctk.CTkEntry(master=self.frame_top_info, width=205)
        TabFormInfo.entry_complemento.grid(row=7, column=1, pady=(5, 15), padx=15, sticky="w")

        self.button_cep = ctk.CTkButton(master=self.frame_top_info, width=80, text="Buscar CEP", command=lambda: self.find_cep())
        self.button_cep.grid(row=7, column=1, pady=(5, 15), padx=15, sticky="e")            

        # ============ frame_bottom_date ============
        self.frame_bottom_date = ctk.CTkFrame(master=self.tab("Embaixador do Rei"))
        self.frame_bottom_date.grid(row=1, column=0, sticky="nwse", padx=20, pady=(10, 20))

        # ======= configure grid layout (2x3) =======
        self.frame_bottom_date.rowconfigure((0, 1), weight=1)
        self.frame_bottom_date.columnconfigure((0, 1, 2), weight=1)

        # ============= Date label ==================       
        self.label_date = ctk.CTkLabel(master=self.frame_bottom_date, text="Data de Nascimento")
        self.label_date.grid(row=0, column=0, columnspan=3, pady=(15, 5), padx=0, sticky="nswe")

        # Birth date
        self.label_nasc = ctk.CTkLabel(master=self.frame_bottom_date, text="Data de Nascimento:")
        self.label_nasc.grid(row=1, column=0, pady=(5, 15), padx=10, sticky="w")

        TabFormInfo.entry_nasc = ctk.CTkEntry(master=self.frame_bottom_date, width=150, state="disabled")
        TabFormInfo.entry_nasc.grid(row=1, column=1, pady=(5, 15), padx=10, sticky="w")

        self.button_date = ctk.CTkButton(master=self.frame_bottom_date, width=120, text="Selecionar Data", command=lambda: self.create_toplevel_date("nascimento"))
        self.button_date.grid(row=1, column=2, pady=(5, 15), padx=15, sticky="e")

        # ============ frame_bottom_tel ============        
        self.frame_bottom_tel = ctk.CTkFrame(master=self.tab("Embaixador do Rei"))
        self.frame_bottom_tel.grid(row=2, column=0, sticky="nwse", padx=20, pady=(10, 20))

        # ======= configure grid layout (2x3) =======
        self.frame_bottom_tel.rowconfigure((0, 1, 2), weight=1)
        self.frame_bottom_tel.columnconfigure((0, 1, 2), weight=1)

        # ============= Telephone label ==================        
        self.label_tel = ctk.CTkLabel(master=self.frame_bottom_tel, text="Telefones Para Contato")
        self.label_tel.grid(row=0, column=0, columnspan=3, pady=(15, 5), padx=0, sticky="nswe")

        # Parents telephone
        self.label_tel_resp = ctk.CTkLabel(master=self.frame_bottom_tel, text="Tel. do Responsável:")
        self.label_tel_resp.grid(row=1, column=0, pady=(5, 15), padx=10, sticky="w")

        TabFormInfo.entry_tel_resp = ctk.CTkEntry(master=self.frame_bottom_tel, width=150)
        TabFormInfo.entry_tel_resp.grid(row=1, column=1, pady=(5, 15), padx=10, sticky="w")       

        self.combobox_tel = ctk.CTkOptionMenu(master=self.frame_bottom_tel, values=["Celular", "Fixo"])
        self.combobox_tel.grid(row=1, column=2, pady=(5, 15), padx=15, sticky="e")

        # telephone
        self.label_tel_ER = ctk.CTkLabel(master=self.frame_bottom_tel, text="Tel. do Embaixador do Rei:")
        self.label_tel_ER.grid(row=2, column=0, pady=(5, 15), padx=10, sticky="w")

        TabFormInfo.entry_tel_ER = ctk.CTkEntry(master=self.frame_bottom_tel, width=150)
        TabFormInfo.entry_tel_ER.grid(row=2, column=1, pady=(5, 15), padx=10, sticky="w")       

        self.combobox_tel_ER = ctk.CTkOptionMenu(master=self.frame_bottom_tel, values=["Celular", "Fixo"])
        self.combobox_tel_ER.grid(row=2, column=2, pady=(5, 15), padx=15, sticky="e")

        
        # ========== create tab 2 - Igreja ==========
        self.add("Igreja")

        # ======== add widgets on tabs ==============
        self.label = ctk.CTkLabel(master=self.tab("Igreja"))
        
        # ============ frame_church_info ============
        self.frame_church_info = ctk.CTkFrame(master=self.tab("Igreja"))
        self.frame_church_info.grid(sticky="nwse", padx=(20, 20), pady=(20, 20))

        # ====== configure grid layout (8x2) ========
        self.frame_church_info.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.frame_church_info.columnconfigure((0, 1), weight=1)
        
        # ===== Basic church information form =======
        self.label_infoER = ctk.CTkLabel(master=self.frame_church_info, text="Igreja e Organização ER")
        self.label_infoER.grid(row=0, column=0, columnspan=2, pady=10, padx=0, sticky="nwse")

        self.label_igreja = ctk.CTkLabel(master=self.frame_church_info, text="É membro de alguma igreja? Se sim, qual?")
        self.label_igreja.grid(row=1, column=0, pady=5, padx=15, sticky="w")               
              
        check_igreja = tk.StringVar()
        self.check_box_igreja = ctk.CTkCheckBox(master=self.frame_church_info, text="", variable=check_igreja, command=lambda: check_church_event("igreja"), onvalue="normal", offvalue="disabled")
        self.check_box_igreja.grid(row=1, column=1, pady=5, padx=15, sticky="w")
        self.check_box_igreja.deselect()
                       
        TabFormInfo.entry_igreja = ctk.CTkEntry(master=self.frame_church_info, width=240, state="disabled")
        TabFormInfo.entry_igreja.grid(row=1, column=1, pady=5, padx=15, sticky="e")

        # Batism
        self.label_batizado = ctk.CTkLabel(master=self.frame_church_info, text="Foi batizado? Se sim, em qual igreja?")
        self.label_batizado.grid(row=2, column=0, pady=5, padx=15, sticky="w")
    
        check_batismo = tk.StringVar()
        TabFormInfo.check_box_batizado = ctk.CTkCheckBox(master=self.frame_church_info, text="", variable=check_batismo, command=lambda: check_church_event("batismo"), onvalue="normal", offvalue="disabled")
        TabFormInfo.check_box_batizado.grid(row=2, column=1, pady=5, padx=15, sticky="w")
        TabFormInfo.check_box_batizado.deselect()

        TabFormInfo.entry_igreja_batismo = ctk.CTkEntry(master=self.frame_church_info, width=240, state="disabled")
        TabFormInfo.entry_igreja_batismo.grid(row=2, column=1, pady=5, padx=15, sticky="e")

        self.label_data_batismo = ctk.CTkLabel(master=self.frame_church_info, text="E qual a data do batismo?")
        self.label_data_batismo.grid(row=3, column=0, pady=5, padx=15, sticky="w")

        TabFormInfo.entry_data_batismo = ctk.CTkEntry(master=self.frame_church_info, width=130, state="disabled")
        TabFormInfo.entry_data_batismo.grid(row=3, column=1, pady=5, padx=15, sticky="w")

        self.button_data_batismo = ctk.CTkButton(master=self.frame_church_info, width=125, text="Selecionar Data", command=lambda: self.create_toplevel_date("batismo"), state="disabled")
        self.button_data_batismo.grid(row=3, column=1, pady=5, padx=15, sticky="e") 

        # EBD
        self.label_EBD = ctk.CTkLabel(master=self.frame_church_info, text="Frequenta EBD? Se sim, em qual igreja?")
        self.label_EBD.grid(row=4, column=0, pady=5, padx=15, sticky="w")

        TabFormInfo.entry_EBD = ctk.CTkEntry(master=self.frame_church_info, width=280, state="normal")
        TabFormInfo.entry_EBD.grid(row=4, column=1, pady=5, padx=15, sticky="e")

        self.label_atividades = ctk.CTkLabel(master=self.frame_church_info,text="Participa de outras atividades/organizações?")
        self.label_atividades.grid(row=5, column=0, columnspan=2, pady=5, padx=15, sticky="w")

        # Activities
        check_atividades = tk.StringVar()
        self.check_box_atividades = ctk.CTkCheckBox(master=self.frame_church_info, text="", variable=check_atividades, command=lambda: check_church_event("atividades"), onvalue="normal", offvalue="disabled")
        self.check_box_atividades.grid(row=6, column=0, pady=5, padx=15, sticky="w")
        self.check_box_atividades.deselect()
        
        TabFormInfo.combobox_atividades = ctk.CTkComboBox(master=self.frame_church_info, state="disabled", width=200, values=["Ministério Infantil", "Música", "Outros"])
        TabFormInfo.combobox_atividades.grid(row=6, column=0, pady=5, padx=20, sticky="e")

        self.label_atividades_igreja = ctk.CTkLabel(master=self.frame_church_info, text="Em qual igreja?")
        self.label_atividades_igreja.grid(row=6, column=1, pady=5, padx=0, sticky="w")

        TabFormInfo.entry_atividades_igreja = ctk.CTkEntry(master=self.frame_church_info, width=200, state="disabled")
        TabFormInfo.entry_atividades_igreja.grid(row=6, column=1, pady=5, padx=15, sticky="e")

        self.label_outros = ctk.CTkLabel(master=self.frame_church_info, text="Caso tenha selecionado outros, especifique:")
        self.label_outros.grid(row=7, column=0, pady=5, padx=15, sticky="w")

        TabFormInfo.textbox_church = ctk.CTkTextbox(master=self.frame_church_info, state="normal")
        TabFormInfo.textbox_church.grid(row=8, column=0, columnspan=2, padx=20, pady=(15, 20), sticky="nsew")

        # Function to check button event
        def check_church_event(campo):
   
            state_var_igreja = check_igreja.get()
            state_var_batismo = check_batismo.get()  
            state_var_atividades = check_atividades.get()             

            if campo == "igreja":
                self.entry_igreja.configure(state=state_var_igreja)

            if campo == "batismo":
                self.entry_igreja_batismo.configure(state=state_var_batismo)
                self.button_data_batismo.configure(state=state_var_batismo)
               
            if campo == "atividades":
                self.combobox_atividades.configure(state=state_var_atividades)
                self.entry_atividades_igreja.configure(state=state_var_atividades)

        
        # ======= create tab 3 - Organização ========
        self.add("Organização")

        # ======== add widgets on tabs ==============
        self.label = ctk.CTkLabel(master=self.tab("Organização"))
        
        # ============ frame_church_info ============
        self.frame_organization_info = ctk.CTkFrame(master=self.tab("Organização"))
        self.frame_organization_info.grid(sticky="nwse", padx=(20, 20), pady=(20, 20))

        # ===== configure grid layout (7x3) =========
        self.frame_organization_info.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame_organization_info.columnconfigure((0, 1, 2), weight=1)

        # === Basic organization information form ===
        self.label_infoER = ctk.CTkLabel(master=self.frame_organization_info, text="Organização ER")
        self.label_infoER.grid(row=0, column=0, columnspan=3, pady=10, padx=0, sticky="nwse")

        # Ingresso
        self.label_data_ingresso = ctk.CTkLabel(master=self.frame_organization_info, text="Frequenta as reuniões desde:")
        self.label_data_ingresso.grid(row=1, column=0, pady=5, padx=15, sticky="w")

        TabFormInfo.entry_data_ingresso = ctk.CTkEntry(master=self.frame_organization_info, width=150, state="disabled")
        TabFormInfo.entry_data_ingresso.grid(row=1, column=1, pady=5, padx=15, sticky="w")

        self.button_data_ingresso = ctk.CTkButton(master=self.frame_organization_info, width=135, text="Selecionar Data", command=lambda: self.create_toplevel_date("ingresso"))
        self.button_data_ingresso.grid(row=1, column=2, pady=5, padx=15, sticky="e") 

        # Aclamação        
        self.label_data_aclamação = ctk.CTkLabel(master=self.frame_organization_info, text="É membro da embaixada desde:")
        self.label_data_aclamação.grid(row=2, column=0, pady=5, padx=15, sticky="w")

        TabFormInfo.entry_data_aclamacao = ctk.CTkEntry(master=self.frame_organization_info, width=150, state="disabled")
        TabFormInfo.entry_data_aclamacao.grid(row=2, column=1, pady=5, padx=15, sticky="w")

        self.button_data_aclamacao = ctk.CTkButton(master=self.frame_organization_info, width=135, text="Selecionar Data", command=lambda: self.create_toplevel_date("aclamacao"))
        self.button_data_aclamacao.grid(row=2, column=2, pady=5, padx=15, sticky="e") 

        # Posto
        self.label_posto = ctk.CTkLabel(master=self.frame_organization_info, text="Posto do embaixador do Rei na organização:")
        self.label_posto.grid(row=3, column=0, columnspan=3, pady=5, padx=(15, 15), sticky="ew")

        TabFormInfo.combobox = ctk.CTkComboBox(master=self.frame_organization_info,  width=165, values=["Embaixador Escudeiro", "Embaixador Arauto", "Embaixador Sênior", "Embaixador Emérito"])
        TabFormInfo.combobox.grid(row=4, column=0, padx=20, pady=5, sticky="e")

        TabFormInfo.entry_data_formatura = ctk.CTkEntry(master=self.frame_organization_info, width=150, state="disabled")
        TabFormInfo.entry_data_formatura.grid(row=4, column=1, pady=5, padx=15, sticky="w")

        self.button_data_formatura = ctk.CTkButton(master=self.frame_organization_info, width=135, text="Selecionar Data", command=lambda: self.create_toplevel_date("formatura"))
        self.button_data_formatura.grid(row=4, column=2, pady=5, padx=15, sticky="e") 

        # Observações
        self.label_infoER = ctk.CTkLabel(master=self.frame_organization_info, text="Observações")
        self.label_infoER.grid(row=5, column=0, columnspan=3, pady=(5, 15), padx=(15, 15), sticky="nwse")

        TabFormInfo.textbox_org = ctk.CTkTextbox(master=self.frame_organization_info)
        TabFormInfo.textbox_org.grid(row=6, column=0, columnspan=3, padx=20, pady=(5, 20), sticky="nsew")


    # ========== Functions - Class Tabview ===========

    # =============== Find Local With CEP ============ 
    def find_localization(self):

        text = self.entry_cep.get()
        text = text.replace("-", "").replace(".", "").replace(" ", "")
    
        link = requests.get(f'https://viacep.com.br/ws/{text}/json/')

        # Verifica erro na requisição do CEP
        if link.status_code != 200:
            self.message_window = ctk.CTkToplevel(self)
            self.message_window.title('Erro de Requisição')
            self.message_window.after(10000, self.message_window.destroy)

            # create label on CTkToplevel window
            label = ctk.CTkLabel(self.message_window, text=f"Ocorreu um erro na requisição do CEP: {text}.\nVerifique o CEP e tente novamente.")
            label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        # Retorna o endereço do CEP em formato json/chaves/dicionário.
        dic_endereco = link.json()

        uf = dic_endereco['uf']
        cidade = dic_endereco['localidade']
        bairro = dic_endereco['bairro']
        logradouro = dic_endereco['logradouro']
        
        self.entry_UF.delete(0, 'end')
        self.entry_UF.insert(0, uf)

        self.entry_bairro.delete(0, 'end')
        self.entry_bairro.insert(0, bairro)

        self.entry_cidade.delete(0, 'end')
        self.entry_cidade.insert(0, cidade)

        self.entry_logradouro.delete(0, 'end')
        self.entry_logradouro.insert(0, logradouro)
        
    # =============== Find CEP ============
    def find_cep(self):

        uf = self.entry_UF.get()
        cidade = self.entry_cidade.get()        
        endereco = self.entry_logradouro.get()              

        link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

        requisicao = requests.get(link) 

        # Verifica erro na requisição do CEP
        if requisicao.status_code != 200:
            self.message_window = ctk.CTkToplevel(self)
            self.message_window.title('Erro de Requisição')
            self.message_window.after(10000, self.message_window.destroy)

            # create label on CTkToplevel window
            label = ctk.CTkLabel(self.message_window, text=f"Ocorreu um erro na requisição do CEP.\nVerifique o endereço e tente novamente.")
            label.pack(side="top", fill="both", expand=True, padx=40, pady=40)       

        dic_requisicao = requisicao.json()   

        self.entry_cep.delete(0, 'end')
        self.entry_cep.insert(0, dic_requisicao[0]['cep'])     
           
    # =========== Window of date pick  ==============
    def create_toplevel_date(self, campo_data):
        
        global date_window

        date_window = ctk.CTkToplevel(self)
        date_window.geometry("325x365")
        date_window.title("Selecionar Data")
        date_window.resizable(width = "false", height= "false")

        global cal

        self.frame_calendar = ctk.CTkFrame(master=date_window)
        self.frame_calendar.pack(padx=15, pady=15)

        # create label on CTkToplevel window
        label = ctk.CTkLabel(self.frame_calendar, text="Selecionar Data")
        label.pack(side="top", fill="both", padx=20, pady=5)
        
        cal = Calendar(self.frame_calendar, selectmode='day')
        cal.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        button_ok = ctk.CTkButton(self.frame_calendar, width=80, text="OK", command=lambda: self.update_date(campo_data))
        button_ok.pack(side="left", fill="both", expand=True, pady=20, padx=20)

        button_cancel = ctk.CTkButton(self.frame_calendar, width=80, text="Cancelar", fg_color="white", command=date_window.destroy)
        button_cancel.pack(side="right", fill="both", expand=True, pady=20, padx=20)

    # ================= Update Date Time ============
    def update_date(self, campo_data):

        new_date = cal.get_date()

        if campo_data == "nascimento":        
            self.entry_nasc.configure(state="normal")
            self.entry_nasc.delete(0, 11)
            self.entry_nasc.insert(0, new_date)
            self.entry_nasc.configure(state="disabled")

        if campo_data == "batismo":        
            self.entry_data_batismo.configure(state="normal")
            self.entry_data_batismo.delete(0, 11)
            self.entry_data_batismo.insert(0, new_date)
            self.entry_data_batismo.configure(state="disabled")

        if campo_data == "ingresso":        
            self.entry_data_ingresso.configure(state="normal")
            self.entry_data_ingresso.delete(0, 11)
            self.entry_data_ingresso.insert(0, new_date)
            self.entry_data_ingresso.configure(state="disabled")

        if campo_data == "aclamacao":        
            self.entry_data_aclamacao.configure(state="normal")
            self.entry_data_aclamacao.delete(0, 11)
            self.entry_data_aclamacao.insert(0, new_date)
            self.entry_data_aclamacao.configure(state="disabled")

        if campo_data == "formatura":        
            self.entry_data_formatura.configure(state="normal")
            self.entry_data_formatura.delete(0, 11)
            self.entry_data_formatura.insert(0, new_date)
            self.entry_data_formatura.configure(state="disabled")
            
        date_window.destroy()
    

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create 5x1 grid system
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.add_user_image = ctk.CTkImage(Image.open(PATH + "/images/add-user.png"), size=(28, 28))
        self.cancel_image = ctk.CTkImage(Image.open(PATH + "/images/cancel.png"), size=(28, 28))
        self.photo_icon = ctk.CTkImage(Image.open(PATH + "/images/user.png"), size=(28, 28))
        self.insignia_image = ctk.CTkImage(Image.open(PATH + "/images/Logo_ER_QIBN.png"), size=(170, 170))

        font_title = ctk.CTkFont(family="Segoe UI", size=18, weight="normal")
        font_name = ctk.CTkFont(family="Segoe UI", size=13, weight="bold")

        # add widgets on to the sidebar...
        self.label = ctk.CTkLabel(self, text="Cadastrar ER", height=30, corner_radius=6, fg_color=("gray70", "gray25"), font=font_title)
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # Buttons
        self.button_photo = ctk.CTkButton(master=self, image=self.photo_icon, text="Selecionar foto", width=100, height=80, border_width=2, corner_radius=10, compound="bottom", 
                                                       border_color="gray50", fg_color=("gray70", "gray25"), hover_color="gray25", command=self.select_image)
        self.button_photo.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.button_register = ctk.CTkButton(master=self, image=self.add_user_image, text="Cadastrar", width=100, height=80, border_width=2,
                                                        corner_radius=10, compound="bottom", border_color="gray50", fg_color=("gray70", "gray25"),
                                                        hover_color="gray25", command=self.button_register)
        self.button_register.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        Sidebar.button_clean = ctk.CTkButton(master=self, image=self.cancel_image, text="Cancelar", width=100, height=80, border_width=2,
                                                        corner_radius=10, compound="bottom", border_color="gray50", fg_color=("gray70", "gray25"),
                                                        hover_color="gray25", command=cancel)
        Sidebar.button_clean.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # Insígnia image and name
        self.insignia_label = ctk.CTkLabel(self, image=self.insignia_image, text="")
        self.insignia_label.grid(row=7, column=0, padx=0, pady=0, sticky="sew")

        self.insignia_label = ctk.CTkLabel(self, text="Embaixada\nPr. Edson P. Messor", font=font_name)
        self.insignia_label.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="nsew")

    # ========== Functions - Class Sidebar ===========

    def select_image(self):

        global image_path               
        image_path = fd.askopenfilename(filetypes=[('JPEG Files', '.jpg .jpeg'), ('PNG Files', '.png')])
                
    def button_register(self):   
        
        # ---------- ER - Tab --> Get information ------------
        nome_ER = TabFormInfo.entry_nome.get()
        nome_resp = TabFormInfo.entry_resp.get()
        data_nasc = TabFormInfo.entry_nasc.get()
        tel_resp = TabFormInfo.entry_tel_resp.get()
        tel_ER = TabFormInfo.entry_tel_ER.get()
        
        # Adress information
        cep = TabFormInfo.entry_cep.get()
        logradouro = TabFormInfo.entry_logradouro.get()
        numero = TabFormInfo.entry_numero.get()
        bairro = TabFormInfo.entry_bairro.get()
        cidade = TabFormInfo.entry_cidade.get()
        estado = TabFormInfo.entry_UF.get()
        complemento = TabFormInfo.entry_complemento.get()

        # Photo path verification
        try:
            image = image_path
        except NameError:
            messagebox.showerror('Erro', 'Preencha todos os campos e selecione uma imagem.')    
            return
        
        # Verification: UF, cidade, complemento and tel_ER
        if estado == '':
            estado = 'RJ'        
        if cidade == '':
            cidade = 'Nilópolis'
        if complemento == '':
            complemento = 'Não informado'
        if tel_ER == '':
            tel_ER = '99999-9999'        

        # List information
        list_basic_info = [nome_ER, nome_resp, data_nasc, tel_resp, tel_ER, cep, logradouro, numero, bairro, cidade, estado, complemento, image]         
        for i in list_basic_info:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos e selecione uma imagem.')
                return        

        # ------  Chuch - Tab --> Get information --------- 
        nome_igreja = TabFormInfo.entry_igreja.get()
        igreja_batismo = TabFormInfo.entry_igreja_batismo.get()
        data_batismo = TabFormInfo.entry_data_batismo.get()
        membro_EBD = TabFormInfo.entry_EBD.get()
        atividades = TabFormInfo.combobox_atividades.get()
        outras_atividades = TabFormInfo.textbox_church.get('0.0', 'end')
        atividades_igreja = TabFormInfo.entry_atividades_igreja.get()

        # Church verification
        if nome_igreja == '':
            nome_igreja = 'Não é membro'

        # Batism verification
        if TabFormInfo.check_box_batizado.get() == 'disabled':
            igreja_batismo = 'Não foi batizado'
            data_batismo = '00/00/00'

        # EBD verification
        if membro_EBD == '':
            info_EBD = 'Não participa'
        else:
            info_EBD = f'Participa na {membro_EBD}'

        # Activities verification
        if atividades == '':
            info_atividades = 'Não participa'
        elif atividades == 'Ministério Infantil' or 'Música':
            info_atividades = f'Participa de {atividades} na {atividades_igreja}'
        else:
            info_atividades = f'Participa de {outras_atividades} na {atividades_igreja}'        

        # List church information
        list_church_info = [nome_ER, nome_igreja, igreja_batismo, data_batismo, info_EBD, info_atividades]             

        # ------- Organization - Tab --> Get information ---------
        data_ingresso = TabFormInfo.entry_data_ingresso.get()
        data_aclamacao = TabFormInfo.entry_data_aclamacao.get()
        data_formatura = TabFormInfo.entry_data_formatura.get()
        posto = TabFormInfo.combobox.get()
        observacao = TabFormInfo.textbox_org.get('0.0', 'end')

        # Info verification
        if data_ingresso == '':
            messagebox.showerror('Erro', 'Informe a data da 1ª reunião que o ER participou.')
            return        
        if data_aclamacao == '':
            data_aclamacao = '00/00/00'

        if posto == 'Embaixador Escudeiro':
            data_formatura = '00/00/00'        
        
        if observacao == '\n':
            observacao = 'Não há'

        # List org information
        list_org_info = [nome_ER, data_ingresso, data_aclamacao, posto, data_formatura, observacao]
        
        # ---------- Save the informations in BD tables ----------- 
        inserir_form(list_basic_info)
        inserir_church(list_church_info)
        inserir_org(list_org_info)

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
              
        # Configure window       
        self.title("Cadastro dos ER")                  
        self.resizable(False, False)

        # Add frames
        self.tab_view = TabFormInfo(master=self)
        self.tab_view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.sidebar_frame = Sidebar(master=self)
        self.sidebar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

def cancel():
    app.destroy()

app = App()
app.mainloop()
