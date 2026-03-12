import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # --- BASE DE DATOS CSV ---
    DB_FILE = "datos_adhesiones.csv"
    if not os.path.exists(DB_FILE):
        df_init = pd.DataFrame(columns=["Fecha", "Colegio", "Anio", "Pasajero", "DNI", "Plan"])
        df_init.to_csv(DB_FILE, index=False)

    # CSS RADICAL PARA OCULTAR MENÚS/LOGOS Y AJUSTAR ESPACIADO
    st.markdown("""
        <style>
        /* Estilos para vista web (pantalla) */
        .main { background-color: white !important; }
        label p { font-weight: 700 !important; font-size: 0.8rem !important; color: black !important; }
        input { height: 28px !important; }

        @media print {
            /* 1. OCULTAR ABSOLUTAMENTE TODO EXCEPTO EL CONTENIDO DE LA FICHA */
            header, footer, [data-testid="stHeader"], [data-testid="stSidebar"], 
            [data-testid="stImage"], .stButton, iframe, [data-testid="stSidebarNav"],
            nav, .no-print, #MainMenu { 
                display: none !important; 
                visibility: hidden !important;
                height: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            /* 2. AJUSTES DE PÁGINA A4 Y ZOOM */
            @page { size: A4; margin: 0.4cm; }
            html, body { 
                zoom: 80% !important; /* Zoom para asegurar que entre */
                background-color: white !important;
                color: black !important;
                height: 100% !important; /* Fuerza una sola página */
            }
            
            /* 3. COMPRESIÓN DE ESPACIOS SUPERIORES */
            .main .block-container { 
                padding: 0 !important; 
                margin: 0 !important; 
                max-width: 100% !important;
            }
            div[data-testid="stVerticalBlock"] > div {
                margin-bottom: -15px !important; /* Achica espacios entre widgets */
            }
            
            /* 4. ESTILO DE FORMULARIO IMPRESO */
            input { 
                border: none !important; 
                border-bottom: 1px solid black !important; 
                background: transparent !important;
                color: black !important;
            }
            hr { margin: 4px 0 !important; border: 0.5px solid black !important; }
            h3 { font-size: 1rem !important; margin: 4px 0 !important; }

            /* 5. FUERZA ESPACIADO INFERIOR (FIRMAS Y FOOTER) MÁS ABAJO */
            #seccion-firmas {
                margin-top: 30mm !important; /* Empuja las firmas 3cm más abajo */
            }
            div[data-testid="stMarkdownContainer"] footer {
                display: block !important; /* Permitimos footer en impresión */
                position: absolute;
                bottom: 0;
                width: 100%;
                font-size: 0.7rem !important;
                margin-top: 0 !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # CABECERA MANUAL EN HTML (Evita widgets de imagen de Streamlit que se agrandan)
    st.markdown(f"""
        <div style="text-align: center; color: black;">
            <h1 style="margin: 0; font-size: 22px;">SOLICITUD DE INGRESO</h1>
            <p style="margin: 0; font-weight: bold; font-size: 14px;">Serrano Turismo - Ficha de Adhesión</p>
        </div>
        <hr style="margin: 5px 0; border: 1px solid black;">
    """, unsafe_allow_html=True)

    # --- CUERPO DE LA FICHA ---
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    f_sol = c1.date_input("Fecha de Solicitud", datetime.now())
    n_clie = c2.text_input("N° de Cliente", key="ctrl_nclie_f")
    n_cont = c3.text_input("N° de Contrato", key="ctrl_contr_f")
    p_loc = c4.text_input("% Localidad", key="ctrl_loc_f")

    inst1, inst2 = st.columns([2, 1])
    colegio = inst1.text_input("Establecimiento Educativo", key="ctrl_inst_f")
    anio_div = inst2.text_input("Año / División", key="ctrl_anio_f")

    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    p_ape = ap1.text_input("Apellido/s", key="pas_ape_f")
    p_nom = nom1.text_input("Nombre/s", key="pas_nom_f")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    p_dni = cd1.text_input("DNI / CUIL", key="pas_dni_f")
    p_vence = cd2.text_input("Vencimiento DNI", key="pas_vence_f") 
    p_nace = cd3.date_input("Nacimiento", min_value=datetime(1990,1,1), key="pas_nace_f")
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True, key="pas_sexo_f")

    dom1, dom2 = st.columns([2, 1])
    p_dom = dom1.text_input("Domicilio Particular", key="pas_dom_f")
    p_cp = dom2.text_input("Localidad / CP", key="pas_cp_f")

    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    t1_1, t1_2, t1_3 = st.columns([2, 1, 1])
    t1_nom = t1_1.text_input("Nombre Tutor 1", key="t1_nom_f")
    t1_cuil = t1_2.text_input("CUIL Tutor 1", key="t1_cuil_f")
    t1_tel = t1_3.text_input("Teléfono", key="t1_tel_f")
    t_email = st.text_input("Correo Electrónico (E-mail):", key="tut_email_f")

    plan_sel = st.pills("Seleccione su Plan de Pago:", 
                       options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], 
                       default="PLAN 4", key="plan_sel_f")

    # Texto Legal completo
    st.markdown(f"""
        <div style="font-size: 0.65rem; text-align: justify; border: 1px solid #ccc; padding: 6px; background-color: #f9f9f9; color: black; line-height: 1.1; margin-top: 5px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente denominado.<br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br>
        <b>NOTA: De no marcar ningun plan de pago, su chequera se emitira como PLAN CUOTAS (PLAN 4).</b>
        </div>
    """, unsafe_allow_html=True)

    # FIRMAS (Empujadas hacia abajo en impresión)
    st.markdown('<div id="seccion-firmas" style="margin-top: 25px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<hr style='
