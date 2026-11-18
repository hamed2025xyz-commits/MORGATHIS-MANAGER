# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from modules.splus_adapter import adapter_status

Window.clearcolor = (0.025, 0.027, 0.045, 1)

BG = (0.035, 0.04, 0.065, 1)
PANEL = (0.075, 0.08, 0.12, 1)
PURPLE = (0.48, 0.28, 0.95, 1)
WHITE = (0.92, 0.93, 1, 1)
MUTED = (0.58, 0.61, 0.72, 1)

class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(14), spacing=dp(8), size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter("height"))
        with self.canvas.before:
            Color(*PANEL)
            self.bg = RoundedRectangle(radius=[dp(16)])
        self.bind(pos=self._update, size=self._update)
    def _update(self, *_):
        self.bg.pos = self.pos
        self.bg.size = self.size

class MButton(Button):
    def __init__(self, **kwargs):
        super().__init__(background_normal="", background_down="", background_color=PURPLE,
                         color=WHITE, size_hint_y=None, height=dp(48), **kwargs)

class MorgathisApp(App):
    def build(self):
        self.title = "MORGATHIS MANAGER"
        outer = BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(12))
        scroll = ScrollView()
        content = BoxLayout(orientation="vertical", spacing=dp(12), size_hint_y=None)
        content.bind(minimum_height=content.setter("height"))

        header = Card()
        header.add_widget(Label(text="[b]MORGATHIS[/b]", markup=True, font_size="25sp",
                                color=WHITE, size_hint_y=None, height=dp(38)))
        header.add_widget(Label(text="MANAGER  •  SOROUSH PLUS", font_size="12sp",
                                color=PURPLE, size_hint_y=None, height=dp(24)))
        header.add_widget(Label(text="پنل مدیریت مستقل اندروید", font_size="14sp",
                                color=MUTED, size_hint_y=None, height=dp(28)))
        content.add_widget(header)

        status = Card()
        status.add_widget(Label(text="[b]وضعیت اتصال[/b]", markup=True, color=WHITE,
                                halign="right", size_hint_y=None, height=dp(28)))
        self.status_label = Label(text=adapter_status(), color=MUTED, halign="right",
                                  valign="middle", size_hint_y=None, height=dp(54))
        self.status_label.bind(size=lambda w, s: setattr(w, "text_size", s))
        status.add_widget(self.status_label)
        content.add_widget(status)

        login = Card()
        login.add_widget(Label(text="[b]اتصال حساب[/b]", markup=True, color=WHITE,
                               halign="right", size_hint_y=None, height=dp(28)))
        self.phone = TextInput(hint_text="شماره تلفن (فعلاً غیرفعال)", multiline=False,
                               size_hint_y=None, height=dp(48), background_color=BG,
                               foreground_color=WHITE, hint_text_color=MUTED, padding=dp(12))
        self.phone.disabled = True
        login.add_widget(self.phone)
        self.connect_btn = MButton(text="اتصال حساب — در انتظار تکمیل احراز هویت")
        self.connect_btn.disabled = True
        login.add_widget(self.connect_btn)
        login.add_widget(Label(text="برای امنیت، رمز و کد ورود را داخل این نسخه وارد نکن.",
                               color=MUTED, font_size="11sp", size_hint_y=None, height=dp(30)))
        content.add_widget(login)

        modules = Card()
        modules.add_widget(Label(text="[b]ماژول‌ها[/b]", markup=True, color=WHITE,
                                 halign="right", size_hint_y=None, height=dp(28)))
        for title, subtitle in [
            ("مدیریت پیام‌ها", "پاسخ خودکار و ابزارهای پیام"),
            ("مدیریت گروه‌ها", "ابزارهای مدیریتی گروه"),
            ("اتوماسیون", "وظایف زمان‌بندی‌شده"),
            ("ابزارهای متن", "قالب‌بندی و تبدیل متن"),
            ("امنیت و گزارش‌ها", "ثبت رویدادها و وضعیت"),
        ]:
            b = MButton(text=f"{title}    |    {subtitle}")
            b.disabled = True
            modules.add_widget(b)
        content.add_widget(modules)

        footer = Label(text="نسخه اولیه رابط کاربری • اتصال واقعی هنوز فعال نشده",
                       color=MUTED, font_size="10sp", size_hint_y=None, height=dp(28))
        content.add_widget(footer)
        scroll.add_widget(content)
        outer.add_widget(scroll)
        return outer

if __name__ == "__main__":
    MorgathisApp().run()
