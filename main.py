from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AddNumbersApp(App):
    def build(self):
        self.title = 'Add Numbers App'
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.num1_input = TextInput(hint_text='Enter number 1', multiline=False)
        self.num2_input = TextInput(hint_text='Enter number 2', multiline=False)
        self.add_button = Button(text='Add Numbers')
        self.result_label = Label(text='Result will appear here')

        self.add_button.bind(on_press=self.calculate_sum)

        self.layout.add_widget(self.num1_input)
        self.layout.add_widget(self.num2_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_sum(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            result = num1 + num2
            self.result_label.text = f'Result: {result}'
        except ValueError:
            self.result_label.text = 'Invalid input'

if __name__ == '__main__':
    AddNumbersApp().run()
