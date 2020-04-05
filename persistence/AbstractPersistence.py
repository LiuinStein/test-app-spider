from abc import ABCMeta, abstractmethod


class AbstractPersistence(metaclass=ABCMeta):
    def __init__(self, conf):
        if not isinstance(conf, dict):
            raise TypeError("Unrecognizable configurations were detected during constructing Persistence")
        self.conf = conf

    @abstractmethod
    def save(self, info):
        pass
