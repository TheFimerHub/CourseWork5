from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit

class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class MegaSword(Skill):
    name = 'Мега-меч'
    stamina = 7
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"

class MegaFraud(Skill):
    name = 'Мега-кража'
    stamina = 7
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"

class BigKnife(Skill):
    name = 'Большой-нож'
    stamina = 6
    damage = 11

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"

class BigKnife(Skill):
    name = 'Большой-нож'
    stamina = 10
    damage = 14

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"

class LavaMoney(Skill):
    name = 'Лава-из-монет'
    stamina = 8
    damage = 12

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"

class AvadaKedavra(Skill):
    name = "Авада-Кедавра"
    stamina = 10
    damage = 17

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику"