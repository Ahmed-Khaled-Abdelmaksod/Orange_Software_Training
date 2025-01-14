
# Observable class
class GameState:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, action):
        for observer in self.observers:
            observer.update(action)