import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # CSS Ultra-optimizado para una sola carilla
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 1rem !important; 
            padding-bottom: 0rem !important;
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 700 !important;
            font-size: 0.75rem !important; /* Más pequeño */
            margin-bottom: 0px !important;
        }
        input {
            color: black !important;
            background-color: #f8f9fa !important;
            border: 1px solid #ced4da !important;
            height: 25px !important; /* Más bajo */
        }
        
        /* AJUSTES ESPECÍFICOS PARA IMPRESIÓN */
        @media print {
            @page { 
                size: A4; 
                margin: 0.2cm; /* Margen casi nulo */
            }
            html, body { 
                zoom: 78%; /* Reducción agresiva para asegurar 1 hoja */
                height: 100%;
                overflow: hidden;
            }
            /* OCULTAR LOGO Y ELEMENTOS DE STREAMLIT */
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], 
            .stButton, [data-testid="stImage"], header, footer { 
                display: none !important; 
            }
            .main .block-container { 
                padding: 0 !important; 
                margin: 0 !important; 
            }
            /* Convertir inputs en líneas simples */
            input { 
                border: none !important; 
                border-bottom: 1px solid #000 !important; 
                background: transparent !important; 
            }
            div[data-testid="stVerticalBlock"] {
                gap: 0rem !important; /* Elimina espacio entre filas */
            }
            hr { margin: 2px 0 !important; }
            h1 { font-size: 1.2rem !important; margin: 0 !important; }
            h3 { font-size: 0.9rem !important; margin: 2px 0 !important; }
            .stRadio > div { padding: 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera - El logo está aquí pero el CSS de arriba lo oculta al imprimir
    c_logo, c_tit = st.columns([1, 5])
    with c_logo:
        st.image(logo_url, width=65)
    with c_tit:
        st.markdown("<h1 style='color: black; margin: 0; padding: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black; margin: 0;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("<hr style='margin: 2px 0;'>", unsafe_allow_html=True)

    # Datos de Control
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha de Solicitud", datetime.now())
    c2.text_input("N° de Cliente", key="ctrl_nclie_f")
    c3.text_input("N° de Contrato", key="ctrl_contr_f")
    c4.text_input("% Localidad", key="ctrl_loc_f")

    inst1, inst2 = st.columns([2, 1])
    inst1.text_input("Establecimiento Educativo", key="ctrl_inst_f")
    inst2.text_input("Año / División", key="ctrl_anio_f")

    st.markdown("<hr style='margin: 2px 0;'>", unsafe_allow_html=True)
    
    # Datos del Pasajero
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    ap1.text_input("Apellido/s", key="pas_ape_f")
    nom1.text_input("Nombre/s", key="pas_nom_f")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL", key="pas_dni_f")
    cd2.text_input("Vencimiento DNI", key
