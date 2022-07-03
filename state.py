from abc import ABC, abstractmethod

class Context:
    """Context class"""

    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.context = self

    def todraft(self):
        self._state.requestdraft()

    def tomoderation(self):
        self._state.requestmoderation()

    def topublish(self):
        self._state.requestpublished()

class State(ABC):
    """Abstract state class"""

    def context(self):
        return self._context

    def context(self, context):
        self._context = context

    @abstractmethod
    def requestdraft(self):
        pass

    @abstractmethod
    def requestmoderation(self):
        pass

    @abstractmethod
    def requestpublished(self):
        pass

class Draft(State):
    """Draft document state"""

    def requestdraft(self):
        pass

    def requestmoderation(self):
        print("Draft -> Moderation")
        self.context.transition_to(Moderation())

    def requestpublished(self):
        print("Draft -> Published")
        self.context.transition_to(Published())

class Moderation(State):
    """Moderation document state"""

    def requestdraft(self):
        print("Moderation -> Draft")
        self.context.transition_to(Draft())

    def requestmoderation(self):
        pass

    def requestpublished(self):
        print("Moderation -> Published")
        self.context.transition_to(Published())

class Published(State):
    """Published document state"""

    def requestdraft(self):
        print("Published -> Draft")
        self.context.transition_to(Draft())

    def requestmoderation(self):
        pass

    def requestpublished(self):
        pass

if __name__ == "__main__":
    """Client code"""

    context = Context(Draft())
    context.tomoderation()
    context.topublish()
    context.todraft()
    context.topublish()
    context.tomoderation()