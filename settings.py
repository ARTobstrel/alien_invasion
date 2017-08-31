class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (130, 130, 130)

        # Настройки корабля.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Параметры пули.
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 - движение вправо, -1 - движение влево.
        self.add_speed = 1 # фактор увеличения скорости нового флота пришельцев
