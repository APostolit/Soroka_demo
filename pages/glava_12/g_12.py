import streamlit as st
import fun_g12

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 12.2':  # Про светофор
            video_url = 'https://youtu.be/1nRWGpv1JIA'
        elif option == 'Листинг 12.2':  # Про светофор
            video_url = 'https://youtu.be/TUodzCtBSWU'
        elif option == 'Листинг 12.3':  # Царевна лягушка
            video_url = 'https://youtu.be/NzbXUCKxhlg'
        elif option == 'Листинг 12.4':  # Клавиатура
            video_url = 'https://youtu.be/F2HE4rPy9JI'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 12", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 12")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 12",
        ("Листинг 12.1", "Листинг 12.2", "Листинг 12.3", "Листинг 12.4",
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

    elif options == "Листинг 12.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_12_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g12.run_12_1()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)

    elif options == "Листинг 12.2":  # Целые числа
        col1, col2 = st.columns([2, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_12_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g12.run_12_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 12.3":  # Целые числа
        col1, col2 = st.columns([2, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_12_4.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g12.run_12_3()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 12.4":  # Целые числа
        col1, col2 = st.columns([8, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g12.run_12_4()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)
