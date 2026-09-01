# Controle de Demandas — treinamento

Projeto simples para treinar o fluxo:

`GitHub → Supabase → Streamlit Community Cloud`

## 1. Criar a tabela no Supabase

1. Abra o projeto no Supabase.
2. Entre em **SQL Editor**.
3. Cole o conteúdo de `supabase_schema.sql`.
4. Clique em **Run**.

Use somente informações fictícias neste projeto. As políticas da tabela são
abertas para facilitar o treinamento e não servem para dados reais de clientes.

## 2. Pegar as informações de conexão

No Supabase, abra **Project Settings → API** e copie:

- Project URL
- Chave pública `anon` / `publishable`

Nunca coloque a chave `service_role` no GitHub ou no Streamlit.

## 3. Configurar o Streamlit

Nos Secrets do aplicativo, adicione:

```toml
SUPABASE_URL = "https://SEU-PROJETO.supabase.co"
SUPABASE_KEY = "SUA-CHAVE-PUBLICA"
```

Arquivo principal do aplicativo: `app_teste.py`.

## Rodar no computador

```bash
pip install -r requirements.txt
streamlit run app_teste.py
```

