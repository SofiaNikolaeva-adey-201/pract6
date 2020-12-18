from abc import ABC, abstractmethod
class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
        }
        self.opit = opit
        self.lvl = lvl
    def opit_up(self):
        self.opit += 15
        return self.opit
    def lvl_up(self):
        stats = self.get_stats()
        self.lvl += 1
        stats['HP'] += 13
        stats['MP'] += 13
        stats['SP'] += 13
        return self.lvl, 'УРОВЕНЬ', stats
    def get_stats(self):
        return self.stats.copy()

    def can(self):
        if Ann.opit >= 20:
            print(Ann.lvl_up())
            ach.subscribe(goods)
            ach.notify('Вам положена БОЛЬШАЯ НАГРАДА!!!')
            print(goods.achievements)
        return 'МОИ ПОЗДРАВЛЕНИЯ!!!'

class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)

