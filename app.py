import asyncio
import base64
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from dotenv import load_dotenv
import requests
import streamlit as st
import streamlit.components.v1 as components

# --- FIX ERREUR ASYNCIO / WINERROR 10054 SOUS WINDOWS ---
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# --- CONFIGURATION ENVIRONNEMENT HUGGING FACE & THREADS ---
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

load_dotenv(override=True)

# 1. Configuration de la page
st.set_page_config(
    page_title="CERT Intelligence Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Styles CSS
st.markdown(
    """
<style>
    .stApp { 
        background-color: #0D1117; 
        color: #E6EDF3; 
    }
    [data-testid="stSidebar"] { 
        background-color: #161B22; 
        border-right: 1px solid #30363D; 
    }
    .sidebar-title { 
        font-size: 1.3rem !important; 
        font-weight: 700; 
        color: #58A6FF; 
        padding: 10px 0px; 
    }
    div.stButton > button {
        width: 100%;
        text-align: left !important;
        justify-content: flex-start !important;
        background-color: #21262D;
        color: #C9D1D9 !important;
        border: 1px solid #30363D !important;
        border-radius: 8px !important;
        padding: 10px 16px !important;
        font-size: 0.95rem !important;
        font-weight: 500;
        margin-bottom: 6px;
    }
    div.stButton > button:hover { 
        background-color: #30363D !important; 
        color: #58A6FF !important; 
        border-color: #58A6FF !important;
    }
    .active-nav button {
        background-color: #1F6FEB !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border-color: #388BFD !important;
    }
    .cert-header { 
        text-align: center; 
        padding-top: 5px;
        padding-bottom: 15px; 
    }
    .cert-title { 
        font-size: 2.3rem !important; 
        font-weight: 800; 
        background: linear-gradient(90deg, #58A6FF, #BC8CFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 5px; 
        margin-bottom: 5px; 
    }
    .cert-subtitle { 
        font-size: 1.05rem !important; 
        color: #8B949E; 
    }
    .history-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #8B949E;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
</style>
""",
    unsafe_allow_html=True,
)


def scroll_to_bottom():
    js = """
    <script>
        function scrollToBottom() {
            var mainContainer = window.parent.document.querySelector('.stMain') || window.parent.document.querySelector('.main');
            if (mainContainer) {
                mainContainer.scrollTop = mainContainer.scrollHeight;
            }
            window.parent.scrollTo(0, window.parent.document.body.scrollHeight);
        }
        setTimeout(scrollToBottom, 100);
    </script>
    """
    components.html(js, height=0, width=0)


def nettoyer_texte_parasite(texte: str) -> str:
    """Nettoie les balises <think> et le texte de réflexion tout en préservant le tableau."""
    if not texte:
        return ""

    # Supprime les balises <think> ... </think>
    texte = re.sub(r"<think>.*?</think>", "", texte, flags=re.DOTALL)
    texte = re.sub(r"<think>.*", "", texte, flags=re.DOTALL)

    # Nettoie les retours à la ligne superflus au début
    return texte.strip()


# 3. Cache du moteur LLM Wiki
@st.cache_resource(show_spinner=False)
def load_wiki_engine():
    from utils.query_engine import WikiQueryEngine

    engine = WikiQueryEngine(wiki_dir="wiki", db_dir="chroma_db")

    if hasattr(engine, "index_wiki"):
        try:
            engine.index_wiki()
        except Exception:
            pass

    return engine


def get_engine():
    try:
        return load_wiki_engine()
    except Exception:
        try:
            from utils.query_engine import WikiQueryEngine

            return WikiQueryEngine(wiki_dir="wiki")
        except Exception as e:
            st.error(f"❌ Erreur critique lors du chargement du module : {e}")
            return None


def get_exact_filename_from_url(response, url):
    filename = None
    cd = response.headers.get("content-disposition")
    if cd:
        filenames = re.findall('filename="?([^"]+)"?', cd)
        if filenames:
            filename = filenames[0]

    if not filename:
        parsed_path = urlparse(url).path
        filename = unquote(os.path.basename(parsed_path))

    if not filename or filename == "":
        filename = "document_web"

    filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
    return filename


if "nav_page" not in st.session_state:
    st.session_state.nav_page = "Ingestion de Veille"

if "messages" not in st.session_state:
    st.session_state.messages = []


# 4. Barre latérale (Sidebar)
with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🖥️ Menu Principal</div>',
        unsafe_allow_html=True,
    )
    st.divider()

    if st.session_state.nav_page == "Ingestion de Veille":
        st.markdown('<div class="active-nav">', unsafe_allow_html=True)
        st.button("☁️ Ingestion de Veille", key="nav_ingest_active")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        if st.button("☁️ Ingestion de Veille", key="nav_ingest"):
            st.session_state.nav_page = "Ingestion de Veille"
            st.rerun()

    if st.session_state.nav_page == "Interroger l'IA":
        st.markdown('<div class="active-nav">', unsafe_allow_html=True)
        st.button("💬 Interroger l'IA", key="nav_chat_active")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        if st.button("💬 Interroger l'IA", key="nav_chat"):
            st.session_state.nav_page = "Interroger l'IA"
            st.rerun()

    st.divider()

    st.markdown(
        '<div class="history-header">📜 Historique de Recherche</div>',
        unsafe_allow_html=True,
    )

    if st.button("🗑️ Effacer l'historique", key="clear_chat"):
        st.session_state.messages = []
        st.rerun()

    user_questions = [
        msg for msg in st.session_state.messages if msg["role"] == "user"
    ]

    if not user_questions:
        st.caption("Aucune recherche récente.")
    else:
        for idx, q in enumerate(reversed(user_questions)):
            q_text = q["content"]
            label = (
                f"🔍 {q_text[:28]}..." if len(q_text) > 28 else f"🔍 {q_text}"
            )
            if st.button(label, key=f"hist_btn_{idx}"):
                st.session_state.nav_page = "Interroger l'IA"
                st.session_state.selected_question = q_text
                st.rerun()


