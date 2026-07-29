from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard

class GraphicConfigApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=15, spacing=12)
        
        # Заголовок
        root.add_widget(Label(text='[b]Game Config Generator[/b]', markup=True, font_size=20, size_hint_y=None, height=35))
        
        # Масштаб разрешения
        self.res_label = Label(text='Разрешение (Scale): 75%', size_hint_y=None, height=25)
        root.add_widget(self.res_label)
        res_slider = Slider(min=50, max=100, value=75, step=5)
        res_slider.bind(value=self.on_res_change)
        root.add_widget(res_slider)
        
        # Лимит FPS
        self.fps_label = Label(text='Лимит FPS: 60', size_hint_y=None, height=25)
        root.add_widget(self.fps_label)
        fps_slider = Slider(min=30, max=120, value=60, step=30)
        fps_slider.bind(value=self.on_fps_change)
        root.add_widget(fps_slider)
        
        # Переключатель теней
        shadow_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=35)
        shadow_box.add_widget(Label(text='Включить тени (Shadows)'))
        self.shadow_switch = Switch(active=False)
        shadow_box.add_widget(self.shadow_switch)
        root.add_widget(shadow_box)
        
        # Переключатель эффектов
        pp_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=35)
        pp_box.add_widget(Label(text='Постобработка (Effects)'))
        self.pp_switch = Switch(active=False)
        pp_box.add_widget(self.pp_switch)
        root.add_widget(pp_box)
        
        # Кнопка генерации
        gen_btn = Button(text='Сгенерировать и скопировать конфиг', size_hint_y=None, height=45)
        gen_btn.bind(on_press=self.generate_config)
        root.add_widget(gen_btn)
        
        # Текстовое поле вывода
        self.output_text = TextInput(text='Здесь появится готовый конфиг...', readonly=True, size_hint_y=None, height=100)
        root.add_widget(self.output_text)
        
        return root

    def on_res_change(self, instance, value):
        self.res_label.text = f'Разрешение (Scale): {int(value)}%'

    def on_fps_change(self, instance, value):
        self.fps_label.text = f'Лимит FPS: {int(value)}'

    def generate_config(self, instance):
        res = int(self.res_label.text.split(': ')[1].replace('%', ''))
        fps = int(self.fps_label.text.split(': ')[1])
        shadows = 'True' if self.shadow_switch.active else 'False'
        effects = 'True' if self.pp_switch.active else 'False'
        
        config_data = f"""[GraphicsSettings]
ResolutionScale = {res}
TargetFPS = {fps}
ShadowsEnabled = {shadows}
PostProcessing = {effects}
TextureQuality = Optimized
AnisotropicFiltering = 2
"""
        self.output_text.text = config_data
        Clipboard.copy(config_data)

if name == 'main':
    GraphicConfigApp().run()
