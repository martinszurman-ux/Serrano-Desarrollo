import streamlit as st
import pandas as pd
import os
from utilidades.footer import render_footer

def render_tarifas(destino):
    # 1. INICIALIZACIÓN DE SESIÓN Y CARPETAS
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # Lógica para San Pedro: Selección de año
    archivo_nombre = "tarifas_y_formas_de_pago.csv"
    if destino == "San Pedro":
        st.markdown("<h4 style='margin-bottom:0px;'>🗓️ Temporada del viaje</h4>", unsafe_allow_html=True)
        temporada = st.segmented_control(
            "Temporada", 
            options=["Temporada 2026", "Temporada 2027"], 
            default="Temporada 2026",
            # label_visibility="collapsed" # Comentado para compatibilidad si da error
        )
        archivo_nombre = "tarifas_2026.csv" if temporada == "Temporada 2026" else "tarifas_2027.csv"
        suffix = "2026" if temporada == "Temporada 2026" else "2027"
        session_key = f"sel_index_{folder}_{suffix}"
        header_path = f"data/{folder}/tarifariosanpedro.jpg"
    else:
        session_key = f"sel_index_{folder}"
        header_path = f"data/{folder}/tarifas_y_formas_header.png"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (VERSIÓN BLINDADA PARA MODO OSCURO)
    st.markdown("""
        <style>
        [data-testid="stImage"] { margin-top: -55px; margin-bottom: -20px; }
        .contenedor-selector-pago { display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; margin: 10px 0; }
        div[data-testid="stPills"] > div { justify-content: center !important; display: flex !important; gap: 6px; }
        
        /* Quitamos el color quemado para que se vuelva blanco en modo oscuro */
        .instruccion-pago { text-align: center; font-weight: 700; margin-bottom: 8px; font-size: 0.95rem; }
        
        /* Itinerarios más chicos - Forzamos el texto a oscuro */
        .plan-card-container { border-radius: 12px; padding: 10px; background: #E8E8E8 !important; border: 1px solid #d1d1d1; text-align: center; min-height: 110px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 5px; transition: all 0.3s ease; }
        .selected-plan { border: 2px solid #4A90E2 !important; background-color: #ffffff !important; box-shadow: 0px 2px 8px rgba(0,0,0,0.05); }
        .header-content { display: flex; justify-content: center; align-items: center; gap: 8px; width: 100%; }
        .day-number { color: #4A90E2 !important; font-size: 2.2rem; font-weight: 900; line-height: 1; margin: 0; }
        .transport-icon { font-size: 1.5rem; line-height: 1; margin: 0; }
        .day-text { color: #1a1a1a !important; font-size: 0.7rem; font-weight: 900; text-transform: uppercase; margin-top: 5px; }
        
        /* Hero Widget (Caja de precio) - Textos oscuros forzados */
        .hero-payment-card { background: linear-gradient(145deg, #ffffff, #f0f2f6) !important; border-radius: 20px; padding: 20px 30px; text-align: center; border: 1px solid #e0e4e8; box-shadow: 10px 10px 30px #d9dbe0; max-width: 400px; margin: 15px auto; transition: all 0.5s ease; cursor: default; }
        .hero-payment-card:hover { transform: translateY(-5px); }
        .hero-label { color: #1a1a1a !important; font-size: 0.8rem; font-weight: 900; text-transform: uppercase; margin-bottom: 5px; }
        /* Simplificamos el color del valor para que no falle en iOS/Android */
        .hero-value { color: #1a1a1a !important; font-size: 2.8rem; font-weight: 900; margin: 0; line-height: 1; -webkit-text-fill-color: #1a1a1a !important; }
        .hero-subtitle { color: #4A90E2 !important; font-size: 1rem; font-weight: 900; margin-top: 5px; }
        
        /* Beneficio más discreto */
        .beneficio-box { max-width: 600px; margin: 15px auto; padding: 12px; background-color: #f0f7ff !important; border-radius: 10px; border: 1px dashed #4A90E2 !important; }
        
        .styled-table th { background-color: #333333 !important; color: white !important; font-size: 0.8rem; padding: 5px !important; }
        .styled-table td { font-size: 0.8rem; padding: 5px !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- 3. CARGA DE IMAGEN ---
    if os.path.exists(header_path):
        _, col_img, _ = st.columns([1.5, 3, 1.5])
        with col_img: st.image(header_path)

    # --- 4. CARGA DE DATOS ---
    path_tarifas = f"data/{folder}/{archivo_nombre}"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        df.columns = df.columns.str.strip()
        
        def clean_val(val):
            if pd.isna(val) or val == '': return 0.0
            clean = str(val).replace('$', '').replace('.', '').replace(',', '').replace('s', '').strip()
            try: return float(clean)
            except: return 0.0

        # --- SECCIÓN 1: ITINERARIO ---
        st.markdown("<h4 style='margin-bottom:10px;'>📅 Itinerario</h4>", unsafe_allow_html=True)
        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))
        
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else ""
            
            # CAMBIO: Si el destino es San Pedro, forzamos icono de micro.
            if destino == "San Pedro" or "bus" in plan.lower():
                icono = "🚌"
            else:
                icono = "✈️"
            
            with cols_p[i]:
                es_activo = st.session_state
