import streamlit as st
from source import get_text

st.title( "ML_task" )

text = st.text_input( "Напечатайте свой текст и нажмите кнопку Обработать" )

if (st.button( 'Обработать!' )):
    result = get_text(text.title())
    st.success(result)


