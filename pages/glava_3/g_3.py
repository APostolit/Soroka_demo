import streamlit as st
import fun_g3

@st.cache_data
def kino(option):
    try:
        video_url = None
        if option == 'Листинг 3.1':  # Учимся считать
            video_url = 'https://youtu.be/PZ1nlNkx7b4'
        elif option == 'Листинг 3.2':  # Степень числа
            video_url = 'https://youtu.be/Kz4ctua_yWQ'
        elif option == 'Листинг 3.3':  # Арифметика
            video_url = 'https://youtu.be/uHpHf3gIRzI'
        elif option == 'Листинг 3.4':  # Округление
            video_url = 'https://youtu.be/nLK6k88tqdc'
        elif option == 'Листинг 3.7':  # Про Чебурашку
            video_url = 'https://youtu.be/rdfS_eJC6T0'
        elif option == 'Листинг 3.8':  # Про лень
            video_url = 'https://youtu.be/tTWiVL6XIZg'
        elif option == 'Листинг 3.11':  # Про лень
            video_url = 'https://youtu.be/ZJToBXBNeU8'
        return video_url
    except Exception as e:
        st.error(f'Ошибка загрузки видео файла: {e}', icon="🚨")

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги темы 3")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги темы 3",
        ("Листинг 3.1", "Листинг 3.2", "Листинг 3.3", "Листинг 3.4", "Листинг 3.5",
         "Листинг 3.6", "Листинг 3.7", "Листинг 3.8", "Листинг 3.9", "Листинг 3.10",
         "Листинг 3.11",
         ),
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

    elif options == "Листинг 3.1":  # Целые числа
        col1, col2 = st.columns([2, 1], width=500)
        with col1:
            pass
        with col2:
            st.image('images/img_3_1.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_1()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 3.2":  # Вещественные числа
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_3_2.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_2()
        with st.expander("🎥 Посмотреть урок"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 3.3":  # Вещественные числа
        col1, col2 = st.columns([3, 1], width=500)
        with col1:
            pass
        with col2:
            st.image('images/img_3_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_3()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 3.4":  # Округление чисел
        col1, col2 = st.columns([3, 1], width=500)
        with col1:
            pass
        with col2:
            st.image('images/img_3_3.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_4()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 3.5":  # Округление чисел
        col1, col2 = st.columns([10, 1], width=550)
        with col1:
            pass
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_5()

    elif options == "Листинг 3.6":  # Округление чисел
        col1, col2 = st.columns([10, 1], width=500)
        with col1:
            pass
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_6()

    elif options == "Листинг 3.7":  # Про Чебурашку, сравнение
        col1, col2 = st.columns([4, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_3_4.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_7()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 3.8":  # Про лень
        col1, col2 = st.columns([6, 1], width=600)
        with col1:
            pass
        with col2:
            st.image('images/img_pyt.png')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_8()
        with st.expander("🎥 Посмотреть мультфильм"):
            video = kino(options)
            st.video(data=video, width=800)

    elif options == "Листинг 3.9":  # Про лень
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_3_5.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_9()

    elif options == "Листинг 3.10":  # Про лень
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_3_5.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_10()

    elif options == "Листинг 3.11":  # Про лень
        col1, col2 = st.columns([5, 1], width=700)
        with col1:
            pass
        with col2:
            st.image('images/img_3_6.jpg')
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_11()
        with st.expander("🎥 Посмотреть урок"):
            video = kino(options)
            st.video(data=video, width=800)