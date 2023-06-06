'''
https://dearpygui.readthedocs.io/en/latest/index.html    - источник

Основной скрипт всегда должен иметь:
create_context      - Создайте контекст 
create_viewport     - Создайте окно просмотра 
setup_dearpygui     - Настройка dearpygui 
show_viewport       - Показать окно просмотра 
start_dearpygui     - Запустите dearpygui 
destroy_context     - Очистите контекст 

Цикл рендеринга вручную должен быть создан после setup_dearpygui

Элементы создаются с помощью их команд add_***. У всех элементов должен быть тег, который может быть указан или автоматически сгенерирован DPG
Теги могут быть как целыми числами, так и строками и используются для ссылки на элемент после его создания. Элементы возвращают свой тег при их создании.
Теги элементов должны быть уникальными, если они указаны с использованием ключевого слова tag. Целые числа 0-10 зарезервированы для внутренних элементов DPG.
'''


import dearpygui.dearpygui as dpg                                           # импортировать dearpygui.dearpygui как dpg 
import dearpygui.demo as demo

dpg.create_context()                                                        # create_context - Создает контекст Dear PyGUI
dpg.create_viewport(title='Custom Title', width=600, height=300)            # create_viewport - Создает окно просмотра. 
                                                                            # title - Задает заголовок видового экрана; 
                                                                            # width - Задает ширину отображаемого пространства на видовом экране. Не включает границу.
                                                                            # height - Задает высоту отображаемого пространства на видовом экране. Не включает в себя рамку или панель декоратора.

with dpg.window(label="Example Window", pos=(200,0)):                                    # window - Создает новое окно для добавления следующих элементов. label - Переопределяет "имя" в качестве метки
 #   dpg.configure_viewport()
    dpg.add_text("Hello, world")                                            # add_text - Добавляет текст. Текст может иметь необязательную метку, которая будет отображаться справа от текста.
    dpg.add_button(label="Save")                                            # add_button - Добавляет кнопку. 
    b0 = dpg.add_button(label="button 0")
    b1 = dpg.add_button(tag=100, label="Button 1")
    dpg.add_button(tag="Btn2", label="Button 2")
    dpg.add_input_text(label="string", default_value="Quick brown fox")     # add_input_text - Добавляет ввод текста. default_value - значение по умолчанию
    dpg.add_slider_float(label="float", default_value=0.273, max_value=10)   # add_slider_float - Добавляет ползунок для одного значения с плавающей точкой. Прямой ввод можно выполнить двойным щелчком мыши или 
                                                                            # сочетанием клавиш CTRL+Click. Сами по себе Min и Max являются мягким ограничением для ползунка. 
                                                                            # Используйте ключевое слово clamped, чтобы также применить ограничения к режимам прямого ввода.
    with dpg.window(label="Window1", pos=(0,0)):
        pass

    with dpg.window(label="Window2", pos=(100,0)):
        pass
dpg.setup_dearpygui()                                                       # setup_dearpygui - помощь (настраивает) Dear PyGui
dpg.show_viewport()                                                         # show_viewport - Показывает окно просмотра
# dpg.set_primary_window("Primary Window", True)                              # set_primary_window - Устанавливает основное окно. DPG может назначить одно окно основным окном. 
                                                                            # Основное окно будет заполнять область просмотра и всегда будет отображаться за другими окнами.
                                                                            # команды, использование требуемого значения True / False позволяет установить или отменить установку окна.
# dpg.start_dearpygui()                                                       # start_dearpygui - Подготавливает окно просмотра (если это еще не сделано). настраивает, очищает и запускает основной цикл обработки событий.
                                                                            # Если необходимо запускать цикл рендеринга вручную, то start_dearpygui() не пишется, а
#  ниже заменяет, start_dearpygui()
while dpg.is_dearpygui_running():
    # вставьте сюда любой код, который вы хотели бы запустить в цикле рендеринга
    # вы можете остановить вручную, используя stop_dearpygui()
    print("это будет выполняться для каждого кадра")
    print("this will run every frame")
    dpg.render_dearpygui_frame()


dpg.destroy_context()                                                       # destroy_context - Разрушает контекст Dear PyGui

#=============================================================================
'''
# Демо
# DPG имеет полную встроенную демонстрацию / showcase. Было бы неплохо ознакомиться с этой демонстрацией. Код для этого можно найти в репозитории в `demo.py `_ файл
dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
'''