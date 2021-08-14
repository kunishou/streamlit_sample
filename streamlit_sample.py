import streamlit as st
from PIL import Image

st.title('Widget Sample')
#image = Image.open('sample.png')
#st.image(image,use_column_width=True)
#st.write('')

# ボタン
st.markdown('## ボタン')
st.write("st.button('ラベル')")
button = st.button('ラベル')

if button:
    st.write("ボタンが押下されました")

st.write('')

# チェックボックス
st.markdown('## チェックボックス')
st.write("st.checkbox('ラベル')")
check = st.checkbox('ラベル')

if check:
    st.write("ボックスにチェックがされました")

st.write('')

# ラジオボタン
st.markdown('## ラジオボタン')
st.write("st.radio('ラベル', ('選択肢1', '選択肢2', '選択肢3'))")
radio = st.radio("ラベル",('選択肢1', '選択肢2', '選択肢3'))
st.write(radio + 'が選択されています')
st.write('')
