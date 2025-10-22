#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: test_wordstream.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Unit tests for the letter generator and spawn controller logic.

Usage: 
pytest -q 

Notes: 
- Ensures deterministic output when RNG is seeded.

===================================================================
"""
from __future__ import annotations

import random

from keyboard_jump.wordstream import ALPHABET, LetterRNG, SpawnController


def test_letter_rng_is_alpha_lowercase():
    rng = LetterRNG(random.Random(42))
    sample = [rng.next_letter() for _ in range(100)]
    assert all(ch in ALPHABET for ch in sample)


def test_spawn_controller_decays_interval_and_triggers():
    sc = SpawnController(interval=1.0, min_interval=0.5, decay=0.1)
    # 0.4 -> no spawn
    assert sc.tick(0.4) is False
    # 0.6 -> triggers, interval becomes 0.9
    assert sc.tick(0.6) is True
    assert abs(sc.interval - 0.9) < 1e-6
    # accumulate another 0.9 -> triggers again
    assert sc.tick(0.45) is False
    assert sc.tick(0.45) is True
    # interval decayed but not below min
    for _ in range(10):
        sc.tick(1.0)
    assert sc.interval >= 0.5
