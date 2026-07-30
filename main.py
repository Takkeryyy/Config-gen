import os
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

# Весь интерфейс зашит в строку, чтобы не плодить файлы в веб-редакторе GitHub.
# Это сильно упрощает правки с планшета.
KV_UI = '''
<ConfigEditor>:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(15)

    Label:
        text: 'GameConfigGen'
        font_size: '28sp'
        bold: True
        size_hint_y: None
        height: dp(50)
        color: (0.2, 0.6, 1, 1)

    TextInput:
        id: resolution_input
        hint_text: 'Разрешение (например, 2400x1500)'
        multiline: False
        font_size: '18sp'
        size_hint_y: None
        height: dp(50)

    TextInput:
        id: fps_input
        hint_text: 'Лимит FPS'
        multiline: False
        input_filter: 'int'
        font_size: '18sp'
        size_hint_y: None
        height: dp(50)

    Button:
        text: 'Сгенерировать конфиг'
        font_size: '20sp'
        size_hint_y: None
        height: dp(60)
        background_color: (0.1, 0.7, 0.3, 1)
        on_release: root.generate_and_save()

    Label:
        id: status_label
        text: 'Готово к работе'
        font_size: '16sp'
        text_size: self.width, None
        halign: 'center'
        valign: 'middle'
        size_hint_y: 1
'''

Builder.load_string(KV_UI)

class ConfigEditor(BoxLayout):
    def generate_and_save(self):
        app = App.get_running_app()
        
        # Получаем данные из полей
        res_val = self.ids.resolution_input.text.strip()
        fps_val = self.ids.fps_input.text.strip()

        # Базовая валидация, чтобы приложение не упало при пустых полях
        if not res_val or not fps_val:
            self.ids.status_label.text = "[color=ff3333]Ошибка: Заполните все поля[/color]"
            self.ids.status_label.markup = True
            return

        # Формируем структуру будущего конфига
        config_data = {
            "graphics": {
                "resolution": res_val,
                "target_fps": int(fps_val)
            },
            "engine_tweaks": {
                "vsync": False,
                "texture_quality": "high"
            }
        }

        # Определяем безопасный путь для сохранения. 
        # app.user_data_dir работает без root-прав и запросов разрешений на Android.
        save_dir = app.user_data_dir
        filepath = os.path.join(save_dir, 'game_config.json')

        try:
            # Безопасная запись файла
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=4, ensure_ascii=False)
            
            self.ids.status_label.text = f"[color=33ff33]Успешно![/color]\nФайл сохранен по пути:\n{filepath}"
            self.ids.status_label.markup = True
            
        except Exception as e:
            # Отлов любых ошибок ввода-вывода (I/O), чтобы приложение не крашнулось
            self.ids.status_label.text = f"[color=ff3333]Сбой при записи:[/color]\n{str(e)}"
            self.ids.status_label.markup = True

class GameConfigGenApp(App):
    def build(self):
        # Настраиваем поведение при паузе (сворачивании приложения)
        # Это важно для Android, чтобы ОС не убила процесс жестко
        self.bind(on_start=self.post_build_init)
        return ConfigEditor()

    def post_build_init(self, *args):
        pass

    def on_pause(self):
        # Сохранение состояния, если нужно, при сворачивании
        return True

    def on_resume(self):
        pass

if name == 'main':
    GameConfigGenApp().run()
