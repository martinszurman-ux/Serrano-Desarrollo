import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # CSS Ultra-compacto y correctivo para impresión
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
            font-size: 0.75rem !important;
            margin-bottom: 0px !important;
        }
        input {
            color: black !important;
            background-color: #f8f9fa !important;
            border: 1px solid #ced4da !important;
            height: 26px !important;
        }
        
        /* FUERZA LA DESAPARICIÓN DE LOGOS Y ESPACIOS EN BLANCO AL IMPRIMIR */
        @media print {
            @page { 
                size: A4; 
                margin: 0.4cm; 
            }
            html, body { 
                zoom: 80%; 
                height: auto !important;
            }
            /* OCULTAR TODO LO QUE NO SEA TEXTO DE LA FICHA */
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], 
            .stButton, [data-testid="stImage"], header, footer, iframe { 
                display: none !important; 
                height: 0px !important;
            }
            .main .block-container { 
                padding: 0 !important; 
                margin: 0 !important; 
            }
            input { 
                border: none !important; 
                border-bottom: 1px solid #000 !important; 
                background: transparent !important; 
            }
            /* Reducir espacios entre widgets de Streamlit */
            div[data-testid="stVerticalBlock"] > div {
                margin-bottom: -10px !important;
            }
            hr { margin: 4px 0 !important; }
            h1 { font-size: 1.4rem !important; margin: 0 !important; }
            h3 { font-size: 1rem !important; margin: 4px 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera (El logo se ve en web, pero desaparece en el PDF por el CSS de arriba)
    c_logo, c_tit = st.columns([1, 5])
    with c_logo:
        st.image(logo_url, width=65)
    with c_tit:
        st.markdown("<h1 style='color: black; margin: 0; padding: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black; margin-top: -5px;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)

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

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
    # Datos del Pasajero
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    ap1.text_input("Apellido/s", key="pas_ape_f")
    nom1.text_input("Nombre/s", key="pas_nom_f")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL", key="pas_dni_f")
    cd2.text_input("Fecha de Vencimiento DNI", key="pas_vence_f") 
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1), key="pas_nace_f")
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True, key="pas_sexo_f")

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio Particular", key="pas_dom_f")
    dom2.text_input("Localidad / CP", key="pas_cp_f")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
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

    st.pills("Seleccione su Plan de Pago:", 
             options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], 
             default="PLAN 4", key="plan_sel_f")

    # Texto Legal Completo
    st.markdown(f"""
        <div style="font-size: 0.65rem; text-align: justify; border: 1px solid #ccc; padding: 6px; background-color: #f9f9f9; color: black; border-radius: 5px; line-height: 1.1; margin-top: 5px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente denominado.<br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br>
        <b>NOTA: De no marcar ningun plan de pago, su chequera se emitira como PLAN CUOTAS (PLAN 4).</b>
        </div>
    """, unsafe_allow_html=True)

    # Firmas
    st.markdown('<div style="margin-top: 15px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Aclaración y N° de C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Botón de impresión (Se oculta solo al imprimir)
    components.html(
        """
        <html><body>
            <button style="background-color: #2E7D32; color: white; padding: 10px; border: none; border-radius: 8px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;" 
            onclick="window.parent.print()">🖨️ GENERAR COMPROBANTE PDF</button>
        </body></html>
        """,
        height=70,
    )

    render_footer()
