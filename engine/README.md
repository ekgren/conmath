# Mathematical engine

[successor.py](successor.py) is the displayed seven-line construction.
[memory.py](memory.py) defines checked reads, writes, and the finite budget.
[evidence.py](evidence.py) independently checks an individual execution record.
It is not a general theorem prover.

The [model specification](../docs/design/row-machine.md) states the cost accounts,
exclusions, and trusted rules. Python runs through locally bundled Pyodide in a
browser worker. The engine has no DOM, network, clock, or storage dependencies.
