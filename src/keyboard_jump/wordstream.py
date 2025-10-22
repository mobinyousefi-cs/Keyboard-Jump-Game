#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: wordstream.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Random letter stream/generator utilities and simple timing helpers. Controls 
spawn cadence and provides the next target letter.

Usage: 
python wordstream.py [options] 

Notes: 
- Letters are lowercase a-z; you can extend to words if desired.
- Deterministic under an injected random.Random instance for testability.

===================================================================
"""
from __future__ import annotations

import random
import string
from dataclasses import dataclass


ALPHABET = string.ascii_lowercase


@dataclass
class SpawnController:
    interval: float
    min_interval: float
    decay: float
    time_since_spawn: float = 0.0

    def tick(self, dt: float) -> bool:
        """Advance the timer; return True when it is time to spawn a new letter."""
        self.time_since_spawn += dt
        if self.time_since_spawn >= self.interval:
            self.time_since_spawn = 0.0
            # tighten interval (faster spawns) but respect min_interval
            self.interval = max(self.min_interval, self.interval - self.decay)
            return True
        return False


class LetterRNG:
    """Random letter generator with injectable RNG for deterministic tests."""

    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()

    def next_letter(self) -> str:
        return self._rng.choice(ALPHABET)
