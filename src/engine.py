import views

class PamagotEngine:

    def __init__(self):
        self.view = views.Room
        self.state = PamagotState()
        self.multi_mode = True
        self.pressed = bitarray(3)

    def press_btn_A(self):
        self.pressed[Buttons.A] = 1

    def press_btn_B(self):
        self.pressed[Buttons.B] = 1

    def press_btn_C(self):
        self.pressed[Buttons.C] = 1

    def update(self):
        # 1 game tick = 3 frames
        pass
        