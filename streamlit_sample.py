import streamlit as st
from PIL import Image

#st.title('Widget Sample')
image = Image.open('sample.png')
st.image(image,use_column_width=True)
st.write('')

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

# 選択肢
st.markdown('## 選択肢')
st.write("st.selectbox('ラベル',('選択肢1', '選択肢2', '選択肢3'))")
select = st.selectbox('ラベル',('選択肢1', '選択肢2', '選択肢3'))
st.write(select + 'が選択されています')
st.write('')

# 複数選択
st.markdown('## 複数選択肢')
st.write("st.multiselect('ラベル', ['選択肢1', '選択肢2', '選択肢3'],['選択肢1'])")
multiselect = st.multiselect('ラベル', ['選択肢1', '選択肢2', '選択肢3'],['選択肢1'])
st.write('・'.join(multiselect) + 'が選択されています')
st.write('')

# スライダー
st.markdown('## スライダー')
st.write("st.slider('音量', 0, 100, 50, 5)")
slider = st.slider('音量', 0, 100, 50, 5)
st.write('音量は' + str(slider) + 'です')
st.write('')

# テキスト入力
st.markdown('## テキスト入力')
st.write("st.text_input('ラベル', '')")
text = st.text_input('ラベル', '')
st.write('「' + text + '」という文字列が入力されています')
st.write('')

# 数値入力
st.markdown('## 数値入力')
st.write("st.number_input('ラベル', 0, 100, 0)")
number = st.number_input('ラベル', 0, 100, 0)
st.write('数値は' + str(number) + 'です')
st.write('')

# ファイルアップロード
#st.markdown('## ファイルアップロード')
#st.write("st.file_uploader('ラベル', type='csv') ")
#st.file_uploader("ラベル", type='csv') 
