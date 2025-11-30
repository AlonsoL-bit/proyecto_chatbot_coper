import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- 1. CONFIGURACIÓN ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Coper - Cooperativa de Agua", page_icon="💧")

# --- 2. PERSONALIDAD Y DATOS (Base de Conocimiento) ---
SYSTEM_INSTRUCTION = """
INSTRUCCIONES:
Eres 'Coper', el asistente virtual de la Cooperativa de Agua de Graneros.
Responde dudas frecuentes de forma amable, breve y servicial.

DATOS OFICIALES DE LA COOPERATIVA:
- Horario de atención: Lunes a Viernes de 08:30 a 14:00 y 15:00 a 17:30.
- Dirección: Av. La Compañía 123, Graneros.
- Emergencias: +56 72 247 1234 (Disponible 24/7).
- Pagos: 
  1. Presencial (Efectivo/Tarjeta).
  2. Transferencia (Cuenta Rut 12345678, correo pagos@cooperativagraneros.cl).
  3. Webpay en el sitio web.
- Cortes de agua: No hay cortes programados actualmente.
- Requisitos nuevo socio: Escritura de propiedad, certificado de dominio vigente y carnet de identidad.

REGLAS:
- Si no sabes la respuesta, sugiere llamar a la oficina. No inventes datos.
"""

st.title("💧 Chatbot Coper")
st.markdown("Atención automática **Cooperativa de Agua de Graneros**.")

if not api_key:
    st.error("⚠️ Falta la API Key en el archivo .env")
    st.stop()

genai.configure(api_key=api_key)

# --- 3. MODELO SELECCIONADO (De tu lista) ---
# Usamos 'gemini-2.0-flash' porque es rápido y estable para chats.
try:
    model = genai.GenerativeModel('models/gemini-2.0-flash')
except Exception as e:
    st.error(f"Error al configurar el modelo: {e}")
    st.stop()

# --- 4. HISTORIAL DE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "model", "content": "¡Hola! Soy Coper 💧. ¿En qué puedo ayudarte hoy?"}]

for msg in st.session_state.messages:
    role_ui = "assistant" if msg["role"] == "model" else "user"
    st.chat_message(role_ui).markdown(msg["content"])

# --- 5. LÓGICA DE RESPUESTA ---
if prompt := st.chat_input("Escribe tu consulta..."):
    # Mostrar mensaje usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    
    try:
        # Contexto manual
        gemini_history = [
            {"role": "user", "parts": [SYSTEM_INSTRUCTION]},
            {"role": "model", "parts": ["Entendido. Soy Coper."]}
        ]
        
        for msg in st.session_state.messages:
            gemini_history.append({"role": msg["role"], "parts": [msg["content"]]})

        # Enviar chat
        chat = model.start_chat(history=gemini_history[:-1])
        response = chat.send_message(prompt)
        
        # Mostrar respuesta
        st.session_state.messages.append({"role": "model", "content": response.text})
        st.chat_message("assistant").markdown(response.text)

    except Exception as e:
        if "429" in str(e):
            st.warning("⏳ Límite de velocidad. Espera unos segundos e intenta de nuevo.")
        else:
            st.error(f"Ocurrió un error: {e}")