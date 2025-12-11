#  pip install -r requirements.txt
import streamlit as st

# Сделать доступной всю ширину страницы
st.set_page_config(layout="wide")
st.set_page_config(initial_sidebar_state="collapsed")

# Иконка приложения
with st.sidebar:
    st.logo(image='favicon.ico', icon_image='favicon.ico', size="large")

# Глава 1
g_1 = st.Page(page="pages/glava_1/g_1.py", title="📕Листинги темы 1")
# Глава 2
g_2 = st.Page(page="pages/glava_2/g_2.py", title="📕Листинги темы 2")
# Глава 3
g_3 = st.Page(page="pages/glava_3/g_3.py", title="📕Листинги темы 3")
# Глава 4
g_4 = st.Page(page="pages/glava_4/g_4.py", title="📕Листинги темы 4")
# Глава 5
g_5 = st.Page(page="pages/glava_5/g_5.py", title="📕Листинги темы 5")
# Глава 6
g_6 = st.Page(page="pages/glava_6/g_6.py", title="📕Листинги темы 6")
# Глава 7
g_7 = st.Page(page="pages/glava_7/g_7.py", title="📕Листинги темы 7")
# Глава 8
g_8 = st.Page(page="pages/glava_8/g_8.py", title="📕Листинги темы 8")
# Глава 9
g_9 = st.Page(page="pages/glava_9/g_9.py", title="📕Листинги темы 9")
# Глава 10
g_10 = st.Page(page="pages/glava_10/g_10.py", title="📕Листинги темы 10")
# Глава 11
g_11 = st.Page(page="pages/glava_11/g_11.py", title="📕Листинги темы 11")
# Глава 12
g_12 = st.Page(page="pages/glava_12/g_12.py", title="📕Листинги темы 12")
# Глава 13
g_13 = st.Page(page="pages/glava_13/g_13.py", title="📕Листинги темы 13")
# Глава 14
g_14 = st.Page(page="pages/glava_14/g_14.py", title="📕Листинги темы 14")
# Глава 15
g_15 = st.Page(page="pages/glava_15/g_15.py", title="📕Листинги темы 15")
# Глава 16
g_16 = st.Page(page="pages/glava_16/g_16.py", title="📕Листинги темы 16")

# Создание навигатора страниц (главное меню)
pages = {
    "Тема 1": [g_1], "Тема 2": [g_2], "Тема 3": [g_3], "Тема 4": [g_4],
    "Тема 5": [g_5], "Тема 6": [g_6], "Тема 7": [g_7], "Тема 8": [g_8],
    "Тема 9": [g_9], "Тема 10": [g_10], "Тема 11": [g_11], "Тема 12": [g_12],
    "Тема 13": [g_13], "Тема 14": [g_14], "Тема 15": [g_15], "Тема 16": [g_16],}
pg = st.navigation(pages=pages, position="top", expanded=False)

# Запуск навигатора страниц
pg.run()