# 5. Header Principal
logo_path = os.path.join("assets", "logo_cert.png")

logo_html = ""
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        logo_html = f'<img src="data:image/png;base64,{encoded}" style="width: 380px; max-width: 100%; height: auto; margin-bottom: 10px;">'

st.markdown(
    f"""
<div class="cert-header" style="text-align: center;">
    {logo_html}
    <div class="cert-title">CERT Intelligence Platform</div>
    <div class="cert-subtitle">Système intelligent de veille stratégique autonome & LLM Wiki</div>
</div>
""",
    unsafe_allow_html=True,
)

st.divider()


# ==============================================================================
# ONGLET 1 : INGESTION DE VEILLE
# ==============================================================================
if st.session_state.nav_page == "Ingestion de Veille":
    st.markdown("### 📑 Ingestion de Nouveaux Documents")
    st.markdown(
        "Déposez vos fichiers ou renseignez une URL pour les analyser et les"
        " intégrer dans votre Wiki."
    )

    raw_dir = "raw"
    os.makedirs(raw_dir, exist_ok=True)

    uploaded_files = st.file_uploader(
        "Glissez-déposez vos fichiers ici (PDF, DOCX, MD, TXT, HTML, MP3, MP4,"
        " PNG, JPG, PPTX)",
        type=[
            "pdf",
            "docx",
            "md",
            "txt",
            "html",
            "mp3",
            "mp4",
            "png",
            "jpg",
            "pptx",
        ],
        accept_multiple_files=True,
        key="file_uploader_key",
    )

    url_input = st.text_input(
        "🔗 Ou entrez l'URL d'un document ou d'un webinaire :",
        placeholder="https://example.com/webinaire",
    )

    saved_files = []

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = os.path.join(raw_dir, uploaded_file.name)

            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except PermissionError:
                    st.warning(
                        "⚠️ Le fichier"
                        f" `{uploaded_file.name}` est actuellement utilisé."
                    )

            try:
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                saved_files.append(uploaded_file.name)
            except Exception as e:
                st.error(
                    f"⚠️ Erreur lors de la sauvegarde de {uploaded_file.name} :"
                    f" {e}"
                )

    if url_input.strip():
        try:
            from bs4 import BeautifulSoup

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            response = requests.get(
                url_input.strip(), timeout=20, headers=headers
            )
            response.raise_for_status()

            filename = get_exact_filename_from_url(response, url_input.strip())

            if not os.path.splitext(filename)[1]:
                filename += ".txt"

            file_path = os.path.join(raw_dir, filename)
            content_type = response.headers.get("Content-Type", "")

            if (
                "text/html" in content_type
                or not os.path.splitext(filename)[1]
                or filename.endswith(".txt")
            ):
                soup = BeautifulSoup(response.content, "html.parser")

                for element in soup([
                    "script",
                    "style",
                    "nav",
                    "footer",
                    "header",
                    "noscript",
                    "svg",
                ]):
                    element.decompose()

                text = soup.get_text(separator="\n", strip=True)

                if len(text) > 30000:
                    text = (
                        text[:30000]
                        + "\n... [Texte tronqué pour limiter la taille]"
                    )

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"Source URL : {url_input.strip()}\n\n{text}")
            else:
                with open(file_path, "wb") as f:
                    f.write(response.content)

            saved_files.append(filename)
            st.success(f"🌐 Téléchargé avec succès sous : `{filename}`")

        except Exception as e:
            st.error(f"❌ Erreur lors du téléchargement de l'URL : {e}")

    if saved_files:
        st.success(
            "📁 Fichier(s) prêt(s) dans `./raw/` :"
            f" **{', '.join(saved_files)}**"
        )

        with st.spinner(
            "🤖 Traitement modulaire Groq et réindexation dans le Wiki..."
        ):
            all_success = True
            from utils.ingest import IngestPipeline

            pipeline = IngestPipeline()

            for file_name in saved_files:
                try:
                    file_path = Path(raw_dir) / file_name
                    res_path = pipeline.process_file(file_path)

                    if not res_path:
                        all_success = False
                        st.error(
                            f"❌ Erreur lors du traitement de `{file_name}`"
                        )
                    else:
                        with st.expander(
                            "📄 Fiche générée avec succès pour"
                            f" `{file_name}`"
                        ):
                            st.write(f"Créé dans : `{res_path}`")

                except Exception as e:
                    all_success = False
                    st.error(
                        f"❌ Erreur lors du traitement de `{file_name}` : {e}"
                    )

            if all_success:
                engine = get_engine()
                if engine and hasattr(engine, "index_wiki"):
                    try:
                        engine.index_wiki()
                    except Exception:
                        pass
                st.success(
                    "🎉 Tous les documents et URLs ont été transformés et"
                    " réindexés dans le Wiki avec succès !"
                )


