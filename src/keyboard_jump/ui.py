#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: ui.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
UI drawing utilities: HUD, score, ground line, and end screen.

Usage: 
python ui.py [options] 

Notes: 
- Pygame must be initialized and fonts loaded via Assets before use.

===================================================================
"""
from __future__ import annotations

import pygame

from .config import Colors, Gameplay, Screen
from .assets import Assets


def draw_hud(surface: pygame.Surface, assets: Assets, score: int, speed: float) -> None:
    score_text = assets.font_medium.render(f"Score: {score}", True, Colors.FG)
    speed_text = assets.font_small.render(f"Speed: {int(speed)} px/s", True, Colors.FG)

    surface.blit(score_text, (16, 12))
    surface.blit(speed_text, (16, 48))


def draw_ground(surface: pygame.Surface) -> None:
    pygame.draw.line(
        surface,
        Colors.ACCENT,
        (0, Gameplay.LETTER_LIFELINE_Y),
        (Screen.WIDTH, Gameplay.LETTER_LIFELINE_Y),
        width=3,
    )


def draw_center_text(surface: pygame.Surface, assets: Assets, message: str) -> None:
    text = assets.font_large.render(message, True, Colors.FG)
    rect = text.get_rect(center=(Screen.WIDTH // 2, Screen.HEIGHT // 2))
    # drop shadow
    shadow = assets.font_large.render(message, True, Colors.SHADOW)
    surface.blit(shadow, rect.move(2, 2))
    surface.blit(text, rect)
