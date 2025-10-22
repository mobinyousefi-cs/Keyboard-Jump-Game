#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: core.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Core game loop and sprite logic for falling letters. Manages input, scoring, 
spawning, collisions with ground, and end state.

Usage: 
python core.py [options] 

Notes: 
- Designed to be imported by main.py which owns initialization concerns.

===================================================================
"""
from __future__ import annotations

import random
from dataclasses import dataclass

import pygame

from .assets import Assets
from .config import Colors, Gameplay, Screen
from .ui import draw_center_text, draw_ground, draw_hud
from .wordstream import LetterRNG, SpawnController


@dataclass
class Letter:
    char: str
    x: float
    y: float

    def rect(self, surface: pygame.Surface, font: pygame.font.Font) -> pygame.Rect:
        glyph = font.render(self.char, True, Colors.FG)
        return glyph.get_rect(center=(int(self.x), int(self.y)))


class Game:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, assets: Assets) -> None:
        self.screen = screen
        self.clock = clock
        self.assets = assets

        self.letters: list[Letter] = []
        self.speed = Gameplay.START_SPEED
        self.running = True
        self.game_over = False
        self.score = 0

        self.spawn = SpawnController(
            interval=Gameplay.SPAWN_INTERVAL,
            min_interval=Gameplay.MIN_SPAWN_INTERVAL,
            decay=0.02,
        )
        self.rng = LetterRNG(random.Random())

    def reset(self) -> None:
        self.letters.clear()
        self.speed = Gameplay.START_SPEED
        self.running = True
        self.game_over = False
        self.score = 0
        self.spawn = SpawnController(
            interval=Gameplay.SPAWN_INTERVAL,
            min_interval=Gameplay.MIN_SPAWN_INTERVAL,
            decay=0.02,
        )
        self.rng = LetterRNG(random.Random())

    def spawn_letter(self) -> None:
        margin = 40
        x = random.randint(margin, Screen.WIDTH - margin)
        y = -30
        char = self.rng.next_letter()
        self.letters.append(Letter(char, float(x), float(y)))

    def handle_key(self, key: int) -> None:
        if self.game_over:
            if key == pygame.K_ESCAPE:
                self.running = False
            else:
                self.reset()
            return

        if key == pygame.K_ESCAPE:
            self.running = False
            return

        # interpret typeable lowercase letters
        try:
            pressed = pygame.key.name(key)
        except Exception:
            pressed = ""

        if len(pressed) == 1 and pressed.isalpha():
            pressed = pressed.lower()
            if self.letters and self.letters[0].char == pressed:
                # correct
                self.score += 1
                self.assets.play_hit()
                self.letters.pop(0)
                # increase difficulty
                self.speed = min(Gameplay.MAX_SPEED, self.speed + Gameplay.SPEED_INCREMENT)
            else:
                # wrong
                self.assets.play_fail()
                self.game_over = True

    def update(self, dt: float) -> None:
        if self.game_over:
            return

        # spawn logic
        if self.spawn.tick(dt):
            self.spawn_letter()

        # move letters
        for letter in self.letters:
            letter.y += self.speed * dt

        # check ground collision -> game over
        if any(l.y >= Gameplay.LETTER_LIFELINE_Y for l in self.letters):
            self.assets.play_fail()
            self.game_over = True

    def render(self) -> None:
        self.screen.fill(Colors.BG)
        draw_ground(self.screen)

        # draw letters (front-most is index 0 for gameplay fairness)
        for i, letter in enumerate(self.letters):
            glyph = self.assets.font_large.render(letter.char, True, Colors.FG)
            rect = glyph.get_rect(center=(int(letter.x), int(letter.y)))

            # subtle depth effect
            if i == 0:
                shadow = self.assets.font_large.render(letter.char, True, Colors.SHADOW)
                self.screen.blit(shadow, rect.move(3, 3))
            self.screen.blit(glyph, rect)

        draw_hud(self.screen, self.assets, self.score, self.speed)

        if self.game_over:
            draw_center_text(self.screen, self.assets, "Game Over — press any key")

        pygame.display.flip()

    def run_forever(self) -> None:
        while self.running:
            dt_ms = self.clock.tick(Screen.FPS)
            dt = dt_ms / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

            self.update(dt)
            self.render()
