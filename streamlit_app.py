import streamlit as st

st.write("""
# Hello

Hello everyone
""")

st.latex(r''' e^{i\pi} + 1 = 0 ''')


tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")


