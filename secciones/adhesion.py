import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
from utilidades.footer import render_footer

def render_adhesion(logo_url):
    # CSS DEFINITIVO: Elimina logos gigantes y menús superiores al imprimir
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
        
        /* --- ESTILOS DE IMPRESIÓN (EL ESCUDO ANTI-LOGOS) --- */
        @media print {
            /* 1. OCULTAR TODO EL MARCO DE STREAMLIT (Menús, logos gigantes, header) */
            header, footer, nav, 
            [data-testid="stHeader"], 
            [data-testid="stSidebar"], 
            [data-testid="stSidebarNav"],
            [data-testid="stImage"], /* Esto mata los logos gigantes */
            .stButton, iframe, #MainMenu, .no-print { 
                display: none !important; 
                visibility: hidden !important;
                height: 0 !important;
                margin: 0 !important;
            }

            /* 2. RESET DE PÁGINA A4 */
            @page { 
                size: A4; 
                margin: 1cm; /* Margen para que no se corte nada */
            }
            html, body { 
                zoom: 85% !important; /* Ajuste para que entre todo en una carilla */
                background-color: white !important;
                color: black !important;
            }
            
            .main .block-container { 
                padding: 0 !important; 
                margin: 0 !important; 
                max-width: 100% !important;
            }
            
            /* 3. CONVERTIR INPUTS EN LÍNEAS */
            input { 
                border: none !important; 
                border-bottom: 1px solid #000 !important; 
                background: transparent !important; 
            }

            /* 4. AJUSTE DE TÍTULOS E INTERLINEADO */
            h1 { font-size: 1.6rem !important; margin-bottom: 10px !important; }
            h3 { font-size: 1.1rem !important; margin-top: 15px !important; }
            hr { margin: 8px 0 !important; }
            
            /* Asegurar que las firmas queden al
