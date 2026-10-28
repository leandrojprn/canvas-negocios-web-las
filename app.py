import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.utils import ImageReader
import io

st.set_page_config(
    page_title="Canvas - Prof. Leandro A. da Silva",
    page_icon="📊",
    layout="wide"
)

CANVAS_BLOCKS = [
    {"id": "KP", "title": "1. Parcerias Principais"},
    {"id": "KA", "title": "2. Atividades-Chave"},
    {"id": "KR", "title": "3. Recursos Principais"},
    {"id": "VP", "title": "4. Proposta de Valor"},
    {"id": "CR", "title": "5. Relacionamento com Clientes"},
    {"id": "CH", "title": "6. Canais"},
    {"id": "CS", "title": "7. Segmentos de Clientes"},
    {"id": "C$", "title": "8. Estrutura de Custos"},
    {"id": "R$", "title": "9. Fontes de Receita"},
]

POSTIT_COLORS = {
    "Verde": "#A8E6CF",
    "Amarelo": "#FEF38B",
    "Azul": "#93E1D8",
    "Rosa": "#FFB7B2",
    "Laranja": "#FFDAC1"
}

APP_TITLE = "Modelo de Negócios Canvas do Professor Leandro A. da Silva"
LEGAL_CREDIT = "Metodologia baseada no Business Model Canvas por Alexander Osterwalder e Yves Pigneur (Strategyzer.com), sob licença CC BY-SA 3.0."

if "canvas_data" not in st.session_state:
    st.session_state.canvas_data = {b["id"]: [] for b in CANVAS_BLOCKS}

st.title("📊 " + APP_TITLE)

# Barra Lateral: Inserção de Notas
st.sidebar.header("📌 Adicionar Post-it")
bloco_selecionado = st.sidebar.selectbox("Selecione o Bloco:", [b["id"] + " - " + b["title"] for b in CANVAS_BLOCKS])
bloco_id = bloco_selecionado.split(" - ")[0]

cor_selecionada = st.sidebar.selectbox("Cor do Post-it:", list(POSTIT_COLORS.keys()), index=0)
texto_postit = st.sidebar.text_area("Texto do Post-it:", max_chars=120, height=80)

if st.sidebar.button("Adicionar Nota", use_container_width=True):
    if texto_postit.strip():
        st.session_state.canvas_data[bloco_id].append({
            "text": texto_postit.strip(),
            "color": POSTIT_COLORS[cor_selecionada]
        })
        st.sidebar.success("Post-it adicionado!")
        st.rerun()

# Metadados
col_meta1, col_meta2 = st.columns(2)
with col_meta1:
    projeto_nome = st.text_input("Título do Projeto:", value="", placeholder="Ex: Plataforma EdTech Seridó")
with col_meta2:
    segmento_nome = st.text_input("Segmento / Setor:", value="", placeholder="Ex: Educação / Agronegócio")

# Abas Principais
tab_canvas, tab_comments = st.tabs(["📊 Canvas Interativo", "📝 Comentários & Observações (Opcional)"])

