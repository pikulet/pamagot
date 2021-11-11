from enum import Enum

BUTTON_A = 0
BUTTON_B = 1
BUTTON_C = 2
  
class ButtonManager:
    '''
    Pyxel only has onButtonDown logic.
    This class implements the onButtonPress logic.
    '''

    Pressed = 0
    Holding = 1
    Released = 2

    def __init__(self):
        self.__buttons = [ButtonManager.Released] * 3

    def press(self, btn) -> bool:
        if self.__buttons[btn] == ButtonManager.Released:
            self.__buttons[btn] = ButtonManager.Pressed
        elif self.__buttons[btn] == ButtonManager.Pressed:
            self.__buttons[btn] = ButtonManager.Holding
    
    def release(self, btn):
        self.__buttons[btn] = ButtonManager.Released

    @property
    def pressed(self):
        return list(map(lambda b: not b, self.__buttons))