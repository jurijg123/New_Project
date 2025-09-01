import numpy as numpy
import string
import random

import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook

class Funkcije:
    
    def get_path_set(self, pillar2):
        
        path_sett = r'C:\SaveAsSettings.txt'
        settings = open(path_sett, "r")
        set_str = [i for i in settings][-1][6:].replace("\\", "/")
        if pillar2 != "None":
            path_for_p = [set_str + '/Biro Bonus/Inzeniring - Dokumenti/' + i for i in pillar2]
        else:
            path_for_p = []
        path_ico = set_str + '/Biro Bonus/Inzeniring - Dokumenti/Other/Icons/icon_BE.ico'
        settings = open(path_sett, "r")
        username = [i for i in settings][0][6:-1]
        
        return path_for_p, path_ico, username
    
    def koda_gen(self, projekt, pillar, stranka1, stranka2, usrname, numb=1, size=4, chars=string.digits, path1=r'\Biro Bonus\Inzeniring - Dokumenti\Other'):
        
        """
        koda_gen(self, projekt, numb=1, size=4, chars=string.digits, path=r'\Biro Bonus\Inzeniring - Dokumenti\Other\projekti.txt')
        
        Ustvari kodo projekta za Bonus Engineering. Ustvari kodo projekta, preveri, če je projekt že vpisan, ga vpiše v.txt datoteko
        ter ustvari projektno mapo z ustrezno podstrukturo.
        
        Parametri:
        ----------
        projekt : string
               Vnešeno ime projekta.
        numb : integer
               Število generiranih kod.
        size : integer
               Dolžina kode.
        path : string
               Pot do projektov.     
        
        """
        
        if stranka2 == "None" or stranka2 == "" or stranka2 == " ":
            stranka = stranka1
        else:
            stranka = stranka2

        path_sett = r'C:\SaveAsSettings.txt'
        settings = open(path_sett, "r")
        set_str = [i for i in settings][-1][6:]
        
        path = set_str + path1 + '\projekti.txt'
        
        path_folder = set_str + '/Biro Bonus/Inzeniring - Dokumenti/'+ pillar + '/' + stranka
        path_folder_min = set_str + '/Biro Bonus/Inzeniring - Dokumenti/'+ pillar     
        
        #preverim, če obstaja mapa, če ne jo ustvarim:
        if os.path.exists(path_folder):
            pass
        else:
            if os.path.exists(path_folder_min):
                path_f_new = os.path.join(path_folder_min, stranka)
                try:
                    os.mkdir(path_f_new)
                except OSError as error:
                    print(error)
            else:
                print(f'Ni ustreznega stebra!\t{path_folder_min}')
        
        
        code1 = []
        today = date.today()
        leto = str(today)[:4]#+str(today)[8:] #uporabimo le leto
        f1 = open(path, "r")
        koda = pillar[-1]+leto
        obj = []
        for k in f1:
            if k[1:5] == leto:
                obj.append(k)
        #obj = [k for k in f1]
        f1.close()
        f = open(path, "a")

        if len(obj) == 0:
            f.write(koda + '-01' +"\t"+projekt+"\t"+stranka+"\t"+str(today)+"\n")
            code1.append(koda + '-01')
        else:
            if len(obj) < 10:
                stevilka = '-0' + str(len(obj)+1)
            else:
                stevilka = '-' + str(len(obj)+1)
            for j in obj:
                while koda + stevilka != j[:8]:
                    f.write(koda + stevilka + "\t"+projekt+"\t"+stranka+"\t"+str(today)+"\n")
                    code1.append(koda + stevilka)
                    break
                break
        f.close()
        
        exc_path = set_str + path1 + '\Projekti.xlsx'
        
        append_data = pd.DataFrame([{"KODA":code1[0], "IME":projekt, "DATUM":str(date.today()), "STRANKA":stranka, "USTVARIL":usrname}])
    
        wb = load_workbook(filename = exc_path)
        ws = wb[leto]
        for r in dataframe_to_rows(append_data, index=False, header=False):  #No index and don't append the column headers
            ws.append(r)
        wb.save(exc_path)
        
        if stranka1 == "ANVIS" or stranka2 == "ANVIS":
            folders = ['01_MODEL', '02_RISBE', '03_IN', '04_SHARE']
            f_001 = ['01_Dodatno']
            f_002 = ['00_DOC', '01_Kosovnice', '02_PDF']
            f_003 = ['01_MERITVE', '02_VHODNI_MODELI']
            f_004 = ['IN', 'OUT']
            f_ = [f_001, f_002, f_003, f_004]
        else:
            folders = ['01_CAD', '02_DOC', '03_IN', '04_SHARE']
            f_001 = ['00_Skupni sestav', '99_Stand']
            f_002 = ['00_CE', '01_Kosovnice']
            f_003 = ['01_IN-CAD', '02_IN-DOC', '03_KONCEPT']
            f_004 = ['IN', 'OUT']
            f_ = [f_001, f_002, f_003, f_004]

        folder_name = code1[0] + "_" + projekt
        path_n = os.path.join(path_folder, folder_name).replace("\\", "/")
        try:
            os.mkdir(path_n)
        except OSError as error:
            print(error)

        for fold in folders:
            path_f = os.path.join(path_n+'/', fold)
            try:
                os.mkdir(path_f)
            except OSError as error:
                print(error)

        for i in range(len(f_)):
            for subf in f_[i]:
                path_sf = os.path.join(path_n+'/'+folders[i], subf).replace("\\", "/")
                try:
                    os.mkdir(path_sf)
                except OSError as error:
                    print(error)        
        
        return code1

    def ustvari(self):
        pil_tmp = clicked.get()
        if pil_tmp == "Automation":
            pill_t = "01A"
        elif pil_tmp == "Product Development":
            pill_t = "02P"
        else:
            print("Ni ustreznega stebra, preveri IF Stavek")
            
        self.code_proj = Funkcije().koda_gen(proj_name.get(), pillar=pill_t, usrname=usr, stranka1=clicked2.get(), stranka2=label_new_p.cget("text"))[0]
        koda_label["text"] = "Koda projekta: "+self.code_proj
        showinfo(title='Ustvarjen projekt', message=f'Ustvarjena je mapa: \'{self.code_proj} - {proj_name.get()}\' v projektni mapi.')

    def copy(self):
        pc.copy(self.code_proj)
        showinfo(title='Kopirano!', message=f'Projektna koda {self.code_proj} je kopirana v odložišče.')