with tab_canvas:
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.subheader("Parcerias")
        for idx, item in enumerate(st.session_state.canvas_data["KP"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_KP_{idx}"):
                st.session_state.canvas_data["KP"].pop(idx)
                st.rerun()
                
    with col2:
        st.subheader("Atividades")
        for idx, item in enumerate(st.session_state.canvas_data["KA"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_KA_{idx}"):
                st.session_state.canvas_data["KA"].pop(idx)
                st.rerun()
                
        st.subheader("Recursos")
        for idx, item in enumerate(st.session_state.canvas_data["KR"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_KR_{idx}"):
                st.session_state.canvas_data["KR"].pop(idx)
                st.rerun()

    with col3:
        st.subheader("Proposta de Valor")
        for idx, item in enumerate(st.session_state.canvas_data["VP"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_VP_{idx}"):
                st.session_state.canvas_data["VP"].pop(idx)
                st.rerun()

    with col4:
        st.subheader("Relacionamento")
        for idx, item in enumerate(st.session_state.canvas_data["CR"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_CR_{idx}"):
                st.session_state.canvas_data["CR"].pop(idx)
                st.rerun()
                
        st.subheader("Canais")
        for idx, item in enumerate(st.session_state.canvas_data["CH"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_CH_{idx}"):
                st.session_state.canvas_data["CH"].pop(idx)
                st.rerun()

    with col5:
        st.subheader("Segmentos")
        for idx, item in enumerate(st.session_state.canvas_data["CS"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_CS_{idx}"):
                st.session_state.canvas_data["CS"].pop(idx)
                st.rerun()

    st.divider()
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("Estrutura de Custos")
        for idx, item in enumerate(st.session_state.canvas_data["C$"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_C$_{idx}"):
                st.session_state.canvas_data["C$"].pop(idx)
                st.rerun()

    with col_c2:
        st.subheader("Fontes de Receita")
        for idx, item in enumerate(st.session_state.canvas_data["R$"]):
            st.markdown(f"<div style='background-color:{item['color']}; padding:8px; border-radius:6px; margin-bottom:5px; color:#111;'><b>{item['text']}</b></div>", unsafe_allow_html=True)
            if st.button("Remover", key=f"del_R$_{idx}"):
                st.session_state.canvas_data["R$"].pop(idx)
                st.rerun()

with tab_comments:
    comentarios = st.text_area("Observações, hipóteses e diagnósticos estratégicos:", height=150)

def gerar_canvas_img():
    width, height = 2400, 1600
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    header_h = 130
    draw.rectangle([(0, 0), (width, header_h)], fill="#1A252F")
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 36)
        sub_font = ImageFont.truetype("arial.ttf", 20)
        block_font = ImageFont.truetype("arialbd.ttf", 22)
        note_font = ImageFont.truetype("arialbd.ttf", 17)
        legal_font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        title_font = block_font = note_font = sub_font = legal_font = ImageFont.load_default()

    draw.text((40, 24), APP_TITLE, fill="#FFFFFF", font=title_font)
    meta_text = f"Projeto: {projeto_nome or 'Não informado'}   |   Segmento: {segmento_nome or 'Geral'}"
    draw.text((42, 82), meta_text, fill="#BDC3C7", font=sub_font)

    GRID_BLOCKS = [
        {"id": "KP", "title": "Parcerias Principais", "col": 0, "row": 0, "colspan": 2, "rowspan": 2},
        {"id": "KA", "title": "Atividades-Chave", "col": 2, "row": 0, "colspan": 2, "rowspan": 1},
        {"id": "VP", "title": "Proposta de Valor", "col": 4, "row": 0, "colspan": 2, "rowspan": 2},
        {"id": "CR", "title": "Relacionamento com Clientes", "col": 6, "row": 0, "colspan": 2, "rowspan": 1},
        {"id": "CS", "title": "Segmentos de Clientes", "col": 8, "row": 0, "colspan": 2, "rowspan": 2},
        {"id": "KR", "title": "Recursos Principais", "col": 2, "row": 1, "colspan": 2, "rowspan": 1},
        {"id": "CH", "title": "Canais", "col": 6, "row": 1, "colspan": 2, "rowspan": 1},
        {"id": "C$", "title": "Estrutura de Custos", "col": 0, "row": 2, "colspan": 5, "rowspan": 1},
        {"id": "R$", "title": "Fontes de Receita", "col": 5, "row": 2, "colspan": 5, "rowspan": 1},
    ]

    comm_box_h = 130 if comentarios.strip() else 0
    grid_top = header_h + 20
    grid_w = width - 48
    grid_h = height - grid_top - (comm_box_h + 55 if comm_box_h else 45)
    col_w = grid_w / 10
    row_h = grid_h / 3

    for b in GRID_BLOCKS:
        bx = 24 + b["col"] * col_w
        by = grid_top + b["row"] * row_h
        bw = b["colspan"] * col_w
        bh = b["rowspan"] * row_h

        draw.rectangle([(bx, by), (bx + bw - 6, by + bh - 6)], fill="#F8F9F9", outline="#BDC3C7", width=2)
        draw.rectangle([(bx, by), (bx + bw - 6, by + 44)], fill="#EAECEE")
        draw.text((bx + 14, by + 10), b["title"], fill="#2C3E50", font=block_font)

        ny = by + 56
        for note in st.session_state.canvas_data[b["id"]]:
            if ny + 65 > by + bh:
                break
            draw.rectangle([(bx + 10, ny), (bx + bw - 16, ny + 56)], fill=note["color"], outline="#D5DBDB", width=1)
            display_text = note["text"] if len(note["text"]) <= 42 else note["text"][:39] + "..."
            draw.text((bx + 18, ny + 18), display_text, fill="#1C2833", font=note_font)
            ny += 64

    if comm_box_h > 0:
        cy = height - comm_box_h - 40
        draw.rectangle([(24, cy), (width - 24, cy + comm_box_h)], fill="#F2F4F4", outline="#BDC3C7", width=2)
        draw.text((36, cy + 10), "Comentários e Observações:", fill="#2C3E50", font=block_font)
        draw.text((38, cy + 45), comentarios.strip()[:200], fill="#34495E", font=sub_font)

    draw.text((26, height - 28), LEGAL_CREDIT, fill="#7F8C8D", font=legal_font)
    return img

st.divider()
st.subheader("📥 Exportação")
col_down1, col_down2 = st.columns(2)

img_pronta = gerar_canvas_img()
buf_img = io.BytesIO()
img_pronta.save(buf_img, format="PNG")
buf_img.seek(0)

with col_down1:
    st.download_button(
        label="Baixar Imagem (.png)",
        data=buf_img,
        file_name="canvas_negocios.png",
        mime="image/png",
        use_container_width=True
    )

buf_pdf = io.BytesIO()
c = pdf_canvas.Canvas(buf_pdf, pagesize=landscape(letter))
pdf_w, pdf_h = landscape(letter)
reader = ImageReader(buf_img)
c.drawImage(reader, 15, 15, width=pdf_w - 30, height=pdf_h - 30)
c.showPage()
c.save()
buf_pdf.seek(0)

with col_down2:
    st.download_button(
        label="Baixar Relatório (.pdf)",
        data=buf_pdf,
        file_name="canvas_negocios.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.caption(f"ℹ️ **Créditos e Atribuição:** {LEGAL_CREDIT}")