import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # CSS AVANZADO: Limpieza absoluta para PDF
    st.markdown("""
        <style>
        /* Ajustes de visualización en Web */
        .main { background-color: white !important; }
        .stTextInput input, .stDateInput div { background-color: #fcfcfc !important; }
        
        /* --- MAGIA PARA IMPRESIÓN --- */
        @media print {
            /* Ocultar elementos de UI de Streamlit y el botón de imprimir */
            header, footer, nav, [data-testid="stHeader"], [data-testid="stSidebar"], 
            .stButton, iframe, #MainMenu, .no-print {
                display: none !important;
            }

            /* Forzar que el contenedor use todo el ancho */
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
            }

            /* Estilo de Formulario Oficial */
            body { font-family: 'Helvetica', 'Arial', sans-serif; color: black !important; }
            h1 { font-size: 22pt !important; margin-bottom: 5px !important; }
            h3 { 
                font-size: 14pt !important; 
                border-bottom: 2px solid #333; 
                padding-bottom: 3px;
                margin-top: 20px !important; 
            }
            
            /* Convertir inputs de Streamlit en líneas simples */
            [data-testid="stWidgetLabel"] p {
                font-size: 9pt !important;
                color: #555 !important;
                text-transform: uppercase;
                margin-bottom: -5px !important;
            }
            
            input {
                border: none !important;
                border-bottom: 1px solid black !important;
                border-radius: 0 !important;
                padding: 0 !important;
                font-size: 11pt !important;
                font-weight: bold !important;
                background: transparent !important;
            }

            /* Ajuste de columnas para que no se apilen en el PDF */
            [data-testid="column"] {
                flex: 1 1 0% !important;
                min-width: 0 !important;
            }

            @page {
                size: A4;
                margin: 1.5cm;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Encabezado Profesional
    col_logo, col_tit = st.columns([1, 4])
    with col_logo:
        st.image(logo_url, width=80)
    with col_tit:
        st.markdown("<h1 style='color: black; margin-bottom:0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.2rem; color: #444;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("---")

    # --- SECCIÓN 1: CONTROL ---
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3 = st.columns([1, 1, 1])
    c1.date_input("Fecha de Solicitud", datetime.now())
    c2.text_input("N° de Cliente", placeholder="Ej: 2026-X")
    c3.text_input("N° de Contrato")

    c4, c5 = st.columns([2, 1])
    c4.text_input("Establecimiento Educativo")
    c5.text_input("Año / División")

    # --- SECCIÓN 2: PASAJERO ---
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap, nom = st.columns(2)
    ap.text_input("Apellido/s")
    nom.text_input("Nombre/s")
    
    d1, d2, d3 = st.columns([1, 1, 1])
    d1.text_input("DNI / CUIL")
    d2.date_input("Fecha de Nacimiento", min_value=datetime(1990, 1, 1))
    d3.text_input("Sexo (M/F/X)")

    dom, loc = st.columns([2, 1])
    dom.text_input("Domicilio Particular")
    loc.text_input("Localidad / CP")

    # --- SECCIÓN 3: TUTORES ---
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    st.markdown("**TUTOR 1**")
    t1_a, t1_b, t1_c = st.columns([2, 1, 1])
    t1_a.text_input("Nombre y Apellido", key="t1_n")
    t1_b.text_input("CUIL", key="t1_c")
    t1_c.text_input("Teléfono", key="t1_t")

    st.markdown("**TUTOR 2**")
    t2_a, t2_b, t2_c = st.columns([2, 1, 1])
    t2_a.text_input("Nombre y Apellido", key="t2_n")
    t2_b.text_input("CUIL", key="t2_c")
    t2_c.text_input("Teléfono", key="t2_t")
    
    st.text_input("Correo Electrónico de Contacto")

    # Plan de Pago (Simplificado para impresión)
    st.markdown("---")
    st.selectbox("Plan de Pago Elegido", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4 (Cuotas)", "PLAN 5", "OTRO"])

    # Texto Legal
    st.markdown(f"""
        <div style="font-size: 0.75rem; text-align: justify; border: 1px solid #000; padding: 10px; color: black; line-height: 1.2; margin-top: 10px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelación de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos seleccionado. 
        Los planes al contado deberán abonarse dentro de los 30 días de firmado el contrato. Declaro conocer todas y cada una de las condiciones del contrato suscripto.
        </div>
    """, unsafe_allow_html=True)

    # Espacio para Firmas
    st.markdown("<br><br>", unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    with f1:
        st.markdown("<div style='border-top: 1px solid black; text-align: center; font-size: 9pt; color: black;'>Firma Responsable</div>", unsafe_allow_html=True)
    with f2:
        st.markdown("<div style='border-top: 1px solid black; text-align: center; font-size: 9pt; color: black;'>Aclaración y N° de C.U.I.L.</div>", unsafe_allow_html=True)

    # Botón de impresión (Se oculta solo al imprimir)
    st.markdown('<div class="no-print">', unsafe_allow_html=True)
    components.html(
        """
        <button style="background-color: #e67e22; color: white; padding: 15px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-size: 18px; font-weight: bold;" 
        onclick="window.parent.print()">🖨️ DESCARGAR / IMPRIMIR FICHA</button>
        """, height=80
    )
    st.markdown('</div>', unsafe_allow_html=True)

    render_footer()
