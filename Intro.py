import streamlit as st
import os

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Portafolio | Estiven Serna", 
    page_icon="🎬", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. INYECCIÓN DE CSS (DISEÑO, ROJO/VINOTINTO Y ANIMACIONES)
# ==========================================
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Fondo principal y sidebar en tonos oscuros elegantes o limpios con acento vinotinto */
    .stApp {
        background-color: #0b0c10;
        color: #e5e5e5;
    }

    [data-testid="stSidebar"] {
        background-color: #14080a !important;
        border-right: 1px solid #3d1217;
    }
    
    /* Gradiente de títulos en tonos Rojos y Vinotinto */
    .title-gradient {
        font-size: 2.8rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #ff1e56, #800020, #b20038);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    /* Tarjetas de proyectos con estética Vinotinto y animaciones fluidas */
    .app-card {
        padding: 1.8rem;
        border-radius: 12px;
        background-color: #1a0b0e;
        border: 1px solid #4a121a;
        margin-bottom: 1.2rem;
        transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.3s ease, border-color 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    .app-card:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow: 0 14px 28px rgba(128, 0, 32, 0.35);
        border-color: #ff1e56;
    }

    /* Estilo personalizado para los botones nativos de enlace */
    .stButton > button, div[data-testid="stLinkButton"] > a {
        background: linear-gradient(135deg, #800020 0%, #b20038 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
        background: linear-gradient(135deg, #b20038 0%, #ff1e56 100%) !important;
        box-shadow: 0 0 15px rgba(255, 30, 86, 0.5) !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. BARRA LATERAL (PERFIL)
# ==========================================
with st.sidebar:
    st.title("Estiven Serna")
    st.subheader("Estudiante de Diseño Interactivo | 6to Semestre")
    st.write("Especializado en animación, creación audiovisual, arte 3D/2D y prototipado de aplicaciones interactivas con Inteligencia Artificial.")
    st.divider()
    st.write("📍 Medellín, Colombia")
    st.write("🔗 [LinkedIn](#)")
    st.write("🔗 [GitHub](#)")

# ==========================================
# 4. BASE DE DATOS DE LAS 10 APLICACIONES (ACTUALIZADAS)
# ==========================================
apps_ia = [
    {
        "titulo": "Visio-Synth: Mapeador de Triggers",
        "tag": "Computer Vision / YOLOv5",
        "icono": "🎛️",
        "desc": "Convierte objetos físicos detectados por la cámara web en disparadores (triggers) de datos. Diseñado conceptualmente para enviar señales OSC/MIDI a software de VJing como Resolume y TouchDesigner.",
        "url": "https://yolov5stv-122.streamlit.app/"
    },
    {
        "titulo": "Typo-Mask VJ Studio",
        "tag": "NLP / Luma Mattes",
        "icono": "🔠",
        "desc": "Transforma textos, guiones y letras de canciones en texturas tipográficas de alto contraste y máscaras Luma Matte. Ideal para emisores de partículas y mapas de desplazamiento en Blender.",
        "url": "https://wordcloudstv-122.streamlit.app"
    },
    {
        "titulo": "Vocal-Synth AV",
        "tag": "Sequence-to-Speech",
        "icono": "🎙️",
        "desc": "Un sampler y sintetizador de voz multilingüe. Traduce entradas de voz y genera archivos de audio profesionales (MP3) listos para usar como diálogos de personajes en Unity o texturas sonoras.",
        "url": "https://traductorstv-122.streamlit.app"
    },
    {
        "titulo": "Prompt-Vault: Búsqueda Semántica",
        "tag": "Information Retrieval / TF-IDF",
        "icono": "🧠",
        "desc": "Sistema de recuperación de información basado en TF-IDF. Permite organizar, clasificar y buscar de forma semántica en tu biblioteca de prompts para IA, texturas y recursos de diseño.",
        "url": "https://tdfespstv-122.streamlit.app"
    },
    {
        "titulo": "Senti-Vision: Dirección de Arte IA",
        "tag": "Clasificación de Texto / Color Grading",
        "icono": "🎭",
        "desc": "Analiza la polaridad y subjetividad de guiones o conceptos narrativos para generar automáticamente paletas de colores (HEX) y parámetros de iluminación para Blender y Unity.",
        "url": "https://sentimentstv-122.streamlit.app"
    },
    {
        "titulo": "Gesture-Synth VJ Controller",
        "tag": "OCR + Machine Learning",
        "icono": "🖐️",
        "desc": "Clasificador de gestos e interacciones físicas mediante modelos entrenados. Traduce posturas de la mano en comandos de control en tiempo real para entornos interactivos.",
        "url": "https://7acrpywfn4dncx2pxs7pb9.streamlit.app"
    },
    {
        "titulo": "OCR Data-Stream",
        "tag": "Optical Character Recognition",
        "icono": "👁️",
        "desc": "Escáner analógico de caracteres que digitaliza texto impreso del mundo real con filtros de binarización avanzados, formateando los datos para su uso en TouchDesigner DATs.",
        "url": "https://ocrstv-122.streamlit.app"
    },
    {
        "titulo": "Narrative-Synth: Voice-Over Studio",
        "tag": "LLM / Text-to-Speech",
        "icono": "🎙️",
        "desc": "Estudio de doblaje sintético para previsualizaciones (Animatics). Convierte monólogos y guiones cinematográficos en assets de audio renderizados de alta calidad.",
        "url": "https://text-to-speech-estivenserna.streamlit.app/"
    },
    {
        "titulo": "Pre-Pro AI: Desglosador de Guiones (RAG)",
        "tag": "RAG / Document AI",
        "icono": "🎬",
        "desc": "Asistente inteligente basado en RAG que analiza documentos PDF y guiones técnicos para extraer automáticamente listados de objetos 3D, esquemas de iluminación y requerimientos de producción.",
        "url": "https://pdf122.streamlit.app"
    },
    {
        "titulo": "LingoEdu: Localizador de Idiomas",
        "tag": "Prototipo Ciberfísico",
        "icono": "📚",
        "desc": "Aplicación interactiva de apoyo al aprendizaje que combina visión artificial y síntesis de voz multilingüe para traducir elementos del entorno físico en experiencias sonoras.",
        "url": "https://ocraudio-122.streamlit.app"
    }
]

# ==========================================
# 5. CONTENIDO PRINCIPAL (PESTAÑAS)
# ==========================================
st.markdown('<p class="title-gradient">Portafolio de Proyectos</p>', unsafe_allow_html=True)
st.write("Explora mis herramientas desarrolladas en la intersección de la Inteligencia Artificial, el diseño interactivo y la creación audiovisual.")

tab1, tab2 = st.tabs(["🧠 Aplicaciones de Inteligencia Artificial", "🎬 Extra: Enfoque Audiovisual y 3D"])

with tab1:
    st.write("### Ecosistema de Herramientas IA")
    st.write("Una colección de aplicaciones prácticas enfocadas en flujos de trabajo creativos, visión por computadora, procesamiento de lenguaje natural y síntesis multimedia.")
    st.write("---")
    
    col1, col2 = st.columns(2)
    
    for i, app in enumerate(apps_ia):
        col = col1 if i % 2 == 0 else col2
        
        with col:
            st.markdown(f"""
            <div class="app-card">
                <h3 style="margin-top: 0; color: #ff1e56;">{app['icono']} {app['titulo']}</h3>
                <p style="color: #c08490; font-size: 0.85em; font-weight: bold; margin-bottom: 12px; letter-spacing: 0.5px;">🏷️ {app['tag'].upper()}</p>
                <p style="color: #d1d5db; line-height: 1.6;">{app['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.link_button(f"🔗 Abrir {app['titulo']}", app['url'], use_container_width=True)
            st.write("") 

with tab2:
    st.write("### Perfil Creativo e Interactivo")
    st.write("Como estudiante de Diseño Interactivo, mi enfoque une la programación de sistemas creativos con la **animación y la producción audiovisual en 3D y 2D**.")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.info("**Programas y Herramientas que domino:**")
        st.write("✔️ **3D y Animación:** Blender, Maya")
        st.write("✔️ **Composición Visual:** After Effects")
        st.write("✔️ **Desarrollo Interactivo:** Unity (C# / XR)")
        st.write("✔️ **VJing y Generativo:** TouchDesigner, Resolume")
        
    with col4:
        st.success("**Enfoque Profesional:**")
        st.write("""
        Busco crear narrativas visuales y experiencias inmersivas que conecten profundamente con los usuarios, 
        fusionando la ingeniería de software, el diseño de interfaces y las artes mediales para explorar nuevas 
        fronteras en la interacción ciberfísica y virtual.
        """)
