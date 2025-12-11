import streamlit as st
import fun_g6

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 6.1':  # Багаж
            video_url = 'https://youtu.be/Sv9WHWchy9w'
        elif option == 'Листинг 6.2':  # Колобок
            video_url = 'https://youtu.be/gfotKoDKh7M'
        elif option == 'Листинг 6.3':  # Кортеж на примере авто
            video_url = 'https://youtu.be/TWqEgTTTrsw'
        elif option == 'Листинг 6.5':  # Память компьютера
            video_url = 'https://youtu.be/q855lXL3p_I'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 6", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 6")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 6",
        ("Листинг 6.1", "Листинг 6.2", "Листинг 6.3", "Листинг 6.4",
         "Листинг 6.5"),
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

    elif options == "Листинг 6.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_6_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g6.run_6_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 6.2":  # Целые числа
        col1, col2 = st.columns([3, 1], width=770)
        with col1:
            pass
        with col2:
            st.image('images/img_6_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g6.run_6_2()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 6.3":  # Целые числа
        col1, col2 = st.columns([3, 1], width=770)
        with col1:
            pass
        with col2:
            st.image('images/img_6_4.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g6.run_6_3()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 6.4":  # Целые числа
        col1, col2 = st.columns([3, 1], width=770)
        with col1:
            pass
        with col2:
            st.image('images/img_6_4.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g6.run_6_4()
        # with st.expander("🎥 Посмотреть мультфильм"):
            # video = kino(options)
            # st.video(data=video, width=800)

    elif options == "Листинг 6.5":  # Целые числа
        col1, col2 = st.columns([3, 1], width=770)
        with col1:
            pass
        with col2:
            st.image('images/img_6_4.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g6.run_6_5()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)
