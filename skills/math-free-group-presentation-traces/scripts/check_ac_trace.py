#!/usr/bin/env python3
"""Exact rank-two Andrews--Curtis trace replay over freely reduced words."""

from __future__ import annotations

import json
import sys
from pathlib import Path


INVERSE = {"x": "X", "X": "x", "y": "Y", "Y": "y"}


def reject(message: str) -> None:
    print(json.dumps({"status": "rejected", "reason": message}, sort_keys=True))
    raise SystemExit(2)


def reduce_word(word: str) -> str:
    if any(letter not in INVERSE for letter in word):
        raise ValueError("words may contain only x, X, y, Y")
    stack: list[str] = []
    for letter in word:
        if stack and INVERSE[letter] == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


def inverse_word(word: str) -> str:
    return "".join(INVERSE[letter] for letter in reversed(word))


def checked_index(value: object, name: str) -> int:
    if type(value) is not int or value not in (0, 1):
        raise ValueError(f"{name} must be 0 or 1")
    return value


def apply(state: tuple[str, str], move: dict[str, object]) -> tuple[str, str]:
    op = move.get("op")
    i = checked_index(move.get("i"), "i")
    words = list(state)
    if op == "invert":
        words[i] = inverse_word(words[i])
    elif op == "right_multiply":
        j = checked_index(move.get("j"), "j")
        sign = move.get("sign")
        if j == i or type(sign) is not int or sign not in (-1, 1):
            raise ValueError("right_multiply requires j != i and sign in {-1,1}")
        factor = words[j] if sign == 1 else inverse_word(words[j])
        words[i] = reduce_word(words[i] + factor)
    elif op == "conjugate":
        c = move.get("c")
        if not isinstance(c, str) or c not in INVERSE:
            raise ValueError("conjugate requires c in {x,X,y,Y}")
        words[i] = reduce_word(c + words[i] + INVERSE[c])
    else:
        raise ValueError("op must be invert, right_multiply, or conjugate")
    return tuple(reduce_word(word) for word in words)  # type: ignore[return-value]


def inverse_move(move: dict[str, object]) -> dict[str, object]:
    inverse = dict(move)
    if inverse["op"] == "right_multiply":
        inverse["sign"] = -int(inverse["sign"])
    elif inverse["op"] == "conjugate":
        inverse["c"] = INVERSE[str(inverse["c"])]
    return inverse


def pair(value: object, name: str) -> tuple[str, str]:
    if not isinstance(value, list) or len(value) != 2 or not all(isinstance(word, str) for word in value):
        raise ValueError(f"{name} must be a two-word list")
    return tuple(reduce_word(word) for word in value)  # type: ignore[arg-type,return-value]


def main(path: Path) -> None:
    try:
        payload = json.loads(path.read_text())
        start = pair(payload["start"], "start")
        target = pair(payload["target"], "target")
        moves = payload["moves"]
        if not isinstance(moves, list) or not all(isinstance(move, dict) for move in moves):
            raise ValueError("moves must be a list of objects")
        state = start
        for move in moves:
            state = apply(state, move)
        if state != target:
            reject(f"final ordered pair {state!r} differs from target {target!r}")
        for move in reversed(moves):
            state = apply(state, inverse_move(move))
        if state != start:
            reject("inverse trace did not return to the freely reduced start")
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        reject(str(exc))
    print(json.dumps({"final": list(target), "moves": len(moves), "start": list(start), "status": "certified"}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} TRACE.json")
    main(Path(sys.argv[1]))
