from engine import PamagotEngine
import pyxel

class Pamagot:

    def __init__(self):
        print("Pamagotchii :]")
        self.engine = PamagotEngine()
        pyxel.init(80, 80, caption="Pamagotchii")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.engine.press_btn_A()
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.engine.press_btn_B()
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.engine.press_btn_C()
        
        self.engine.update()

    def draw(self):
        pyxel.cls(0)
        self.engine.draw()

if __name__ == '__main__':
    Pamagot()