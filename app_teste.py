import streamlit as st
from supabase import Client, create_client


st.set_page_config(
    page_title="Controle de Demandas",
    page_icon="📋",
    layout="wide",
)

STATUS = ["Pendente", "Em andamento", "Concluída"]
PRIORIDADES = ["Baixa", "Normal", "Alta", "Urgente"]


@st.cache_resource
def conectar_supabase() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"],
    )


def carregar_demandas(cliente: Client) -> list[dict]:
    resposta = (
        cliente.table("demandas_teste")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return resposta.data or []


st.title("📋 Controle de Demandas")
st.caption("Projeto de treinamento: GitHub + Supabase + Streamlit")

if "SUPABASE_URL" not in st.secrets or "SUPABASE_KEY" not in st.secrets:
    st.warning("O sistema está pronto, mas ainda falta conectar o Supabase.")
    st.code(
        'SUPABASE_URL = "https://SEU-PROJETO.supabase.co"\n'
        'SUPABASE_KEY = "SUA-CHAVE-ANON"',
        language="toml",
    )
    st.info(
        "Adicione essas duas informações nos Secrets do aplicativo no "
        "Streamlit Community Cloud. Nunca coloque a chave diretamente no GitHub."
    )
    st.stop()

try:
    supabase = conectar_supabase()
except Exception as erro:
    st.error(f"Não foi possível conectar ao Supabase: {erro}")
    st.stop()

aba_nova, aba_lista, aba_status = st.tabs(
    ["➕ Nova demanda", "📋 Demandas", "🔄 Atualizar status"]
)

with aba_nova:
    with st.form("nova_demanda", clear_on_submit=True):
        empresa = st.text_input("Empresa ou setor *")
        processo = st.text_input("Processo que precisa melhorar *")
        descricao = st.text_area("Descrição da necessidade")
        prioridade = st.selectbox("Prioridade", PRIORIDADES, index=1)
        salvar = st.form_submit_button("Salvar demanda", type="primary")

    if salvar:
        if not empresa.strip() or not processo.strip():
            st.warning("Preencha a empresa/setor e o processo.")
        else:
            try:
                supabase.table("demandas_teste").insert(
                    {
                        "empresa": empresa.strip(),
                        "processo": processo.strip(),
                        "descricao": descricao.strip(),
                        "prioridade": prioridade,
                        "status": "Pendente",
                    }
                ).execute()
                st.success("Demanda cadastrada com sucesso!")
            except Exception as erro:
                st.error(f"Erro ao cadastrar a demanda: {erro}")

with aba_lista:
    try:
        demandas = carregar_demandas(supabase)
        if not demandas:
            st.info("Nenhuma demanda cadastrada ainda.")
        else:
            col1, col2, col3 = st.columns(3)
            col1.metric("Total", len(demandas))
            col2.metric(
                "Pendentes",
                sum(item["status"] == "Pendente" for item in demandas),
            )
            col3.metric(
                "Concluídas",
                sum(item["status"] == "Concluída" for item in demandas),
            )

            st.dataframe(
                demandas,
                use_container_width=True,
                hide_index=True,
                column_order=[
                    "id",
                    "empresa",
                    "processo",
                    "descricao",
                    "prioridade",
                    "status",
                    "created_at",
                ],
                column_config={
                    "id": "Código",
                    "empresa": "Empresa/Setor",
                    "processo": "Processo",
                    "descricao": "Descrição",
                    "prioridade": "Prioridade",
                    "status": "Status",
                    "created_at": "Criada em",
                },
            )
    except Exception as erro:
        st.error(f"Erro ao consultar as demandas: {erro}")

with aba_status:
    try:
        demandas_status = carregar_demandas(supabase)
        if not demandas_status:
            st.info("Cadastre uma demanda antes de atualizar o status.")
        else:
            opcoes = {
                f"#{item['id']} — {item['empresa']} — {item['processo']}": item
                for item in demandas_status
            }
            escolha = st.selectbox("Escolha a demanda", list(opcoes))
            demanda = opcoes[escolha]
            novo_status = st.selectbox(
                "Novo status",
                STATUS,
                index=STATUS.index(demanda["status"]),
            )
            if st.button("Atualizar status", type="primary"):
                supabase.table("demandas_teste").update(
                    {"status": novo_status}
                ).eq("id", demanda["id"]).execute()
                st.success("Status atualizado!")
                st.rerun()
    except Exception as erro:
        st.error(f"Erro ao atualizar o status: {erro}")

