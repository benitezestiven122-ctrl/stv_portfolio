import streamlit as st
from PIL import Image
import os
import time

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA Y UX
# ==========================================
st.set_page_config(
    page_title="Estiven Serna | Diseño Interactivo", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. INYECCIÓN DE CSS (ESTÉTICA Y ANIMACIONES)
# ==========================================
# Esto mejora la tipografía, añade bordes redondeados y animaciones al pasar el cursor (hover)
custom_css = """
<style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animación de Hover para imágenes */
    img {
        border-radius: 12px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    img:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    /* Estilo para los títulos de sección */
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 3. BASE DE DATOS DE PROYECTOS (ESTRUCTURADA)
# ==========================================
# Divididos por categorías para mejor Arquitectura de la Información
portfolio_data = {
    "3D y Animación": [
        {
            "titulo": "Modelado y Renderizado Hard Surface",
            "herramientas": "Blender | Maya",
            "imagen": "proyecto_3d_1.png",
            "desc_corta": "Creación de assets 3D optimizados con texturizado PBR.",
            "desc_larga": "Elaboración de props y escenarios para entornos inmersivos, cuidando la topología y optimizando los mapas de normales y rugosidad.",
            "enlace": "https://behance.net/tu-enlace"
        },
        {
            "titulo": "Motion Graphics y Composición",
            "herramientas": "After Effects",
            "imagen": "proyecto_ae_1.png",
            "desc_corta": "Animación 2D y postproducción audiovisual.",
            "desc_larga": "Integración de elementos gráficos con video real, trackeo de cámara y diseño de interfaces animadas (FUI).",
            "enlace": "https://behance.net/tu-enlace"
        }
    ],
    "Interactividad y VR": [
        {
            "titulo": "Experiencia en Realidad Virtual",
            "herramientas": "Unity | C#",
            "imagen": "proyecto_vr_1.png",
            "desc_corta": "Mecánicas interactivas para entornos inmersivos.",
            "desc_larga": "Desarrollo de interacciones espaciales, físicas y diseño de nivel en Unity usando XR Interaction Toolkit.",
            "enlace": "https://github.com/tu-enlace"
        }
    ],
    "Audiovisual y Tiempo Real": [
        {
            "titulo": "Sistemas Generativos / VJing",
            "herramientas": "TouchDesigner | Resolume",
            "imagen": "proyecto_vj_1.png",
            "desc_corta": "Arte generativo y visuales reactivos al audio.",
            "desc_larga": "Creación de parches en TouchDesigner que reaccionan a frecuencias sonoras en tiempo real, mapeados para presentaciones en vivo usando Resolume Arena.",
            "enlace": "https://youtube.com/tu-enlace"
        }
    ]
}

# ==========================================
# 4. BARRA LATERAL (NAVEGACIÓN UX)
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Reemplaza por una URL de tu foto de perfil
    st.title("Estiven Serna")
    st.caption("Diseñador Interactivo | 6to Semestre")
    st.divider()
    
    # Menú de navegación simulado
    menu = st.radio(
        "Navegación",
        ["🏠 Inicio", "📂 Mi Trabajo", "🛠️ Habilidades", "✉️ Contacto"]
    )
    
    st.divider()
    st.write("📍 Medellín, Colombia")
    st.write("🔗 [LinkedIn](#)")
    st.write("🔗 [Behance](#)")

# ==========================================
# 5. LÓGICA DE LAS VISTAS (PÁGINAS)
# ==========================================

if menu == "🏠 Inicio":
    # Layout asimétrico para la cabecera (texto a la izq, imagen abstracta a la der)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<p class="section-title">Creando experiencias donde el diseño y la tecnología colisionan.</p>', unsafe_allow_html=True)
        st.write("")
        st.write("""
        Soy un apasionado de la creación audiovisual y el diseño interactivo. 
        Mi enfoque fusiona el arte digital con la programación para crear narrativas visuales, 
        desde **animación 3D/2D** hasta **sistemas generativos y realidad virtual**.
        """)
        if st.button("Ver mi trabajo 🚀"):
            st.info("👆 Usa el menú lateral para ir a 'Mi Trabajo'")
            
    with col2:
        # Aquí puedes poner un GIF de tu reel de animación
        st.image("https://cdn.dribbble.com/users/107759/screenshots/3629471/media/e48f02f067d5ce39097bc751d387f631.gif", use_column_width=True)

elif menu == "📂 Mi Trabajo":
    st.markdown('<p class="section-title">Portafolio de Proyectos</p>', unsafe_allow_html=True)
    st.write("Explora mis disciplinas a través de las siguientes pestañas:")
    
    # Pestañas para dividir la información (Excelente UX)
    tab1, tab2, tab3 = st.tabs(["🎨 3D & Animación", "🕹️ Interactividad & VR", "🎛️ Audiovisual & VJ"])
    
    tabs = [tab1, tab2, tab3]
    categorias = list(portfolio_data.keys())
    
    # Renderizado dinámico de proyectos
    for tab, categoria in zip(tabs, categorias):
        with tab:
            st.write("---")
            # Crear columnas dinámicas basadas en la cantidad de proyectos
            proyectos = portfolio_data[categoria]
            cols = st.columns(2) # Mostramos 2 proyectos por fila para que se vean grandes y limpios
            
            for i, p in enumerate(proyectos):
                col = cols[i % 2]
                with col:
                    # Contenedor del proyecto
                    if os.path.exists(p["imagen"]):
                        st.image(p["imagen"], use_column_width=True)
                    else:
                        # Placeholder estético si no hay imagen
                        st.image("https://via.placeholder.com/600x400/1E1E1E/FFFFFF?text=Imagen+del+Proyecto", use_column_width=True)
                    
                    st.subheader(p["titulo"])
                    st.caption(f"🛠️ {p['herramientas']}")
                    st.write(p["desc_corta"])
                    
                    # Expander para revelación progresiva (No satura al usuario de texto)
                    with st.expander("Ver detalles del proceso"):
                        st.write(p["desc_larga"])
                        st.markdown(f"[Ver proyecto completo]({p['enlace']})")
                    st.write("") # Espaciador

elif menu == "🛠️ Habilidades":
    st.markdown('<p class="section-title">Stack Tecnológico</p>', unsafe_allow_html=True)
    st.write("Herramientas y software que utilizo en mi flujo de trabajo creativo.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("CGI & Animación")
        st.write("Blender")
        st.progress(85)
        st.write("Maya")
        st.progress(70)
        st.write("After Effects")
        st.progress(90)
        
    with col2:
        st.subheader("Interactividad & Tiempo Real")
        st.write("Unity")
        st.progress(75)
        st.write("TouchDesigner")
        st.progress(65)
        st.write("Resolume")
        st.progress(80)

elif menu == "✉️ Contacto":
    st.markdown('<p class="section-title">Hablemos</p>', unsafe_allow_html=True)
    st.write("¿Tienes un proyecto en mente o quieres colaborar? Envíame un mensaje.")
    
    # Formulario simulado de contacto
    with st.form("contacto_form"):
        nombre = st.text_input("Tu Nombre")
        email = st.text_input("Tu Correo Electrónico")
        mensaje = st.text_area("Mensaje")
        enviado = st.form_submit_button("Enviar Mensaje 🚀")
        
        if enviado:
            st.success(f"¡Gracias {nombre}! Tu mensaje ha sido enviado (simulación).")
            st.balloons() # Pequeño detalle de satisfacción (QoL)
