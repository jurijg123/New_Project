# src/app.py
import streamlit as st
import os
from logic import Funkcije

# Inicializacija
f = Funkcije()
usr = f.get_path_set(pillar2="None")[2]

st.set_page_config(page_title="Ustvari projektno mapo", layout="centered")

st.title("📁 Ustvari projektno mapo")

# Vnos imena projekta
proj_name = st.text_input("Ime projekta:")

# Izbira stebra (pillar)
pillar_options = [" ", "Automation", "Product Development"]
pillar_choice = st.selectbox("Izberi steber:", pillar_options)

# Stranke
options_2i = []
pillar2 = ["01A", "02P"]
for i in f.get_path_set(pillar2=pillar2)[0]:
    if os.path.exists(i):
        for j in os.listdir(i):
            options_2i.append(j)

if len(options_2i) != 0:
    for x in ["Konceptualizacija", "Past Projects", "Solidworks"]:
        if x in options_2i:
            options_2i.remove(x)
    options_2i.sort()

options_2 = list(dict.fromkeys(options_2i))
options_2.insert(0, " ")

clicked2 = st.selectbox("Izberi stranko:", options_2)

# Možnost dodaj nove stranke
new_stranka = st.text_input("Dodaj novo stranko (opcijsko):")

# Gumbi
if st.button("Ustvari projekt"):
    if pillar_choice == "Automation":
        pill_t = "01A"
    elif pillar_choice == "Product Development":
        pill_t = "02P"
    else:
        pill_t = None

    if pill_t and proj_name:
        code_proj = f.koda_gen(
            proj_name,
            pillar=pill_t,
            usrname=usr,
            stranka1=clicked2,
            stranka2=new_stranka,
        )[0]

        st.success(f"✅ Ustvarjena je mapa: '{code_proj} - {proj_name}'")
        st.session_state["last_code"] = code_proj
    else:
        st.error("Prosim izberi steber in vnesi ime projekta.")

if "last_code" in st.session_state:
    if st.button("📋 Kopiraj kodo projekta"):
        st.write("Koda projekta:", st.session_state["last_code"])
        st.toast("Koda je kopirana (ročno jo lahko kopiraš iz zgornje vrstice)")
