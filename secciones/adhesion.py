import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # --- BASE DE DATOS ---
    DB_FILE = "datos_adhesiones.csv"
    if not os.path.exists(DB_FILE):
        df_init = pd.DataFrame(columns=["Fecha", "Colegio", "Anio", "Pasajero", "DNI", "Plan"])
        df_init.to_csv(DB_FILE, index=False)

    # CSS "QUIRÚRGICO" PARA IMPRESIÓN
    st.markdown("""
        <style>
        /* Estilos para la vista web */
        .main { background-color: white !important; }
        
        @media print {
            /* 1. OCULTAR ABSOLUTAMENTE TODA LA ESTRUCTURA DE STREAMLIT */
            div[data-testid="stHeader"], 
            div[data-testid="stSidebar"], 
            div[data-testid="stToolbar"],
            div[data-testid="stDecoration"],
            div[data-testid="stStatusWidget"],
            #MainMenu, header, footer, nav, .stButton, iframe {
                display: none !important;
                visibility: hidden !important;
            }

            /* 2. FORZAR QUE EL CONTENIDO OCUPE TODA LA PÁGINA SIN MÁRGENES RAROS */
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
            }

            /* 3. ELIMINAR CUALQUIER IMAGEN QUE NO HAYAMOS PUESTO NOSOTROS CON HTML */
            img { display: none !important; }

            /* 4. AJUSTE DE PÁGINA A4 Y ZOOM */
            @page { 
                size: A4; 
                margin: 0.8cm; 
            }
            html, body { 
                zoom: 82%; 
                background: white !important; 
                color: black !important;
            }
            
            /* 5. COMPRIMIR ESPACIOS PARA QUE ENTRE EN UNA HOJA */
            div[data-testid="stVerticalBlock"] > div {
                margin-bottom: -14px !important; 
            }
            
            /* Dibujar los inputs como líneas negras */
            input { 
                border: none !important; 
                border-bottom: 1px solid black !important; 
                background: transparent !important;
                border-radius: 0 !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABECERA MANUAL EN HTML (No usamos st.image ni st.title) ---
    st.markdown(f"""
        <div style="text-align: center; color: black; border-bottom: 2px solid black; padding-bottom: 5px;">
            <h1 style="margin: 0; font-size: 26px;">SOLICITUD DE INGRESO</h1>
            <p style="margin: 0; font-weight: bold; font-size: 16px;">Serrano Turismo - Ficha de Adhesión</p>
        </div>
    """, unsafe_allow_html=True)

    # --- CAMPOS DEL FORMULARIO ---
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    fecha_val = c1.date_input("Fecha", datetime.now())
    n_clie = c2.text_input("N° de Cliente")
    n_cont = c3.text_input("N° de Contrato")
    p_loc = c4.text_input("% Localidad")

    inst1, inst2 = st.columns([2, 1])
    colegio = inst1.text_input("Establecimiento Educativo")
    anio_div = inst2.text_input("Año / División")

    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    p_ape = ap1.text_input("Apellido/s")
    p_nom = nom1.text_input("Nombre/s")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    p_dni = cd1.text_input("DNI / CUIL")
    p_vence = cd2.text_input("Vencimiento DNI") 
    p_nace = cd3.date_input("Nacimiento", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    dom1, dom2 = st.columns([2, 1])
    p_dom = dom1.text_input("Domicilio Particular")
    p_cp = dom2.text_input("Localidad / CP")

    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    t1, t2, t3 = st.columns([2, 1, 1])
    t_nom = t1.text_input("Nombre y Apellido Tutor")
    t_cuil = t2.text_input("CUIL Tutor")
    t_tel = t3.text_input("Teléfono")
    st.text_input("Correo Electrónico (E-mail):")

    plan_sel = st.pills("Plan de Pago:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], default="PLAN 4")

    # --- TEXTO LEGAL COMPLETO ---
    st.markdown(f"""
        <div style="font-size: 0.68rem; text-align: justify; border: 1px solid black; padding: 6px; color: black; line-height: 1.1; margin-top: 10px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente denominado.<br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br>
        <b>NOTA: De no marcar ningun plan de pago, su chequera se emitira como PLAN CUOTAS (PLAN 4).</b>
        </div>
    """, unsafe_allow_html=True)

    # --- FIRMAS ---
    st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Aclaración y N° de C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BOTONES ---
    st.markdown("---")
    c_save, c_print = st.columns(2)
    
    if c_save.button("💾 GUARDAR REGISTRO"):
        nuevo = pd.DataFrame([{"Fecha": fecha_val, "Colegio": colegio, "Anio": anio_div, "Pasajero": f"{p_ape} {p_nom}", "DNI": p_dni, "Plan": plan_sel}])
        nuevo.to_csv(DB_FILE, mode='a', header=False, index=False)
        st.success("Guardado.")

    with c_print:
        # BOTÓN DE IMPRESIÓN MEJORADO
        components.html("""
            <button onclick="window.parent.print()" style="background-color: #2E7D32; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;">
            🖨️ IMPRIMIR AHORA
            </button>
        """, height=70)

    # SIDEBAR
    with st.sidebar:
        st.header("Excel")
        if os.path.exists(DB_FILE):
            df_hist = pd.read_csv(DB_FILE)
            st.download_button("📥 Descargar Historial", df_hist.to_csv(index=False).encode('utf-8'), "adhesiones.csv")

    render_footer()
