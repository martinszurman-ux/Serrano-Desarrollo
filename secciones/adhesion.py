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

    # CSS RADICAL PARA OCULTAR TODO LO QUE NO SEA LA FICHA
    st.markdown("""
        <style>
        /* Estilos para la web */
        .main { background-color: white !important; }
        
        /* FUERZA BRUTA PARA IMPRESIÓN */
        @media print {
            /* Ocultar absolutamente todo lo que Streamlit genera por fuera del contenido */
            header, footer, nav, iframe, button, .stButton, 
            [data-testid="stHeader"], 
            [data-testid="stSidebar"], 
            [data-testid="stSidebarNav"],
            [data-testid="stImage"],
            [data-testid="stToolbar"],
            #MainMenu, .no-print {
                display: none !important;
                visibility: hidden !important;
                height: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
            }

            /* Reset de página A4 */
            @page { size: A4; margin: 0.5cm; }
            html, body { 
                zoom: 78%; /* Un poco más chico para asegurar 1 sola hoja */
                background: white !important; 
                color: black !important;
                width: 210mm;
                height: 297mm;
            }

            .main .block-container { 
                padding: 0 !important; 
                margin: 0 !important; 
                max-width: 100% !important;
            }

            /* Ajuste de inputs para que parezcan líneas */
            input { 
                border: none !important; 
                border-bottom: 1px solid black !important; 
                background: transparent !important;
            }
            
            /* Comprimir espacios entre elementos de Streamlit */
            div[data-testid="stVerticalBlock"] > div {
                margin-bottom: -15px !important; 
            }
            
            hr { margin: 5px 0 !important; border: 0.5px solid black !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABECERA MANUAL (Sin widgets de Streamlit para evitar que se agranden) ---
    st.markdown(f"""
        <div style="text-align: center; color: black;">
            <h1 style="margin: 0; font-size: 24px;">SOLICITUD DE INGRESO</h1>
            <p style="margin: 0; font-weight: bold; font-size: 14px;">Serrano Turismo - Ficha de Adhesión</p>
        </div>
        <hr style="margin: 10px 0; border: 1px solid black;">
    """, unsafe_allow_html=True)

    # --- CAMPOS DEL FORMULARIO ---
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    fecha_val = c1.date_input("Fecha", datetime.now())
    n_clie = c2.text_input("N° de Cliente")
    n_cont = c3.text_input("N° de Contrato")
    p_loc = c4.text_input("% Liberado")

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
        <div style="font-size: 0.68rem; text-align: justify; border: 1px solid #000; padding: 8px; color: black; line-height: 1.2; margin-top: 10px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente denominado.<br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br>
        <b>NOTA: De no marcar ningun plan de pago, su chequera se emitira como PLAN CUOTAS (PLAN 4).</b>
        </div>
    """, unsafe_allow_html=True)

    # --- FIRMAS ---
    st.markdown('<div style="margin-top: 25px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Aclaración y N° de C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- ACCIONES ---
    st.markdown("---")
    col_g, col_i = st.columns(2)
    
    if col_g.button("💾 GUARDAR REGISTRO"):
        nuevo = pd.DataFrame([{"Fecha": fecha_val, "Colegio": colegio, "Anio": anio_div, "Pasajero": f"{p_ape} {p_nom}", "DNI": p_dni, "Plan": plan_sel}])
        nuevo.to_csv(DB_FILE, mode='a', header=False, index=False)
        st.success("Guardado.")

    with col_i:
        # Script mejorado para imprimir evitando menús
        components.html("""
            <script>
            function printDiv() {
                window.parent.focus();
                window.parent.print();
            }
            </script>
            <button onclick="printDiv()" style="background-color: #2E7D32; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;">
            🖨️ IMPRIMIR COMPROBANTE
            </button>
        """, height=70)

    # SIDEBAR
    with st.sidebar:
        st.header("Excel")
        if os.path.exists(DB_FILE):
            df_hist = pd.read_csv(DB_FILE)
            st.download_button("📥 Descargar Todo (CSV)", df_hist.to_csv(index=False).encode('utf-8'), "adhesiones.csv")

    render_footer()
