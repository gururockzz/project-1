from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivy.clock import Clock
import speech_recognition as sr
import pyttsx3
import ctypes

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: 'Voice Command App'
            left_action_items: [["menu", lambda x: app.callback()]]
            right_action_items: [["stop", lambda x: app.stop_listening()]]
            
        MDTextField:
            id: keyword_field
            hint_text: "Enter stop word"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: 0.8
        MDRaisedButton:
            id: button
            text: 'Start Listening'
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release: app.toggle_listening()
'''

class VoiceCommandApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)
        self.listening = False
        self.keyword = ''
        return self.root

    def toggle_listening(self):
        if not self.listening:
            self.keyword = self.root.ids.keyword_field.text.lower()
            if not self.keyword:
                return
            self.listening = True
            self.root.ids.button.text = "Listening..."
            Clock.schedule_interval(self.listen, 1.5)  # Adjust the interval as needed
        else:
            self.stop_listening()

    def stop_listening(self):
        self.listening = False
        self.root.ids.button.text = "Start Listening"
        Clock.unschedule(self.listen)

    def listen(self, dt):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            engine = pyttsx3.init()
            try:
                audio = r.listen(source, timeout=1)
                text = r.recognize_google(audio)
                if text.lower() == self.keyword:
                    self.stop_music()
                    engine.say(f"{self.keyword} Someone is calling you")
                    engine.runAndWait()
            except sr.UnknownValueError:
                pass
            except sr.WaitTimeoutError:
                pass  # Continue listening
            except sr.RequestError as e:
                print("Error: {}".format(e))

    def stop_music(self):
        APPCOMMAND_MEDIA_STOP = 0xE0000
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        ctypes.windll.user32.SendMessageTimeoutW(hwnd, 0x319, 0, APPCOMMAND_MEDIA_STOP, 0, 5000, None)

    def callback(self):
        print("Menu button pressed")

    def on_stop(self):
        self.stop_listening()

if __name__ == '__main__':
    VoiceCommandApp().run()
