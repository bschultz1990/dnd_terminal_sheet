from character import Character

hero = Character(name="Shinsu", health=100)
enemy = Character(name="Zorbog the Terrible", health=100)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()
