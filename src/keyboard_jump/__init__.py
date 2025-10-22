#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Keyboard Jump Game 
File: __init__.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs) 
Created: 2025-10-22 
Updated: 2025-10-22 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Package initializer for the Keyboard Jump Game. Exposes the public API.

Usage: 
python -m keyboard_jump 

Notes: 
- Initializes package metadata.
- See README for details.

===================================================================
"""

__all__ = ["run"]

from .main import run  # re-export CLI entry point
