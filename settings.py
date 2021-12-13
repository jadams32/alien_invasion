class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 4.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 40
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.inialize_dynamic_settings()

    def inialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
