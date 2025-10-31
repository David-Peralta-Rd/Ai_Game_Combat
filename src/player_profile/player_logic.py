class PlayerConfig:
    def __init__(self, level: int, name: str, health: int, damage: int):
        self.level = level
        self.name = name
        self.heal = health
        self.damage = damage

        # Current exp
        self.experience = 0

        # Defect 20 in the level 1, but when you level up the limit increases by 5 points
        self.exp_new_level_required = 20

        # Global stadist
        self.total_stats_exp = 0
        self.total_stats_damage = 0
        self.total_stats_deads = 0
        self.total_stats_hours = 0


    def stats_show(self):
        print(f"\n👤 Stats de {self.name}")
        print(f"Nivel: {self.level}")
        print(f"Vida: {self.heal}")
        print(f"Daño: {self.damage}")
        print(f"Experiencia: {self.experience}/{self.exp_new_level_required}")


    def total_stadist(self):
        print(f"Experiencia total obtenida: {self.total_stats_exp}")
        print(f"Daño total en todo tu viaje: {self.total_stats_damage}")
        print(f"Muertes totales: {self.total_stats_deads}")
        print(f"Horas totales jugadas: {self.total_stats_hours}")


    def level_current(self):
        self.heal = 100 * self.level
        self.damage = 15 * self.level + 5


    def level_up(self, exp: int):
        self.exp = exp
        self.total_stats_exp += self.exp

        while self.exp >= self.exp_new_level_required:
            self.level += 1
            self.level_current()
            self.exp -= self.exp_new_level_required
            self.exp_new_level_required += 5
            self.experience = self.exp

            print(f"\n🎉 {self.name} subió al nivel {self.level}!")
            self.stats_show()


    def live_active(self):
        return self.heal > 0


    def dead_active(self):
        self.heal = 0
        print(f"☠️ {self.name} ha caído en batalla...")



class PlayerManager:
    def __init__(self):
        self.save_players = []


    def add_player(self, name: str):
        player = PlayerConfig(
            level = 1,
            name = name,
            health = 100,
            damage = 5,
            )

        self.save_players.append(player)
        print(f"✅ Jugador {player.name} creado correctamente.")
        return player

    def get_player(self, name: str):
        for p in self.save_players:
            if p.name == name:
                return p
        print("Jugador no encontrado.")
        return None

    def show_all(self):
        for search in self.save_players:
            search.stats_show()


manager = PlayerManager()
manager.add_player("sadas1")
manager.add_player("sadas12")
manager.get_player("pepe")
#manager.get_player("sadas122")
manager.show_all()

# Tests functions
#playerOne.stats_show()
