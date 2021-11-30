from enum import Enum


class GenderEnum(Enum):
    MALE = 'Male'
    FEMAIL = 'Femail'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)