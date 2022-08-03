import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components

#sidebar (mess up)
if st.sidebar.button("สารบัญ sidebar"):
    st.sidebar.button("บทนำ แนวทางประชาธิปไตยที่เหมาะสมในทัศนะผู้เขียน")
    st.sidebar.button("บทที่ 1 ประชาธิปไตยในบริบทสากล")
    st.sidebar.button("1.1 ประชาธิปไตย คืออะไร")
    st.sidebar.button("1.2 รูปแบบการปรองระบอบประชาธิปไตย")
    st.sidebar.button("1.2.1 ประชาธิปไตยทางตรง (Direct Democracy)")
    st.sidebar.button("1.2.2 ประชาธิปไตยแบบมีผู้แทน (Representative Democracy)")
    st.sidebar.button("บทที่ 2 ประชาธิปไตยในประเทศไทย")
    st.sidebar.button("2.1 รูปแบบการปรองระบอบประชาธิปไตย ")
    st.sidebar.button("2.1.1 คิดว่าประชาธิปไตยคือการเลือกตั้ง")
    st.sidebar.button("2.1.2 คิดว่ารัฐธรรมนูญดีจะทำให้เกิดประชาธิปไตยที่เข็มแข็ง")
    
#pop up (can't scroll down)
open_modal1 = st.sidebar.button("สารบัญ pop up")
if open_modal1:
    modal.open()

if modal.is_open():
    with modal.container():
        st.header("สารบัญ")
        st.subheader("บทนำ แนวทางประชาธิปไตยที่เหมาะสมในทัศนะผู้เขียน")
        st.write("บทที่ 1 ประชาธิปไตยในบริบทสากล")
        st.caption("1.1 ประชาธิปไตย คืออะไร")
        st.caption("1.2 รูปแบบการปรองระบอบประชาธิปไตย")
        st.caption("1.2.1 ประชาธิปไตยทางตรง (Direct Democracy)")
        st.caption("1.2.2 ประชาธิปไตยแบบมีผู้แทน (Representative Democracy)")
        st.write("บทที่ 2 ประชาธิปไตยในประเทศไทย")
        st.caption("2.1 รูปแบบการปกครองระบอบประชาธิปไตย ")
        st.caption("2.1.1 คิดว่าประชาธิปไตยคือการเลือกตั้ง")
        st.caption("2.1.2 คิดว่ารัฐธรรมนูญดีจะทำให้เกิดประชาธิปไตยที่เข็มแข็ง")

