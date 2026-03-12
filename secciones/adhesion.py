import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer


def render_adhesion(logo_url):

    # ── ESTILOS GENERALES + MEDIA PRINT ──────────────────────────────────────
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 0rem !important;
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 700 !important;
            font-size: 0.85rem !important;
            margin-bottom: 2px !important;
        }
        input {
            color: black !important;
            background-color: #f8f9fa !important;
            border: 1px solid #ced4da !important;
            height: 30px !important;
        }

        @media print {
            @page {
                size: A4;
                margin: 0.6cm;
            }
            html, body {
                zoom: 72% !important;
                background-color: white !important;
                color: black !important;
            }
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
            }
            /* Compactar espaciados para entrar en una sola hoja */
            .main .block-container > div > div > div {
                gap: 0.2rem !important;
            }
            [data-testid="stVerticalBlock"] {
                gap: 0.2rem !important;
            }
            input {
                border: none !important;
                border-bottom: 1px solid #000 !important;
                background: transparent !important;
                height: 22px !important;
            }
            h1 { font-size: 1.4rem !important; margin-bottom: 4px !important; margin-top: 0 !important; }
            h3 { font-size: 0.95rem !important; margin-top: 6px !important; margin-bottom: 2px !important; }
            hr { margin: 3px 0 !important; }
            p { margin: 2px 0 !important; }
            .firmas-container { margin-top: 20px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # ── CABECERA ──────────────────────────────────────────────────────────────
    c_logo, c_tit = st.columns([1, 5])
    with c_logo:
        st.image(logo_url, width=65)
    with c_tit:
        st.markdown(
            "<h1 style='color: black; margin: 0; padding: 0;'>SOLICITUD DE INGRESO</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='font-weight: bold; color: black; margin-top: -5px;'>Serrano Turismo - Ficha de Adhesión</p>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)

    # ── DATOS DE CONTROL ──────────────────────────────────────────────────────
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

    # ── DATOS DEL PASAJERO ────────────────────────────────────────────────────
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    ap1.text_input("Apellido/s", key="pas_ape_f")
    nom1.text_input("Nombre/s", key="pas_nom_f")

    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL", key="pas_dni_f")
    cd2.text_input("Fecha de Vencimiento DNI", key="pas_vence_f")
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990, 1, 1), key="pas_nace_f")

    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True, key="pas_sexo_f")

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio Particular", key="pas_dom_f")
    dom2.text_input("Localidad / CP", key="pas_cp_f")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)

    # ── DATOS DE TUTORES ──────────────────────────────────────────────────────
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")

    st.markdown("**DATOS TUTOR 1**")
    t1_1, t1_2, t1_3 = st.columns([2, 1, 1])
    t1_1.text_input("Nombre y Apellido", key="t1_nom_f")
    t1_2.text_input("CUIL", key="t1_cuil_f")
    t1_3.text_input("Teléfono de Contacto", key="t1_tel_f")

    st.markdown("**DATOS TUTOR 2**")
    t2_1, t2_2, t2_3 = st.columns([2, 1, 1])
    t2_1.text_input("Nombre y Apellido ", key="t2_nom_f")
    t2_2.text_input("CUIL ", key="t2_cuil_f")
    t2_3.text_input("Teléfono de Contacto ", key="t2_tel_f")

    st.text_input("Correo Electrónico (E-mail):", key="tut_email_f")

    # ── PLAN DE PAGO ──────────────────────────────────────────────────────────
    st.pills(
        "Seleccione su Plan de Pago:",
        options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"],
        default="PLAN 4",
        key="plan_sel_f",
    )

    # ── TEXTO LEGAL ───────────────────────────────────────────────────────────
    st.markdown("""
        <div style="font-size: 0.68rem; text-align: justify; border: 1px solid #ccc;
                    padding: 8px; background-color: #f9f9f9; color: black;
                    border-radius: 5px; line-height: 1.1;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto,
        para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos
        que figura en la solicitud de reserva mencionada anteriormente denominado.<br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi
        y/u otro representante del contingente de referencia.<br>
        <b>NOTA: De no marcar ningun plan de pago, su chequera se emitira como PLAN CUOTAS (PLAN 4).</b>
        </div>
    """, unsafe_allow_html=True)

    # ── FIRMAS ────────────────────────────────────────────────────────────────
    st.markdown('<div class="firmas-container" style="margin-top: 30px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown(
        "<hr style='border:0.5px solid black; margin-bottom:0;'>"
        "<p style='text-align:center; font-size:8pt; color:black;'>Firma Responsable</p>",
        unsafe_allow_html=True,
    )
    f2.markdown(
        "<hr style='border:0.5px solid black; margin-bottom:0;'>"
        "<p style='text-align:center; font-size:7pt; color:black;'>Aclaración y N° de C.U.I.L.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # ── BOTÓN DE IMPRESIÓN CON JS ─────────────────────────────────────────────
    # Fix bug cancelar: Chrome a veces no dispara afterprint si se cancela.
    # Solución: usamos un flag + setTimeout de 2s como fallback de restauración.
    components.html(
        """
        <html><body>
        <button
            id="print-btn"
            style="background-color: #2E7D32; color: white; padding: 10px; border: none;
                   border-radius: 8px; cursor: pointer; width: 100%; font-size: 16px;
                   font-weight: bold;"
            onclick="prepareAndPrint()">
            🖨️ GENERAR COMPROBANTE PDF
        </button>

        <script>
        function prepareAndPrint() {
            const doc = window.parent.document;

            const selectorsToHide = [
                '.navbar',
                '.navbar-mobile',
                '[data-testid="stHeader"]',
                '[data-testid="stToolbar"]',
                '[data-testid="stDecoration"]',
                '[data-testid="stSidebar"]',
                '[data-testid="stSidebarNav"]',
                '.stButton',
                'footer',
                '.footer-container',
                '.wa-float',
                'iframe',
            ];

            const snapshot = [];
            selectorsToHide.forEach(sel => {
                doc.querySelectorAll(sel).forEach(el => {
                    snapshot.push({ el, prev: el.style.display });
                    el.style.display = 'none';
                });
            });

            const wrapper = doc.querySelector('.content-wrapper');
            const prevMargin = wrapper ? wrapper.style.marginTop : null;
            if (wrapper) wrapper.style.marginTop = '0px';

            // Función de restauración reutilizable
            function restoreAll() {
                snapshot.forEach(({ el, prev }) => { el.style.display = prev; });
                if (wrapper && prevMargin !== null) wrapper.style.marginTop = prevMargin;
            }

            setTimeout(() => {
                window.parent.print();

                // Fallback: si afterprint no se dispara (ej. cancelar en Chrome),
                // restauramos igual a los 2 segundos
                const fallbackTimer = setTimeout(restoreAll, 2000);

                window.parent.addEventListener('afterprint', function restore() {
                    clearTimeout(fallbackTimer);  // cancelamos el fallback si afterprint sí se disparó
                    restoreAll();
                    window.parent.removeEventListener('afterprint', restore);
                }, { once: true });

            }, 300);
        }
        </script>
        </body></html>
        """,
        height=70,
    )

    render_footer()
