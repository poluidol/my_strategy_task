from observers.observer import Observer


class Player:
    def __init__(self):
        self.observers = []
        self.lvl = 0
        self.id = 0

    def attach_object(self, observer: Observer):

        self.observers.append(observer)

    def detach_object(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self) -> None:
        print("notified")
        for observer in self.observers:
            observer.update(self)

    def lvlup(self):
        self.lvl += 1
        self.notify()
