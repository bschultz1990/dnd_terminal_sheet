class Weapon:
    def __init__(self,
                 name:str,
                 cost:float,
                 # damage:list,
                 damage:int,
                 damage_type:str,
                 weight:float,
                 properties:list
                 ) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.weight = weight
        self.properties = properties



fists = Weapon(
    name="Fists",
    cost=0,
    damage=2,
    # damage=[1,4],
    damage_type="Bludgeoning",
    weight=0,
    properties=["Unarmed"]
)


club = Weapon(
    name="Club",
    cost=0.1,
    damage=2,
    # damage=[1,4],
    damage_type="Bludgeoning",
    weight=2,
    properties=["Light"]
)


shortbow = Weapon(
    name="Shortbow",
    cost=25,
    damage=3,
    # damage=[1,6],
    damage_type="Piercing",
    weight=2,
    properties=["Ammunition", "Range: 80/320", "Loading", "Two-Handed"]
)


quarterstaff = Weapon(
    name="Quarterstaff",
    cost=0.2,
    damage=3,
    # damage=[1,6],
    damage_type="Bludgeoning",
    weight=4,
    properties=["Versatile", "1d8"]
)
