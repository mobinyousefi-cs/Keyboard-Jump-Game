#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: config.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Centralized configuration and constants for the game including colors, screen 
dimensions, speeds, and gameplay tuning parameters.

Usage: 
python config.py [options] 

Notes: 
- This module contains no side effects and can be safely imported in tests.

===================================================================
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    BG = (16, 18, 22)
    FG = (245, 245, 245)
    ACCENT = (120, 190, 255)
    DANGER = (255, 105, 97)
    SHADOW = (0, 0, 0)


@dataclass(frozen=True)
class Screen:
    WIDTH: int = 960
    HEIGHT: int = 540
    CAPTION: str = "Keyboard Jump — Type Fast!"
    FPS: int = 60


@dataclass(frozen=True)
class Gameplay:
    START_SPEED: float = 120.0  # px/sec downward movement
    MAX_SPEED: float = 600.0
    SPEED_INCREMENT: float = 4.0  # added each correct key
    SPAWN_INTERVAL: float = 1.2  # seconds between new letters at start
    MIN_SPAWN_INTERVAL: float = 0.35
    FONT_SIZE_LARGE: int = 64
    FONT_SIZE_MEDIUM: int = 28
    FONT_SIZE_SMALL: int = 20
    GRAVITY: float = 0.0  # no acceleration; constant speed feels fair
    LETTER_LIFELINE_Y: int = Screen.HEIGHT - 88  # ground line threshold


@dataclass(frozen=True)
class AssetsConfig:
    FONT_FAMILY: str = "freesansbold.ttf"  # bundled with pygame
    SFX_HIT: str | None = None
    SFX_FAIL: str | None = None
