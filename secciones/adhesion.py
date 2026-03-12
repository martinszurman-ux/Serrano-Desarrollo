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
    cd2.text_input("Vencimiento DNI", key="pas_vence_f") 
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1), key="pas_nace_f")
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True, key="pas_sexo_f")

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio Particular", key="pas_dom_f")
    dom2.text_input("Localidad / CP", key="pas_cp_f")

    st.markdown("<hr style='margin: 2px 0;'>", unsafe_allow_html=True)
    
    # Datos de Tutores
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    
    t1_1, t1_2, t1_3 = st.columns([2, 1, 1])
    t1_1.text_input("Nombre y Apellido", key="t1_nom_f")
    t1_2.text_input("CUIL", key="t1_cuil_f")
    t1_3.text_input("Teléfono de Contacto", key="t1_tel_f")
    
    t2_1, t2_2, t2_3 = st.columns([2, 1, 1])
    t2_1.text_input("Nombre y Apellido ", key="t2_nom_f")
    t2_2.text_input("CUIL ", key="t2_cuil_f")
    t2_3.text_input("Teléfono de Contacto ", key="t2_tel_f")
    
    st.text_input("Correo Electrónico (E-mail):", key="tut_email_f")

    # Selección de Plan
    st.pills("Seleccione su Plan de Pago:", 
             options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], 
             default="PLAN 4", key="plan_sel_f")

    # Texto Legal - Reducido al máximo
    st.markdown(f"""
        <div style="font-size: 0.62rem; text-align: justify; border: 1px solid #ccc; padding: 4px; background-color: #f9f9f9; color: black; line-height: 1;">
        Declaro bajo juramento que los datos volcados son exactos y acepto el plan de pagos de SERRANO TURISMO. 
        Los planes al contado deben abonarse dentro de los 30 días. Conozco las condiciones del contrato. 
        <b>NOTA: De no marcar plan, se emitirá PLAN 4.</b>
        </div>
    """, unsafe_allow_html=True)

    # Firmas - Espacio reducido
    st.markdown('<div style="margin-top: 10px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Aclaración y N° de C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Botón de impresión
    components.html(
        """
        <html><body>
            <button style="background-color: #2E7D32; color: white; padding: 10px; border: none; border-radius: 8px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;" 
            onclick="window.parent.print()">🖨️ GENERAR COMPROBANTE PDF</button>
        </body></html>
        """,
        height=60,
    )

    render_footer()
