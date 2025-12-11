import streamlit as st
import fun_g7

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 7.1':  # Про клад
            video_url = 'https://youtu.be/Q2OEpFS9haU'
        elif option == 'Листинг 7.2':  # Город изумрудный - песня
            video_url = 'https://youtu.be/G8S41JQPUCQ'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 7", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 7")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 7",
        ("Листинг 7.1", "Листинг 7.2", "Листинг 7.3",
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

    elif options == "Листинг 7.1":  # Целые числа
        col1, col2 = st.columns([3, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_7_1.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g7.run_7_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 7.2":  # Целые числа
        col1, col2 = st.columns([3, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_7_0.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g7.run_7_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 7.3":  # Целые числа
        col1, col2 = st.columns([3, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_7_0.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g7.run_7_3()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)

