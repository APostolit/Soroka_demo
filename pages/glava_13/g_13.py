import streamlit as st
import fun_g13

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 13.1':  # Про репку
            video_url = 'https://youtu.be/q_Dwa5KKfLE'
        elif option == 'Листинг 13.2':  # Про козленка
            video_url = 'https://youtu.be/upja5Zu2HGA'
        elif option == 'Листинг 12.3':  # Царевна лягушка
            video_url = 'https://youtu.be/NzbXUCKxhlg'
        elif option == 'Листинг 12.4':  # Клавиатура
            video_url = 'https://youtu.be/F2HE4rPy9JI'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 13", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 13")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 13",
        ("Листинг 13.1", "Листинг 13.2", "Листинг 13.3", "Листинг 13.4",
         "Листинг 13.5",),
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

    elif options == "Листинг 13.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_13_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g13.run_13_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 13.2":  # Целые числа
        col1, col2 = st.columns([3.3, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_13_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g13.run_13_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 13.3":  # Целые числа
        col1, col2 = st.columns([3.3, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_13_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g13.run_13_3()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)

    elif options == "Листинг 13.4":  # Целые числа
        col1, col2 = st.columns([3.3, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_13_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g13.run_13_4()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)

    elif options == "Листинг 13.5":  # Целые числа
        col1, col2 = st.columns([2.8, 0.1], width=650)
        with col1:
            pass
        with col2:
            pass
            # st.image('images/img_13_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g13.run_13_5()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)
