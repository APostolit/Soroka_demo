import streamlit as st
import fun_g16

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 16.1':  # Про ОПП
            video_url = 'https://youtu.be/Fy8QDIx4wVg'
        elif option == 'Листинг 16.2':  # Про ОПП2
            video_url = 'https://youtu.be/f5vLvG-P73c'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 16", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 16")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 16",
        ("Листинг 16.1", "Листинг 16.2"),
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

    elif options == "Листинг 16.1":  # Целые числа
        col1, col2 = st.columns([1.2, 0.1], width=700)
        with col1:
            pass
        with col2:
            pass
            # st.image('images/img_14_1.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g16.run_16_1()
        with st.expander("🎥 Посмотреть фильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 16.2":  # Целые числа
        col1, col2 = st.columns([1.2, 0.1], width=700)
        with col1:
            pass
        with col2:
            pass
            # st.image('images/img_14_1.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g16.run_16_2()
        with st.expander("🎥 Посмотреть фильм"):
            video = kino(options)
            st.video(data=video, width=800)
