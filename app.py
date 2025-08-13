import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais usando os filtros à esquerda.")

# --- Carregamento dos dados (cacheado) ---
@st.cache_data(show_spinner=True)
def load_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url)

DATA_URL = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
df = load_data(DATA_URL)

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")
anos_sel = st.sidebar.multiselect("Ano", sorted(df['ano'].dropna().unique()), default=sorted(df['ano'].dropna().unique()))
sen_sel  = st.sidebar.multiselect("Senioridade", sorted(df['senioridade'].dropna().unique()), default=sorted(df['senioridade'].dropna().unique()))
ctr_sel  = st.sidebar.multiselect("Tipo de Contrato", sorted(df['contrato'].dropna().unique()), default=sorted(df['contrato'].dropna().unique()))
tam_sel  = st.sidebar.multiselect("Tamanho da Empresa", sorted(df['tamanho_empresa'].dropna().unique()), default=sorted(df['tamanho_empresa'].dropna().unique()))

mask = (
    df['ano'].isin(anos_sel) &
    df['senioridade'].isin(sen_sel) &
    df['contrato'].isin(ctr_sel) &
    df['tamanho_empresa'].isin(tam_sel)
)
df_filtrado = df.loc[mask].copy()

# --- KPIs ---
st.subheader("Métricas gerais (Salário anual em USD)")
if not df_filtrado.empty:
    salario_medio = float(df_filtrado['usd'].mean())
    salario_maximo = float(df_filtrado['usd'].max())
    total_registros = int(df_filtrado.shape[0])
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
    salario_medio = salario_maximo = 0.0
    total_registros = 0
    cargo_mais_frequente = "—"

c1, c2, c3, c4 = st.columns(4)
c1.metric("Salário médio", f"${salario_medio:,.0f}")
c2.metric("Salário máximo", f"${salario_maximo:,.0f}")
c3.metric("Total de registros", f"{total_registros:,}")
c4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# --- Gráficos ---
st.subheader("Gráficos")
g1, g2 = st.columns(2)

with g1:
    if not df_filtrado.empty:
        top_cargos = (
            df_filtrado.groupby('cargo', as_index=False)['usd']
            .mean()
            .nlargest(10, 'usd')
            .sort_values('usd', ascending=True)
        )
        fig = px.bar(
            top_cargos, x='usd', y='cargo', orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
        )
        fig.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with g2:
    if not df_filtrado.empty:
        fig = px.histogram(
            df_filtrado, x='usd', nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': 'Contagem'}
        )
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

g3, g4 = st.columns(2)

with g3:
    if not df_filtrado.empty and 'remoto' in df_filtrado.columns:
        remoto = df_filtrado['remoto'].value_counts(dropna=False).reset_index()
        remoto.columns = ['tipo_trabalho', 'quantidade']
        fig = px.pie(
            remoto, names='tipo_trabalho', values='quantidade',
            title='Proporção dos tipos de trabalho', hole=0.5
        )
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with g4:
    if not df_filtrado.empty and 'residencia_iso3' in df_filtrado.columns:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3', as_index=False)['usd'].mean()
            fig = px.choropleth(
                media_ds_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale='RdYlGn',  # atenção ao case
                title='Salário médio de Cientista de Dados por país',
                labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
            )
            fig.update_layout(title_x=0.1)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Sem registros de 'Data Scientist' no recorte atual.")
    else:
        st.warning("Nenhum dado para exibir no mapa por país.")

# --- Tabela e download ---
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado, use_container_width=True)
st.sidebar.download_button(
    "Baixar CSV filtrado",
    df_filtrado.to_csv(index=False).encode("utf-8"),
    file_name="dados_filtrados.csv",
    mime="text/csv",
)
