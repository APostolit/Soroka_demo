import streamlit as st
import fun_g5

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 5.1':  # Козленок до десяти
            video_url = 'https://youtu.be/upja5Zu2HGA'
        elif option == 'Листинг 5.2':  # Про память и гаджеты
            video_url = 'https://youtu.be/K71MTOmmyTk'
        elif option == 'Листинг 5.4':  # Список
            video_url = 'https://youtu.be/mMla3pPoszA'
        elif option == 'Листинг 5.5':  # Список
            video_url = 'https://youtu.be/h56nD886kdU'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 5", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 5")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 5",
        ("Листинг 5.1", "Листинг 5.2", "Листинг 5.3", "Листинг 5.4",
         "Листинг 5.5", ),
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

    elif options == "Листинг 5.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_5_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 5.2":  # Целые числа
        col1, col2 = st.columns([5, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_5_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 5.3":  # Целые числа
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_5_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_3()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)

    elif options == "Листинг 5.4":  # Целые числа
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_5_6.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_4()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 5.5":  # Целые числа
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_5_7.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_5()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)
