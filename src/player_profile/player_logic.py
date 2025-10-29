class PlayerConfig:
    def __init__(self, level: int, name: str, health: int, damage: int):
        self.level = level
        self.name = name
        self.heal = health
        self.damage = damage

        self.experience = 0

        # Defect 20 in the level 1, but when you level up the limit increases by 5 points
        self.exp_new_level_required = 20

        # Global stadist
        self.total_stats_exp = 0
        self.total_stats_damage = 0
        self.total_stats_deads = 0
        self.total_stats_hours = 0

    def stats_show(self):
        print("Mis stats: ")
        print(f"Nombre: {self.name}")
        print(f"Tu nivel: {self.level}")
        print(f"Tu vida: {self.heal}")
        print(f"Tu daño: {self.damage}")
        print(f"Experiencia actual es: {self.experience}/{self.exp_new_level_required}")

    def total_stadist(self):
        print(f"Experiencia total obtenida: {self.total_stats_exp}")
        print(f"Daño total en todo tu viaje: {self.total_stats_damage}")
        print(f"Muertes totales: {self.total_stats_deads}")
        print(f"Horas totales jugadas: {self.total_stats_hours}")

    def level_up(self, exp: int):
        self.exp = exp
        self.total_stats_exp += self.exp

        while self.exp >= self.exp_new_level_required:
            self.level += 1
            self.heal += 100
            self.damage += 3
            self.exp -= self.exp_new_level_required
            self.exp_new_level_required += 5
            self.experience = self.exp

            if self.exp <= self.exp_new_level_required:
                print("Nuevo Nivel, ¡Has Mejorado!")
                self.stats_show()
                break




    def atk_basic(self):
        pass


playerOne = PlayerConfig(
    name = "Alex",
    level = 1,
    health= 100,
    damage= 5
)

# Tests functions
playerOne.stats_show()
#playerOne.level_up(20000)
playerOne.level_up(200000)
playerOne.total_stadist()
playerOne.total_stadist()
