import streamlit as st
import fun_g10

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 10.1':  # Про инструкцию
            video_url = 'https://youtu.be/ET838We_UvE'
        elif option == 'Листинг 10.2':  # Про компьютерную мышь
            video_url = 'https://youtu.be/ZYTBvwV2uwc'
        elif option == 'Листинг 10.3':  # Про программиста - манипулятор
            video_url = 'https://youtu.be/0hm3QODDMv4'
        elif option == 'Листинг 10.4':  # Кто такие программисты
            video_url = 'https://youtu.be/oJMrTyvwj8Y'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 10", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 10")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 10",
        ("Листинг 10.1", "Листинг 10.2", "Листинг 10.3", "Листинг 10.4",
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор кода ✍🏻')
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 10.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_10_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g10.run_10_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 10.2":  # Целые числа
        col1, col2 = st.columns([2, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_10_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g10.run_10_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 10.3":  # Целые числа
        col1, col2 = st.columns([4.6, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_10_1.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g10.run_10_3()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 10.4":  # Целые числа
        col1, col2 = st.columns([3, 1.5], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_10_5.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g10.run_10_4()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)
