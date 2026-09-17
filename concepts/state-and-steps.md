# State and steps

The opening program's state includes its data memory, local variables, current point of execution, and remaining budget. A write changes memory; a read observes its current contents.

The program explicitly calls `budget.step()` before each loop round and before its final write. A round performs bounded index arithmetic, one read, and one write. This is the chosen cost unit for this example; it is not a claim that a Python statement or processor instruction has that cost.

Reads and writes appear individually in the execution record. They share the number of the charged round that performed them. Budget exhaustion stops before the next round. An invalid address stops at that access; earlier writes remain visible as debugging state.

The Python interpreter runs in the browser. Interpreter work and rendering are separate from this program's declared cost model. The bounded example cannot imply that arbitrary Python functions are resource-bounded.