# ==============================================================================
# ONGLET 2 : INTERROGER L'IA
# ==============================================================================
elif st.session_state.nav_page == "Interroger l'IA":
    st.markdown("### 💬 Interroger l'IA")

    # 1. Rendu direct des messages sauvegardés dans l'historique
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 2. Capture de la question (bouton historique ou zone de saisie)
    user_input = None
    if "selected_question" in st.session_state:
        user_input = st.session_state.selected_question
        del st.session_state.selected_question

    chat_prompt = st.chat_input(
        "Posez votre question à la base de connaissances du CERT..."
    )
    if chat_prompt:
        user_input = chat_prompt.strip()

    if user_input:
        # Affiche la question immédiatement dans l'interface
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        engine = get_engine()

        if engine:
            try:
                with st.spinner("🔍 Recherche en cours dans les fiches Wiki..."):
                    res = engine.query(user_input)
                    
                    # On vérifie la structure de retour du moteur RAG/Wiki
                    if isinstance(res, dict):
                        answer_raw = res.get("answer", "Aucune information trouvée.")
                    else:
                        answer_raw = str(res)

                    answer_clean = nettoyer_texte_parasite(answer_raw)

                # Affiche la réponse générée directement dans la page Streamlit
                with st.chat_message("assistant"):
                    st.markdown(answer_clean)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer_clean,
                })
            except Exception as e:
                err_msg = f"❌ Erreur lors de la consultation du Wiki : {e}"
                with st.chat_message("assistant"):
                    st.markdown(err_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": err_msg,
                })
        else:
            err_msg = "❌ Impossible d'initialiser le moteur de recherche."
            with st.chat_message("assistant"):
                st.markdown(err_msg)
            st.session_state.messages.append({
                "role": "assistant",
                "content": err_msg,
            })

        scroll_to_bottom()