#!/usr/bin/env python3.8.0

import dis
import sys

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
    instructions = dis.get_instructions(code)
    names = set()
    for instr in instructions:
        if instr.opname == "LOAD_CONST" and isinstance(instr.argval, str) and not instr.argval.startswith("__"):
            names.add(instr.argval)
    for name in sorted(names):
        print(name)
