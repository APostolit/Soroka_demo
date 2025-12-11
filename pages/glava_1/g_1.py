import streamlit as st
import fun_g1

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 1.1':  # Три поросенка
            video_url = 'https://youtu.be/exn8HjHBcvs'
        elif option == 'Листинг 1.4':  # А и Б сидели на трубе
            video_url = 'https://youtu.be/ZhVvZn6vkzc'
        elif option == 'Листинг 1.9':  # А и Б сидели на трубе
            video_url = 'https://youtu.be/Xu5wor59YHc'
        elif option == 'Листинг 1.12':  # Отступы
            video_url = 'https://youtu.be/7MwA0u5Xot4'
        elif option == 'Листинг 1.13':  # Отступы
            video_url = 'https://youtu.be/k-CMhjCsDQ8'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")


# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 1", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

st.header("👩🏻‍💻Тема 1. Знакомимся с Python 🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox(
        "🕵🏻‍♂️ Листинги темы 1",
        ("Листинг 1.1", "Листинг 1.2", "Листинг 1.3", "Листинг 1.4", "Листинг 1.5",
         "Листинг 1.6", "Листинг 1.7", "Листинг 1.8", "Листинг 1.9", "Листинг 1.10",
         "Листинг 1.11", "Листинг 1.12", "Листинг 1.13", "Листинг 1.14"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=700)

with cont:
    st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор кода ✍🏻')
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)
    elif options == "Листинг 1.1":  # Три поросенка
        col1, col2 = st.columns(2, width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 1.2":  # Три поросенка
        col1, col2 = st.columns(2, width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_2()

    elif options == "Листинг 1.3":  # Константы
        col1, col2 = st.columns(2, width=600)
        with col1:
            path = 'pages/glava_1/Listing_1_3.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_5.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_3()

    elif options == "Листинг 1.4":  # А и Б сидели на трубе
        col1, col2 = st.columns(2, width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_4.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_6.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_4()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 1.5":  # А и Б сидели на трубе
        col1, col2 = st.columns(2, width=800)
        with col1:
            path = 'pages/glava_1/Listing_1_5.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_6.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_5()

    elif options == "Листинг 1.6":  # Логические литералы
        col1, col2 = st.columns(2, width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_6.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_7.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_6()

    elif options == "Листинг 1.7":  # Пусто
        col1, col2 = st.columns(2, width=500)
        with col1:
            path = 'pages/glava_1/Listing_1_7.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_8.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_7()

    elif options == "Листинг 1.8":  # Пусто
        col1, col2 = st.columns([2,1], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_8.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_9.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_8()

    elif options == "Листинг 1.9":  # Карлсон
        col1, col2 = st.columns([2,1], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_9.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_10.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_9()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 1.10":  # Пусто
        col1, col2 = st.columns([2.2,0.8], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_10.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_11.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_10()

    elif options == "Листинг 1.11":  # Пусто
        col1, col2 = st.columns([2.2,0.8], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_11.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_13.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_11()

    elif options == "Листинг 1.12":  # Пусто
        col1, col2 = st.columns([1, 1], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_12.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_16.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_12()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 1.13":  # Пусто
        col1, col2 = st.columns([1, 1], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_13.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_16.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_13()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 1.14":  # Пусто
        col1, col2 = st.columns([1.8, 0.2], width=700)
        with col1:
            path = 'pages/glava_1/Listing_1_14.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_1_17.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g1.run_1_14()
