import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- 1. CONFIGURACIÓN ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Coper - Cooperativa de Agua", page_icon="💧")

# --- 2. CEREBRO DEL BOT (Datos Oficiales) ---
SYSTEM_INSTRUCTION = """
ROL:
Eres 'Coper', el asistente virtual de la Cooperativa de Agua de Graneros.
Tu público son adultos mayores: responde con respeto, usa palabras sencillas y sé breve.

BASE DE CONOCIMIENTO OFICIAL:

1. TARIFAS 2024 (Vigentes desde Abril):
- Cargo Fijo Mensual: $2.000.
- Valor por metro cúbico ($m^3$) según tramos:
  * Tramo Básico (0-15 $m^3$): $730.
  * Tramo Medio (16-30 $m^3$): $980.
  * Tramo Alto (31-45 $m^3$): $1.480.
  * Sobreconsumo (46+ $m^3$): $2.190.

2. PROBLEMAS TÉCNICOS:
- Agua blanca: Es aire atrapado. Dejar correr. Es segura.
- Olor a Cloro: Norma entre 0.7 y 0.8. Dejar correr si estuvo estancada.
- Poca Presión: Tuberías antiguas y alto consumo. Estamos trabajando en unir un segundo estanque.

3. CORTES DE AGUA:
- Programados: Se avisan con tiempo. Lavado de estanque 2 veces al año.
- Emergencias: Roturas de matriz. Corte inmediato. Reparación aprox 2 horas.

4. BENEFICIOS SOCIALES:
- Cuota mortuoria, ayuda floral y caja mercadería.
- Becas escolares.
- Fiestas costumbristas.

5. CONTACTO:
- Av. La Compañía 123, Graneros.
- Lun-Vie 08:30-14:00 y 15:00-17:30.
- Emergencias (24/7): +56 72 247 1234.
"""

st.title("💧 Chatbot Coper")
st.markdown("Atención automática **Cooperativa de Agua de Graneros**.")

if not api_key:
    st.error("⚠️ Falta la API Key en el archivo .env")
    st.stop()

genai.configure(api_key=api_key)

# --- 3. FUNCIÓN DE PROCESAMIENTO ---
def procesar_mensaje(texto_usuario):
    st.session_state.messages.append({"role": "user", "content": texto_usuario})
    
    try:
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        
        gemini_history = [
            {"role": "user", "parts": [SYSTEM_INSTRUCTION]},
            {"role": "model", "parts": ["Entendido. Soy Coper."]}
        ]
        
        for msg in st.session_state.messages:
            gemini_history.append({"role": msg["role"], "parts": [msg["content"]]})

        chat = model.start_chat(history=gemini_history[:-1])
        response = chat.send_message(texto_usuario)
        
        st.session_state.messages.append({"role": "model", "content": response.text})
        st.rerun()

    except Exception as e:
        st.error(f"Error de conexión: {e}")

# --- 4. HISTORIAL VISUAL (AQUÍ ESTÁ EL CAMBIO) ---
# Cambiamos el mensaje inicial para que invite a usar los botones
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "model", 
        "content": "¡Hola! Soy Coper 💧. Tengo las tarifas actualizadas 2024. **Selecciona una opción de abajo para ayudarte:**"
    }]

for msg in st.session_state.messages:
    role_ui = "assistant" if msg["role"] == "model" else "user"
    st.chat_message(role_ui).markdown(msg["content"])

# --- 5. BOTONES DE OPCIONES RÁPIDAS ---
# Se muestran siempre que el último mensaje sea de Coper
if st.session_state.messages[-1]["role"] == "model":
    st.write("---") # Línea separadora
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("💰 Tarifas 2024"):
            procesar_mensaje("Quiero saber los precios y tarifas del agua 2024")
    
    with col2:
        if st.button("🚰 Cortes"):
            procesar_mensaje("¿Por qué se corta el agua? Diferencia entre corte programado y emergencia")
            
    with col3:
        if st.button("👵 Beneficios"):
            procesar_mensaje("¿Qué beneficios tiene ser socio de la cooperativa?")
            
    with col4:
        if st.button("📍 Ubicación"):
            procesar_mensaje("Dame la dirección y horario de atención")

# --- 6. BARRA DE CHAT ---
if prompt := st.chat_input("O escribe otra consulta aquí..."):
    procesar_mensaje(prompt)