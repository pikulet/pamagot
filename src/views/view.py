from abc import abstractmethod

class View:
        
    @abstractmethod
    def draw(self, state):
        pass

    @abstractmethod
    def press_btn_A(self, state):
        pass

    @abstractmethod
    def press_btn_B(self, state):
        pass

    @abstractmethod
    def press_btn_C(self, state):
        pass

class MultiView(View):

    @abstractmethod
    def press_btn_AB(self, state):
        pass

    @abstractmethod
    def press_btn_AC(self, state):
        pass

    @abstractmethod
    def press_btn_BC(self, state):
        pass