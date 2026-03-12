import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # --- CONFIGURACIÓN DE DATOS (EXCEL/CSV) ---
    DB_FILE = "datos_adhesiones.csv"
    if not os.path.exists(DB_FILE):
        df_init = pd.DataFrame(columns=["Fecha", "Colegio", "Anio", "Pasajero", "DNI", "Plan", "Tutor"])
        df_init.to_csv(DB_FILE, index=False)

    # CSS OPTIMIZADO PARA UNA SOLA CARILLA
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 0.5rem !important; 
            padding-bottom: 0rem !important;
            max-width: 95% !important;
        }
        [data-testid="stVerticalBlock"] > div { gap: 0.1rem !important; }
        
        @media print {
            @page { size: A4; margin: 0.3cm; }
            html, body { zoom: 80%; overflow: hidden !important; height: 99%; }
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], 
            .stButton, footer, iframe { display: none !important; }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            input { border: none !important; border-bottom: 1px solid #000 !important; }
            hr { margin: 3px 0 !important; }
            h1 { font-size: 1.3rem !important; }
            h3 { font-size: 1rem !important; margin-top: 2px !important; }
            div[data-testid="stMarkdownContainer"] p { font-size: 0.8rem !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- FORMULARIO ---
    c_logo, c_tit = st.columns([1, 5])
    with c_logo: st.image(logo_url, width=60)
    with c_tit:
        st.markdown("<h1 style='color: black; margin: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black; margin: 0;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Datos de Control
    st.markdown("### 📋 DATOS DE CONTROL")
    col_ctrl1 = st.columns(4)
    f_sol = col_ctrl1[0].date_input("Fecha", datetime.now())
    n_clie = col_ctrl1[1].text_input("N° de Cliente") # Opcional
    n_cont = col_ctrl1[2].text_input("N° de Contrato") # Opcional
    p_loc = col_ctrl1[3].text_input("% Localidad") # Opcional

    inst1, inst2 = st.columns([2, 1])
    colegio = inst1.text_input("Establecimiento Educativo *")
    anio_div = inst2.text_input("Año / División *")

    # Datos Pasajero
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    p_ape = ap1.text_input("Apellido/s *")
    p_nom = nom1.text_input("Nombre/s *")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    p_dni = cd1.text_input("DNI / CUIL *")
    p_vence = cd2.text_input("Vencimiento DNI *") 
    p_nace = cd3.date_input("Nacimiento *", min_value=datetime(1990,1,1))
    
    st.radio("Sexo *", ["Masculino", "Femenino", "X"], horizontal=True)
    dom1, dom2 = st.columns([2, 1])
    p_dom = dom1.text_input("Domicilio Particular *")
    p_cp = dom2.text_input("Localidad / CP *")

    # Datos Tutores
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    t1_1, t1_2, t1_3 = st.columns([2, 1, 1])
    t1_nom = t1_1.text_input("Nombre y Apellido Tutor 1 *")
    t1_cuil = t1_2.text_input("CUIL Tutor 1 *")
    t1_tel = t1_3.text_input("Teléfono *")
    t_mail = st.text_input("Correo Electrónico *")

    plan_sel = st.pills("Plan de Pago:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5"], default="PLAN 4")

    # Texto Legal (Reducido para espacio)
    st.markdown(f"""<div style="font-size: 0.65rem; text-align: justify; border: 1px solid #ccc; padding: 5px; background-color: #f9f9f9; color: black; line-height: 1;">
        Declaro bajo juramento que los datos son exactos y acepto el plan de pagos seleccionado. Los planes al contado vencen a los 30 días.
        Conozco las condiciones del contrato suscrito. NOTA: Sin selección se emitirá PLAN 4.</div>""", unsafe_allow_html=True)

    # Firmas
    f1, f2 = st.columns(2)
    f1.markdown("<br><hr style='border:0.5px solid black;'><p style='text-align:center; font-size:7pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<br><hr style='border:0.5px solid black;'><p style='text-align:center; font-size:7pt; color:black;'>Aclaración y N° de C.U.I.L.</p>", unsafe_allow_html=True)

    # --- VALIDACIÓN Y GUARDADO ---
    campos_validar = [colegio, anio_div, p_ape, p_nom, p_dni, p_vence, p_dom, p_cp, t1_nom, t1_cuil, t1_tel, t_mail]
    todo_completo = all(str(c).strip() != "" for c in campos_validar)

    st.markdown("---")
    if not todo_completo:
        st.warning("⚠️ Complete todos los campos marcados con (*) para habilitar la impresión y el guardado.")
    else:
        col_btns = st.columns([1, 1])
        if col_btns[0].button("💾 GUARDAR REGISTRO"):
            nuevo = pd.DataFrame([{
                "Fecha": f_sol, "Colegio": colegio, "Anio": anio_div, 
                "Pasajero": f"{p_ape}, {p_nom}", "DNI": p_dni, "Plan": plan_sel, "Tutor": t1_nom
            }])
            nuevo.to_csv(DB_FILE, mode='a', header=False, index=False)
            st.success("¡Datos guardados!")
            st.session_state['listo_para_imprimir'] = True

        if st.session_state.get('listo_para_imprimir', False):
            with col_btns[1]:
                components.html("""
                    <button style="background-color: #2E7D32; color: white; padding: 8px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold;" 
                    onclick="window.parent.print()">🖨️ IMPRIMIR AHORA</button>
                """, height=50)

    # --- SIDEBAR: EXPORTACIÓN POR COLEGIO ---
    with st.sidebar:
        st.header("📂 Exportar Datos")
        if os.path.exists(DB_FILE):
            df_total = pd.read_csv(DB_FILE)
            if not df_total.empty:
                colegios_lista = ["Ver todos"] + sorted(df_total["Colegio"].unique().tolist())
                sel = st.selectbox("Seleccionar Colegio", colegios_lista)
                
                df_final = df_total if sel == "Ver todos" else df_total[df_total["Colegio"] == sel]
                
                st.write(f"Registros encontrados: {len(df_final)}")
                csv = df_final.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Descargar Excel (CSV)", csv, f"adhesion_{sel}.csv", "text/csv")

    render_footer()
