# Robot Distance Sensor Simulator

**Module:** Programming for Robotics 

## Overview

Simulates a robot's front-facing distance sensor. Given a list of raw sensor readings, the program classifies each reading into a movement command and validates bad input along the way.

## Class: `Robot`

| Member | Type | Description |
|---|---|---|
| `name` | `str` | Robot identifier |
| `battery` | `int/float` | Battery level  |
| `evaluate_distances(distances)` | method | Takes a list of readings |

## Decision Logic

| Condition | Output |
|---|---|
| `distance < 0` | `INVALID (<value>)` |
| `0 <= distance < 0.5` | `STOP` |
| `0.5 <= distance <= 1.0` | `SLOW` |
| `distance > 1.0` | `MOVE FAST` |
| non-numeric / `None` | `INVALID (<value>)` |

## Error Handling

- Each reading is cast with `float(distance)` inside a `try/except (ValueError, TypeError)` block — catches strings that aren't numeric (`"ABC"`) and `None`.
- Negative values pass the cast but are explicitly flagged as `INVALID` before hitting the threshold logic, so `-0.5` doesn't silently fall into `STOP`.
- One bad reading doesn't crash the batch — each element is evaluated independently and the loop continues.

## Test Cases

| # | Input | Expected Output |
|---|---|---|
| 1 | `[0.3, 1.5, 0.8, 2.0, 0.4]` | `STOP, MOVE FAST, SLOW, MOVE FAST, STOP` |
| 2 | `[0.0, 0.5, 1.0, 1.01]` (boundaries) | `STOP, SLOW, SLOW, MOVE FAST` |
| 3 | `[-0.5, -10, 0.2]` (negative) | `INVALID (-0.5), INVALID (-10.0), STOP` |
| 4 | `["0.4", "ABC", None, 1.8]` (bad types) | `STOP, INVALID (ABC), INVALID (None), MOVE FAST` |
| 5 | `[]` (empty list) | *(empty line — no readings to evaluate)* |

## Run

```bash
python3 robot.py
```

## Review Notes

Full concept review (variables, loops, OOP basics, error handling) documented on Notion:
[ROS2 Robotics Masterclass — Python Revision](https://app.notion.com/p/ROS2-Robotics-Masterclass-Python-Revision-3c1631df44df8061a0eeecb21bb9b389?source=copy_li)
