from __future__ import annotations

from abc import ABC, abstractmethod

class State(ABC):
    state: State

    def __init__(self):
        self.sub_state = None

    @staticmethod
    def switch_state(state: State):
        State.state = state

    @staticmethod
    def get_state() -> State:
        return State.state

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, win):
        pass