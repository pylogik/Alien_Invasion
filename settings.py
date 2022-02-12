#!/usr/bin/python3
#Author: Cherry, Title: Settings
#Descrition: Settings for Alien Invasion stored in this file

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initilize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (115, 40, 230)
       
        #Alien settings
        self.fleet_drop_speed = 2
        
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Ship settings
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_width = 3 
        self.height = 15
        self.bullet_color = (60, 60, 60) 
        self.bullets_allowed = 3

        #How quickly the game speeds up.
        self.speedup_scale = 1.4

        #How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        #Scoring
        self.alien_points = 50

        #Fleet_direction of 1 respresents right; -1 represents left.
        self.feet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
