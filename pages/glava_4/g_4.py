import streamlit as st
import fun_g4

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 4.1':  # Золотая рыбка
            video_url = 'https://youtu.be/dbPZTjrH2mA'
        elif option == 'Листинг 4.2':  # У лукоморья
            video_url = 'https://youtu.be/M43A-xnLuSw'
        elif option == 'Листинг 4.3':  # Кузнечик
            video_url = 'https://youtu.be/IFU6Ty3so-c'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 4")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 4",
        ("Листинг 4.1", "Листинг 4.2", "Листинг 4.3",),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=700)
with cont_2:
    st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор кода ✍🏻')
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 4.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_4_1.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 4.2":  # Целые числа
        col1, col2 = st.columns([4, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_4_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 4.3":  # Целые числа
        col1, col2 = st.columns([3, 1], width=500)
        with col1:
            pass
        with col2:
            st.image('images/img_4_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_3()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)
