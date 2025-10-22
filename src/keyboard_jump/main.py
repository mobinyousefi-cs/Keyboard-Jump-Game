#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: main.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Entry point for the Keyboard Jump Game. Initializes pygame, loads assets, and 
runs the main game loop.

Usage: 
python main.py [options] 

Notes: 
- Use `python -m keyboard_jump` after installing with `pip install -e .`.
- Audio init failures are handled gracefully.

===================================================================
"""
from __future__ import annotations

import sys

import pygame

from .assets import Assets
from .config import Gameplay, Screen
from .core import Game


def run() -> int:
    pygame.init()

    # Try to initialize audio; continue if not available
    try:
        pygame.mixer.init()
    except Exception:
        pass

    screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    pygame.display.set_caption(Screen.CAPTION)
    clock = pygame.time.Clock()

    assets = Assets()
    assets.load(
        font_sizes=(Gameplay.FONT_SIZE_LARGE, Gameplay.FONT_SIZE_MEDIUM, Gameplay.FONT_SIZE_SMALL)
    )

    game = Game(screen, clock, assets)
    game.run_forever()

    pygame.quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())
