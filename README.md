# Conexão Supabase — treinamento

Projeto simples para treinar o fluxo sem modificar a tabela real `demandas`:

`GitHub → Supabase → Streamlit Community Cloud`

## 1. Pegar as informações de conexão

No Supabase, abra **Project Settings → API** e copie:

- Project URL
- Chave pública `anon` / `publishable`

Nunca coloque a chave `service_role` no GitHub ou no Streamlit.

## 2. Configurar o Streamlit

Nos Secrets do aplicativo, adicione:

```toml
SUPABASE_URL = "https://SEU-PROJETO.supabase.co"
SUPABASE_KEY = "SUA-CHAVE-PUBLICA"
```

Arquivo principal do aplicativo: `app_teste.py`.

O teste acessa somente a raiz do Data API. Nenhuma tabela é consultada,
inserida, atualizada ou removida.

## Rodar no computador

```bash
pip install -r requirements.txt
streamlit run app_teste.py
```
