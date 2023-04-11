import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class laGrid(GridLayout):
    def __init__(self,  **kwargs):
        super(laGrid, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="nombre: "))
        self.name = TextInput(multiline=True)
        self.add_widget(self.name) 

        self.add_widget(Label(text="comida favorita: "))
        self.food = TextInput(multiline=False)
        self.add_widget(self.food)

        self.add_widget(Label(text="deporte favorito: "))
        self.sport= TextInput(multiline=False)
        self.add_widget(self.sport)

        #crea el submit
        self.submit = Button(text="enviar")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self, instance):
        name = self.name.text
        food = self.food.text
        sport = self.sport.text
        self.add_widget(Label(text=f"hola {name}, veo que te gusta comer {food}, y que tambien practicas {sport}"))

        #limpia las cosas
        self.name =''
        self.food=''
        self.sport=''


class MainApp(App):
    def build(self):
        return laGrid()

if __name__ == '__main__':
    MainApp().run()