import requests
import streamlit as st


st.set_page_config(
    page_title="Conexão Ecodecor",
    page_icon="🔌",
    layout="centered",
)

st.title("🔌 Teste de conexão")
st.caption("GitHub + Supabase + Streamlit")

if "SUPABASE_URL" not in st.secrets or "SUPABASE_KEY" not in st.secrets:
    st.warning("Falta configurar a URL e a chave pública do Supabase.")
    st.code(
        'SUPABASE_URL = "https://SEU-PROJETO.supabase.co"\n'
        'SUPABASE_KEY = "SUA-PUBLISHABLE-KEY"',
        language="toml",
    )
    st.info(
        "Coloque essas informações nos Secrets do Streamlit. "
        "Não envie a chave pelo GitHub nem pelo chat."
    )
    st.stop()

url = str(st.secrets["SUPABASE_URL"]).rstrip("/")
chave = str(st.secrets["SUPABASE_KEY"])

try:
    resposta = requests.get(
        f"{url}/rest/v1/",
        headers={"apikey": chave},
        timeout=15,
    )

    if resposta.ok:
        st.success("Conexão com o Supabase realizada com sucesso!")
        st.write("Nenhuma tabela foi consultada ou alterada neste teste.")
        st.write("Agora podemos criar módulos novos em tabelas separadas.")
    else:
        st.error(
            "O Supabase respondeu, mas recusou a conexão. "
            f"Código: {resposta.status_code}"
        )
except requests.RequestException as erro:
    st.error(f"Não foi possível acessar o Supabase: {erro}")

