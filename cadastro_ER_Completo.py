import tkinter as tk 
import customtkinter as ctk
from tkcalendar import Calendar

import requests

from PIL import Image

import os

PATH = os.path.dirname(os.path.realpath(__file__))

class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # ========== create tab 1 - ER ===========
        self.add("Embaixador do Rei")        

        # ======== add widgets on tabs ===========
        self.label = ctk.CTkLabel(master=self.tab("Embaixador do Rei"))
      
        # ====== create 2x2 grid system ==========
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ============ frame_top_info ============
        self.frame_top_info = ctk.CTkFrame(master=self.tab("Embaixador do Rei"))
        self.frame_top_info.grid(row=0, column=0, sticky="nwse", padx=(20, 20), pady=(20, 10))

        # ==== configure grid layout (8x2) ======
        self.frame_top_info.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.frame_top_info.columnconfigure((0, 1), weight=1)

        # ======= Basic information form ========
        self.label_informacoes = ctk.CTkLabel(master=self.frame_top_info, text="Informações Básicas")
        self.label_informacoes.grid(row=0, column=0, columnspan=2, pady=10, padx=0, sticky="nwse")

        self.label_nome = ctk.CTkLabel(master=self.frame_top_info, text="Nome Completo:")
        self.label_nome.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        self.entry_nome = ctk.CTkEntry(master=self.frame_top_info, width=320)
        self.entry_nome.grid(row=1, column=1, columnspan=2, pady=5, padx=15, sticky="ew")

        self.label_resp = ctk.CTkLabel(master=self.frame_top_info, text="Nome do Responsável:")
        self.label_resp.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        self.entry_resp = ctk.CTkEntry(master=self.frame_top_info, width=320)
        self.entry_resp.grid(row=2, column=1,  columnspan=2, pady=5, padx=15, sticky="ew")

        self.label_cep = ctk.CTkLabel(master=self.frame_top_info, text="CEP:")
        self.label_cep.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        self.entry_cep = ctk.CTkEntry(master=self.frame_top_info, width=145)
        self.entry_cep.grid(row=3, column=1, pady=5, padx=15, sticky="w")
        
        self.button_end = ctk.CTkButton(master=self.frame_top_info, width=125, text="Buscar endereço", command=lambda: self.find_localization())
        self.button_end.grid(row=3, column=1, pady=5, padx=15, sticky="e")
       
        self.label_endereco = ctk.CTkLabel(master=self.frame_top_info, text="Endereço:")
        self.label_endereco.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        self.entry_logradouro = ctk.CTkEntry(master=self.frame_top_info, placeholder_text="Logradouro", width=265)
        self.entry_logradouro.grid(row=4, column=1, pady=5, padx=15, sticky="w")

        self.entry_numero = ctk.CTkEntry(master=self.frame_top_info, placeholder_text="Nº", width=30)
        self.entry_numero.grid(row=4, column=1, pady=5, padx=15, sticky="e")

        self.label_bairro = ctk.CTkLabel(master=self.frame_top_info, text="Bairro:")
        self.label_bairro.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        self.entry_bairro = ctk.CTkEntry(master=self.frame_top_info, width=320)
        self.entry_bairro.grid(row=5, column=1, pady=5, padx=15, sticky="ew")

        self.label_cidade = ctk.CTkLabel(master=self.frame_top_info, text="Cidade:")
        self.label_cidade.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        self.entry_cidade = ctk.CTkEntry(master=self.frame_top_info, width=265)
        self.entry_cidade.grid(row=6, column=1, pady=5, padx=15, sticky="w")

        self.entry_UF = ctk.CTkEntry(master=self.frame_top_info, placeholder_text="UF", width=30)
        self.entry_UF.grid(row=6, column=1, pady=5, padx=15, sticky="e")

        self.label_complemento = ctk.CTkLabel(master=self.frame_top_info, text="Complemento:")
        self.label_complemento.grid(row=7, column=0, pady=(5, 15), padx=10, sticky="w")

        self.entry_complemento = ctk.CTkEntry(master=self.frame_top_info, width=205)
        self.entry_complemento.grid(row=7, column=1, pady=(5, 15), padx=15, sticky="w")

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

        self.label_nasc = ctk.CTkLabel(master=self.frame_bottom_date, text="Data de Nascimento:")
        self.label_nasc.grid(row=1, column=0, pady=(5, 15), padx=10, sticky="w")

        self.entry_nasc = ctk.CTkEntry(master=self.frame_bottom_date, width=150, state="disabled")
        self.entry_nasc.grid(row=1, column=1, pady=(5, 15), padx=10, sticky="w")

        self.button_date = ctk.CTkButton(master=self.frame_bottom_date, width=120, text="Selecionar Data", command=lambda: self.create_toplevel_date("nascimento"))
        self.button_date.grid(row=1, column=2, pady=(5, 15), padx=15, sticky="e")

         # ============ frame_bottom_tel ============
        self.frame_bottom_tel = ctk.CTkFrame(master=self.tab("Embaixador do Rei"))
        self.frame_bottom_tel.grid(row=2, column=0, sticky="nwse", padx=20, pady=(10, 20))

        # ======= configure grid layout (2x3) =======
        self.frame_bottom_tel.rowconfigure((0, 1, 2), weight=1)
        self.frame_bottom_tel.columnconfigure((0, 1, 2), weight=1)

        # ============= Date label ==================
        self.label_tel = ctk.CTkLabel(master=self.frame_bottom_tel, text="Telefones Para Contato")
        self.label_tel.grid(row=0, column=0, columnspan=3, pady=(15, 5), padx=0, sticky="nswe")

        self.label_tel_resp = ctk.CTkLabel(master=self.frame_bottom_tel, text="Tel. do Responsável:")
        self.label_tel_resp.grid(row=1, column=0, pady=(5, 15), padx=10, sticky="w")

        self.entry_tel_resp = ctk.CTkEntry(master=self.frame_bottom_tel, width=150)
        self.entry_tel_resp.grid(row=1, column=1, pady=(5, 15), padx=10, sticky="w")       

        self.combobox_tel = ctk.CTkOptionMenu(master=self.frame_bottom_tel, values=["Celular", "Fixo"])
        self.combobox_tel.grid(row=1, column=2, pady=(5, 15), padx=15, sticky="e")

        self.label_tel_ER = ctk.CTkLabel(master=self.frame_bottom_tel, text="Tel. do Embaixador do Rei:")
        self.label_tel_ER.grid(row=2, column=0, pady=(5, 15), padx=10, sticky="w")

        self.entry_tel_ER = ctk.CTkEntry(master=self.frame_bottom_tel, width=150)
        self.entry_tel_ER.grid(row=2, column=1, pady=(5, 15), padx=10, sticky="w")       

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
        
        def check_event(campo):
   
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
              
        check_igreja = tk.StringVar()
        self.check_box_igreja = ctk.CTkCheckBox(master=self.frame_church_info, text="", variable=check_igreja, command=lambda: check_event("igreja"), onvalue="normal", offvalue="disabled")
        self.check_box_igreja.grid(row=1, column=1, pady=5, padx=15, sticky="w")
        self.check_box_igreja.deselect()
                       
        self.entry_igreja = ctk.CTkEntry(master=self.frame_church_info, width=240, state="disabled")
        self.entry_igreja.grid(row=1, column=1, pady=5, padx=15, sticky="e")

        self.label_batizado = ctk.CTkLabel(master=self.frame_church_info, text="Foi batizado? Se sim, em qual igreja?")
        self.label_batizado.grid(row=2, column=0, pady=5, padx=15, sticky="w")
    
        check_batismo = tk.StringVar()
        self.check_box_batizado = ctk.CTkCheckBox(master=self.frame_church_info, text="", variable=check_batismo, command=lambda: check_event("batismo"), onvalue="normal", offvalue="disabled")
        self.check_box_batizado.grid(row=2, column=1, pady=5, padx=15, sticky="w")
        self.check_box_batizado.deselect()

        self.entry_igreja_batismo = ctk.CTkEntry(master=self.frame_church_info, width=240, state="disabled")
        self.entry_igreja_batismo.grid(row=2, column=1, pady=5, padx=15, sticky="e")

        self.label_data_batismo = ctk.CTkLabel(master=self.frame_church_info, text="E qual a data do batismo?")
        self.label_data_batismo.grid(row=3, column=0, pady=5, padx=15, sticky="w")

        self.entry_data_batismo = ctk.CTkEntry(master=self.frame_church_info, width=130, state="disabled")
        self.entry_data_batismo.grid(row=3, column=1, pady=5, padx=15, sticky="w")

        self.button_data_batismo = ctk.CTkButton(master=self.frame_church_info, width=125, text="Selecionar Data", command=lambda: self.create_toplevel_date("batismo"), state="disabled")
        self.button_data_batismo.grid(row=3, column=1, pady=5, padx=15, sticky="e") 

        self.label_EBD = ctk.CTkLabel(master=self.frame_church_info, text="Frequenta EBD? Se sim, em qual igreja?")
        self.label_EBD.grid(row=4, column=0, pady=5, padx=15, sticky="w")

        self.entry_EBD = ctk.CTkEntry(master=self.frame_church_info, width=280, state="normal")
        self.entry_EBD.grid(row=4, column=1, pady=5, padx=15, sticky="e")

        self.label_atividades = ctk.CTkLabel(master=self.frame_church_info,text="Participa de outras atividades/organizações?")
        self.label_atividades.grid(row=5, column=0, columnspan=2, pady=5, padx=15, sticky="w")

        check_atividades = tk.StringVar()
        self.check_box_atividades = ctk.CTkCheckBox(master=self.frame_church_info, text="", variable=check_atividades, command=lambda: check_event("atividades"), onvalue="normal", offvalue="disabled")
        self.check_box_atividades.grid(row=6, column=0, pady=5, padx=15, sticky="w")
        self.check_box_atividades.deselect()
        
        self.combobox_atividades = ctk.CTkComboBox(master=self.frame_church_info, state="disabled", width=200, values=["Ministério Infantil", "Música", "Outros"])
        self.combobox_atividades.grid(row=6, column=0, pady=5, padx=20, sticky="e")

        self.label_atividades_igreja = ctk.CTkLabel(master=self.frame_church_info, text="Em qual igreja?")
        self.label_atividades_igreja.grid(row=6, column=1, pady=5, padx=0, sticky="w")

        self.entry_atividades_igreja = ctk.CTkEntry(master=self.frame_church_info, width=200, state="disabled")
        self.entry_atividades_igreja.grid(row=6, column=1, pady=5, padx=15, sticky="e")

        self.label_outros = ctk.CTkLabel(master=self.frame_church_info, text="Caso tenha selecionado outros, especifique:")
        self.label_outros.grid(row=7, column=0, pady=5, padx=15, sticky="w")

        self.textbox = ctk.CTkTextbox(master=self.frame_church_info, state="normal")
        self.textbox.grid(row=8, column=0, columnspan=2, padx=20, pady=(15, 20), sticky="nsew")

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

        self.label_data_ingresso = ctk.CTkLabel(master=self.frame_organization_info, text="Frequenta as reuniões desde:")
        self.label_data_ingresso.grid(row=1, column=0, pady=5, padx=15, sticky="w")

        self.entry_data_ingresso = ctk.CTkEntry(master=self.frame_organization_info, width=150, state="disabled")
        self.entry_data_ingresso.grid(row=1, column=1, pady=5, padx=15, sticky="w")

        self.button_data_ingresso = ctk.CTkButton(master=self.frame_organization_info, width=135, text="Selecionar Data", command=lambda: self.create_toplevel_date("ingresso"))
        self.button_data_ingresso.grid(row=1, column=2, pady=5, padx=15, sticky="e") 

        self.label_data_aclamação = ctk.CTkLabel(master=self.frame_organization_info, text="É membro da embaixada desde:")
        self.label_data_aclamação.grid(row=2, column=0, pady=5, padx=15, sticky="w")

        self.entry_data_aclamacao = ctk.CTkEntry(master=self.frame_organization_info, width=150, state="disabled")
        self.entry_data_aclamacao.grid(row=2, column=1, pady=5, padx=15, sticky="w")

        self.button_data_aclamacao = ctk.CTkButton(master=self.frame_organization_info, width=135, text="Selecionar Data", command=lambda: self.create_toplevel_date("aclamacao"))
        self.button_data_aclamacao.grid(row=2, column=2, pady=5, padx=15, sticky="e") 

        self.label_posto = ctk.CTkLabel(master=self.frame_organization_info, text="Posto do embaixador do Rei na organização:")
        self.label_posto.grid(row=3, column=0, columnspan=3, pady=5, padx=(15, 15), sticky="ew")

        self.combobox = ctk.CTkComboBox(master=self.frame_organization_info,  width=165, values=["Embaixador Escudeiro", "Embaixador Arauto", "Embaixador Sênior", "Embaixador Emérito"])
        self.combobox.grid(row=4, column=0, padx=20, pady=5, sticky="e")

        self.entry_data_formatura = ctk.CTkEntry(master=self.frame_organization_info, width=150, state="disabled")
        self.entry_data_formatura.grid(row=4, column=1, pady=5, padx=15, sticky="w")

        self.button_data_formatura = ctk.CTkButton(master=self.frame_organization_info, width=135, text="Selecionar Data", command=lambda: self.create_toplevel_date("formatura"))
        self.button_data_formatura.grid(row=4, column=2, pady=5, padx=15, sticky="e") 

        self.label_infoER = ctk.CTkLabel(master=self.frame_organization_info, text="Observações")
        self.label_infoER.grid(row=5, column=0, columnspan=3, pady=(5, 15), padx=(15, 15), sticky="nwse")

        self.textbox = ctk.CTkTextbox(master=self.frame_organization_info)
        self.textbox.grid(row=6, column=0, columnspan=3, padx=20, pady=(5, 20), sticky="nsew")

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

        self.insignia_image = ctk.CTkImage(Image.open(PATH + "/images/Logo_ER_QIBN.png"), size=(170, 170))

        font_title = ctk.CTkFont(family="Segoe UI", size=18, weight="normal")
        font_name = ctk.CTkFont(family="Segoe UI", size=13, weight="bold")

        # add widgets on to the sidebar...
        self.label = ctk.CTkLabel(self, text="Cadastrar ER", height=30, corner_radius=6, fg_color=("gray70", "gray25"), font=font_title)
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.button_register = ctk.CTkButton(master=self, image=self.add_user_image, text="Cadastrar", width=100, height=80, border_width=2,
                                                        corner_radius=10, compound="bottom", border_color="gray50", fg_color=("gray70", "gray25"),
                                                        hover_color="gray25", command=self.button_function)
        self.button_register.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.button_clean = ctk.CTkButton(master=self, image=self.cancel_image, text="Cancelar", width=100, height=80, border_width=2,
                                                        corner_radius=10, compound="bottom", border_color="gray50", fg_color=("gray70", "gray25"),
                                                        hover_color="gray25", command=self.button_function)
        self.button_clean.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.insignia_label = ctk.CTkLabel(self, image=self.insignia_image, text="")
        self.insignia_label.grid(row=7, column=0, padx=0, pady=0, sticky="sew")

        self.insignia_label = ctk.CTkLabel(self, text="Embaixada\nPr. Edson P. Messor", font=font_name)
        self.insignia_label.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="nsew")
    
    def button_function(self):
        print("button pressed")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
              
        self.title("Cadastro dos ER")

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.sidebar_frame = Sidebar(master=self)
        self.sidebar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()