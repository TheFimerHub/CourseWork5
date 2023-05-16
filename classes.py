from dataclasses import dataclass

from skills import *


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


SmugglerClass = UnitClass(
    name='Контрабандист',
    max_health=50.0,
    max_stamina=30.0,
    attack=2.5,
    stamina=0.6,
    armor=2.0,
    skill=MegaSword()
)

ThiefClass = UnitClass(
    name='Вор',
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.5,
    skill=MegaFraud()
)

MurderClass = UnitClass(
    name='Убийца',
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=BigKnife()
)

MerchantClass = UnitClass(
    name='Пряностник',
    max_health=40.0,
    max_stamina=20.0,
    attack=0.8,
    stamina=0.8,
    armor=1.2,
    skill=LavaMoney()
)

MagClass = UnitClass(
    name='Маг',
    max_health=20.0,
    max_stamina=20.0,
    attack=3.5,
    stamina=1.0,
    armor=1.2,
    skill=AvadaKedavra()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    SmugglerClass.name: SmugglerClass,
    MurderClass.name: MurderClass,
    MerchantClass.name: MerchantClass,
    MagClass.name: MagClass
}
