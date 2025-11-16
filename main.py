from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class SalamAliApp(App):
    def build(self):
        # تنظیم رنگ پس‌زمینه
        Window.clearcolor = (0.2, 0.6, 0.8, 1)  # آبی روشن
        
        # ایجاد layout اصلی
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # ایجاد برچسب با متن "سلام علی"
        salam_label = Label(
            text='سلام علی!',
            font_size='40sp',
            color=(1, 1, 1, 1),  # رنگ سفید
            bold=True
        )
        
        # اضافه کردن برچسب به layout
        layout.add_widget(salam_label)
        
        return layout

if __name__ == '__main__':
    SalamAliApp().run()