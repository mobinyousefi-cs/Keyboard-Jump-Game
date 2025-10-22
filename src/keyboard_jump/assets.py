#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: assets.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Asset loading helpers for fonts and sounds. Audio is optional and failure to 
init/load gracefully degrades without crashing the game.

Usage: 
python assets.py [options] 

Notes: 
- Pygame must be initialized by the caller.
- Uses built-in font `freesansbold.ttf` available in pygame.

===================================================================
"""
from __future__ import annotations

import pygame

from .config import AssetsConfig


class Assets:
    def __init__(self) -> None:
        # Fonts
        self.font_large = None
        self.font_medium = None
        self.font_small = None

        # Sounds (optional)
        self.sfx_hit = None
        self.sfx_fail = None

    def load(self, *, font_sizes: tuple[int, int, int]) -> None:
        large, medium, small = font_sizes
        self.font_large = pygame.font.Font(AssetsConfig.FONT_FAMILY, large)
        self.font_medium = pygame.font.Font(AssetsConfig.FONT_FAMILY, medium)
        self.font_small = pygame.font.Font(AssetsConfig.FONT_FAMILY, small)

        # Audio is optional; ignore errors
        try:
            if AssetsConfig.SFX_HIT:
                self.sfx_hit = pygame.mixer.Sound(AssetsConfig.SFX_HIT)
            if AssetsConfig.SFX_FAIL:
                self.sfx_fail = pygame.mixer.Sound(AssetsConfig.SFX_FAIL)
        except Exception:
            self.sfx_hit = None
            self.sfx_fail = None

    def play_hit(self) -> None:
        if self.sfx_hit:
            try:
                self.sfx_hit.play()
            except Exception:
                pass

    def play_fail(self) -> None:
        if self.sfx_fail:
            try:
                self.sfx_fail.play()
            except Exception:
                pass
