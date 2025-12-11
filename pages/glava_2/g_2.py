# https://python-code-online.pages.dev/ru/
import streamlit as st
import fun_g2

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 2.2':  # Три поросенка
            video_url = 'https://youtu.be/Ua0hykvLEZ4'
        elif option == 'Листинг 2.4':  # А и Б сидели на трубе
            video_url = 'https://youtu.be/ZhVvZn6vkzc'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 2")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4",
         ),
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
    elif options == "Листинг 2.1":  # Три поросенка
        col1, col2 = st.columns([2.7,0.3], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_1()

    elif options == "Листинг 2.2":  # Три поросенка
        col1, col2 = st.columns([2.7,0.3], width=700)
        with col1:
            path = 'pages/glava_2/Listing_2_2.py'
            file = open(path, 'r')
            code = file.read()
            # st.code(code, language="python", line_numbers=True)
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 2.3":  # Три поросенка
        col1, col2 = st.columns([2.7, 0.3], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_3()

    elif options == "Листинг 2.4":  # Три поросенка
        col1, col2 = st.columns([2, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_2_4.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_4()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

