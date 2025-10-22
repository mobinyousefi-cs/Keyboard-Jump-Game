#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: __main__.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Module execution entry point: enables `python -m keyboard_jump`.

Usage: 
python -m keyboard_jump 

Notes: 
- Delegates to keyboard_jump.run().

===================================================================
"""
from __future__ import annotations

import sys

from .main import run

if __name__ == "__main__":
    sys.exit(run())
