import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer


def render_adhesion(logo_url):

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
    # Estrategia: en lugar de depender de @media print desde el iframe,
    # el JS inyecta un <style id="print-overrides"> directamente en el
    # documento padre ANTES de imprimir, y lo elimina en afterprint.
    # Esto garantiza que Chrome aplique los estilos correctamente.
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

            // ── 1. OCULTAR ELEMENTOS DE UI ────────────────────────────────
            const selectorsToHide = [
                '.navbar', '.navbar-mobile',
                '[data-testid="stHeader"]', '[data-testid="stToolbar"]',
                '[data-testid="stDecoration"]', '[data-testid="stSidebar"]',
                '[data-testid="stSidebarNav"]',
                '.stButton', 'footer', '.footer-container', '.wa-float', 'iframe',
            ];
            const snapshot = [];
            selectorsToHide.forEach(sel => {
                doc.querySelectorAll(sel).forEach(el => {
                    snapshot.push({ el, prev: el.style.display });
                    el.style.display = 'none';
                });
            });

            // Quitar margin del content-wrapper (espacio reservado para el navbar)
            const wrapper = doc.querySelector('.content-wrapper');
            const prevMargin = wrapper ? wrapper.style.marginTop : null;
            if (wrapper) wrapper.style.marginTop = '0px';

            // ── 2. INYECTAR CSS DE IMPRESIÓN DIRECTO EN EL PADRE ─────────
            // Chrome aplica esto de forma mucho más confiable que @media print
            // desde dentro de un iframe.
            const printStyle = doc.createElement('style');
            printStyle.id = 'serrano-print-overrides';
            printStyle.textContent = `
                @page { size: A4 portrait; margin: 1cm; }

                body, html { background: white !important; }

                /* Quitar todo el padding/margin extra de Streamlit */
                .main .block-container {
                    padding: 0 !important;
                    margin: 0 !important;
                    max-width: 100% !important;
                }
                .content-wrapper {
                    margin-top: 0 !important;
                    padding: 0 !important;
                }

                /* Compactar gaps verticales — esto es lo que genera el espacio en blanco */
                [data-testid="stVerticalBlock"] {
                    gap: 0.25rem !important;
                    row-gap: 0.25rem !important;
                }
                [data-testid="stVerticalBlock"] > * {
                    margin-bottom: 0 !important;
                    padding-bottom: 0 !important;
                }
                /* Gap entre columnas */
                [data-testid="stHorizontalBlock"] {
                    gap: 0.5rem !important;
                }

                /* Inputs: solo línea inferior, sin caja */
                input {
                    border: none !important;
                    border-bottom: 1px solid #000 !important;
                    background: transparent !important;
                    height: 20px !important;
                    font-size: 0.8rem !important;
                    padding: 0 !important;
                }

                /* Tipografía compacta */
                h1 { font-size: 1.1rem !important; margin: 0 0 2px !important; line-height: 1.2 !important; }
                h3 { font-size: 0.82rem !important; margin: 3px 0 1px !important; line-height: 1.2 !important; }
                p  { font-size: 0.78rem !important; margin: 1px 0 !important; line-height: 1.2 !important; }
                label p { font-size: 0.72rem !important; margin: 0 !important; }
                hr { margin: 2px 0 !important; }

                /* Logo de cabecera más chico */
                [data-testid="stImage"] img { max-height: 45px !important; width: auto !important; }

                /* Texto legal */
                div[style*="0.68rem"] {
                    font-size: 0.6rem !important;
                    line-height: 1.05 !important;
                    padding: 4px !important;
                }

                /* Firmas */
                .firmas-container { margin-top: 10px !important; }

                /* Evitar saltos de página dentro del formulario */
                .main { page-break-inside: avoid; }
            `;
            doc.head.appendChild(printStyle);

            // ── 3. IMPRIMIR ───────────────────────────────────────────────
            setTimeout(() => {
                window.parent.print();

                // ── 4. RESTAURAR TODO ─────────────────────────────────────
                function restoreAll() {
                    // Quitar el style inyectado
                    const injected = doc.getElementById('serrano-print-overrides');
                    if (injected) injected.remove();
                    // Restaurar elementos ocultos
                    snapshot.forEach(({ el, prev }) => { el.style.display = prev; });
                    // Restaurar margin del wrapper
                    if (wrapper && prevMargin !== null) wrapper.style.marginTop = prevMargin;
                }

                // Fallback: si afterprint no se dispara (cancelar en Chrome)
                const fallbackTimer = setTimeout(restoreAll, 2000);

                window.parent.addEventListener('afterprint', function restore() {
                    clearTimeout(fallbackTimer);
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
