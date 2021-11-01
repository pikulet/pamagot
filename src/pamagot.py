import pyxel

class Pamagot:

    def __init__(self):
        print(f"Pamagotchii :]")
        pyxel.init(80, 80, caption="Pamagotchii")
        pyxel.run(self.update, self.draw)

        self.draw_function = lambda: pyxel.cls(0)
        self.engine = None

    @property
    def draw_function(self):
        return self.draw_function

    @draw_function.setter
    def draw_function(self, fn):
        self.draw_function = fn

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
