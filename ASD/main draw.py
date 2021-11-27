from math import sqrt, atan2, inf
from pydraw import *

def line_length(a, b):
  dx = b[0] - a[0]
  dy = b[1] - a[1]
  return sqrt(dx**2 + dy**2)

def split_line(a, b):
  dx = b[0] - a[0]
  dy = b[1] - a[1]
  l = sqrt(dx**2 + dy**2)
  if abs(dx) < 1:
    if dy > 0:
      c = (a[0] + l/2, a[1] + l/2)
    else:
      c = (a[0] - l/2, a[1] - l/2)
  elif abs(dy) < 1:
    if dx > 0:
      c = (a[0] + l/2, a[1] - l/2)
    else:
      c = (a[0] - l/2, a[1] + l/2)
  else:
    c = (b[0], a[1]) if dx * dy > 0 else (a[0], b[1])
  return c

def dragon_curve(a, b, color, max_depth=10, depth=0):
  if depth == max_depth:
    line(a[0], a[1], b[0], b[1], color, 1)
  else:
    c = split_line(a, b)
    dragon_curve(a, c, color, max_depth, depth + 1)
    dragon_curve(b, c, color, max_depth, depth + 1)

resize(500, 500)
origin(250, 250)
clear('white')
dragon_curve((-100, 0), (150, 0), 'green', 18)