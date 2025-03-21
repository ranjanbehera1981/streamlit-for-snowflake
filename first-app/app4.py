import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def makeTreemap(labels, parents):
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color = "lightgray"
    )
    fig = go.Figure(data)
    return fig

def makeIcircle(labels, parents):
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
    )
    fig=go.Figure(data)
    return fig

def makeSunburst(labels, parents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        insidetextorientation='horizontal'
    )
    fig = go.Figure(data)
    return fig

def makeSankey(labels, parents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(x) for x in labels],
            target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
            label=labels,
            value=list(range(1, len(labels)))
        )
    )
    fig = go.Figure(data)
    return fig

st.title("Hirarchical Data Charts")

df = pd.read_csv("data/employees.csv", header = 0).convert_dtypes()

labels, parents = df[df.columns[0]], df[df.columns[1]]

t1, t2, t3, t4 = st.tabs(["Treemap", "Icicle", "Sumburst", "Sankey"])

with t1:
    fig = makeTreemap(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

fig = makeIcircle(labels, parents)
t2.plotly_chart(fig, use_container_width=True)

with t3:
    fig = makeSunburst(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

with t4:
    fig = makeSankey(labels, parents)
    st.plotly_chart(fig, use_container_width=True)