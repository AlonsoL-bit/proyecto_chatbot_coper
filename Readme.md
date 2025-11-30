# 💧 Chatbot Coper - Cooperativa de Agua de Graneros

Este proyecto consiste en la implementación de un **Chatbot Asistente Virtual** basado en Modelos de Lenguaje de Gran Escala (LLMs). El sistema, denominado "Coper", utiliza la API de Google Gemini para responder preguntas frecuentes de los socios de la Cooperativa de manera contextual y natural.

## 📋 Descripción del Proyecto

El objetivo es automatizar la atención al cliente resolviendo consultas sobre:
- Horarios de atención de la cooperativa
- Métodos de pago disponibles
- Ubicación y contacto de emergencias
- Requisitos para nuevos socios
- Información sobre cortes de agua programados

## 🚀 Tecnologías Utilizadas

- **Lenguaje:** Python 3.13+
- **Interfaz (Frontend):** Streamlit
- **Motor de IA (Backend):** Google Gemini API
- **Gestión de Variables de Entorno:** Python-dotenv
- **Librerías principales:**
  - `streamlit` - Para la interfaz web interactiva
  - `google-generativeai` - Para integración con Google Gemini
  - `python-dotenv` - Para gestionar variables de entorno

## ⚙️ Instrucciones de Instalación

### Requisitos Previos

- Python 3.10 o superior instalado
- Git (para clonar el repositorio)
- Una API Key válida de Google Generative AI

### Pasos de Instalación

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/AlonsoL-bit/proyecto_chatbot_coper.git
cd proyecto_chatbot_coper
```

#### 2. Crear un Entorno Virtual

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar las Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install streamlit google-generativeai python-dotenv
```

#### 4. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```
GOOGLE_API_KEY=tu_api_key_aqui
```

**Para obtener tu API Key de Google Generative AI:**
1. Accede a [Google AI Studio](https://aistudio.google.com)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key desde el panel de control
4. Copia la clave y pégala en el archivo `.env`

⚠️ **IMPORTANTE:** Nunca publiques tu `.env` en repositorios públicos. Asegúrate de que esté incluido en el `.gitignore`.

## 🎯 Cómo Usar la Aplicación

### Ejecutar la Aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Interacción con el Chatbot

1. Escribe tu consulta en el campo de entrada
2. El chatbot responderá basado en la información programada de la cooperativa
3. Si no tiene información disponible, sugerirá contactar a la oficina

## 📁 Estructura del Proyecto

```
proyecto_chatbot_coper/
├── app.py                 # Archivo principal de la aplicación Streamlit
├── .env                   # Variables de entorno (no incluir en Git)
├── .gitignore            # Archivos a ignorar en Git
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## 🔧 Configuración Personalizada

La personalidad y conocimiento del chatbot se define en la variable `SYSTEM_INSTRUCTION` dentro de `app.py`. Puedes modificar:

- **Nombre del asistente:** Cambia "Coper" por otro nombre
- **Datos de la cooperativa:** Actualiza horarios, contactos, ubicación, etc.
- **Idioma:** Cambia las instrucciones a otro idioma si lo necesitas
- **Comportamiento:** Ajusta las reglas de respuesta según tus necesidades

## 📝 Variables de Entorno

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `GOOGLE_API_KEY` | Clave de API de Google Generative AI | Sí |

## ⚠️ Troubleshooting

### Error: "GOOGLE_API_KEY not found"
- Verifica que el archivo `.env` existe en la raíz del proyecto
- Asegúrate de haber ingresado correctamente la API Key

### Error: "Import streamlit could not be resolved"
- Asegúrate de estar en el entorno virtual activado
- Instala las dependencias nuevamente: `pip install -r requirements.txt`

### El chatbot no responde correctamente
- Verifica que la API Key sea válida
- Revisa la conexión a internet
- Comprueba que el modelo configurado esté disponible

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes preguntas o problemas, por favor abre un issue en el repositorio.

---

**Última actualización:** Noviembre 2025
