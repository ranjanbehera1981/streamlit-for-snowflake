import streamlit as st

st.title("Hirarchical Data Viewer")
st.header("This is a header")
st.subheader("Sub Header")
st.caption("Caption")
st.write("This is write")
st.text("Fixed Text")
st.code("v = variable()\nanother_call()", "python")
st.markdown("**bold**")
st.markdown("*bold*")
st.divider()
st.latex("...")

st.error("This is an error")
st.info("This is an info")
st.warning("This is a warning")
st.success("This is a success")

st.balloons()
st.snow()