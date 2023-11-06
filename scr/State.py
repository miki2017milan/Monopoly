from abc import ABC, abstractmethod

class State(ABC):
    state = None

    @staticmethod
    def switch_state(state):
        State.state = state

    @staticmethod
    def get_state():
        return State.state

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, win):
        pass