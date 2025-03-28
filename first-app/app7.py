import webbrowser
import urllib
import pandas as pd
import streamlit as st

def getGraph(df):
    edges = ""
    for _, row in df.iterrows():
        if not pd.isna(row.iloc[1]):
            edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'
    return f'digraph {{\n{edges}}}'
    
st.title("Hirarchical Data Viewer")
df_orig = pd.read_csv("data/employees.csv", header = 0).convert_dtypes()
cols = list(df_orig.columns)

child = st.sidebar.selectbox("Child Column Name", cols, index=0)
parent = st.sidebar.selectbox("Parent column_name", cols, index=1)
df = df_orig[[child, parent]]

tabs = st.tabs(["Source", "Graph", "Dot Code"])

tabs[0].dataframe(df_orig)

chart = getGraph(df)    
tabs[1].graphviz_chart(chart, use_container_width=True)

url = f'https://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(chart)}'
st.link_button("visualize Online", url)
#webbrowser.open(url)
tabs[2].code(chart)