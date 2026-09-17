# Objects and constructions

Begin with a row of marks. We can store it, read it, and construct another row from it. We will use this small example to make three things precise: what the object is, where it lives, and what work an operation performs.

## A row and its successor

A row may contain no marks, one mark, or several marks:

<div class="notation" aria-label="one mark; two marks; three marks"><span>Ⅰ</span><span>ⅠⅠ</span><span>ⅠⅠⅠ</span></div>

Two rows are equal when they have the same marks in the same order. We write the empty row as <span class="math">ε</span>. That symbol names the empty row; it is not a mark stored inside it.

The *successor* of a row is a copy with one more mark at the end. We write the operation as <span class="math">S</span>:

<math display="block" aria-label="The successor of three marks is four marks"><mrow><mi>S</mi><mo>(</mo><mtext>ⅠⅠⅠ</mtext><mo>)</mo><mo>=</mo><mtext>ⅠⅠⅠⅠ</mtext></mrow></math>

To carry out that operation, we need to say where to read the original row and where to write the new one.

## The program

{{source:engine/successor.py}}

`source` and `target` are starting addresses. `length` says how many marks to copy. The loop reads one mark from `source + i` and writes it to `target + i`. After copying the row, the last line writes the additional mark.

For three marks, we call:

```python
successor(memory, source=0, target=8, length=3, budget=budget)
```

There are sixteen data cells in this example. Addresses 0 through 7 are reserved for the source; addresses 8 through 15 are reserved for the target. A marked cell holds `1`; a blank holds `0`. The input length tells us which source cells belong to the row. The two regions do not overlap, so writing the result leaves the input unchanged.

The displayed function is real Python and is the function the browser runs. Its three supporting operations have small, explicit contracts:

- **`memory.read(address)`** checks the address and returns the value stored there.
- **`memory.write(address, value)`** checks the address and stores the value there. It does not allocate another cell.
- **`budget.step()`** consumes one available step. With none left, it stops the computation with failure.

A charged step covers one loop round—its bounded index arithmetic, one read, and one write—or the final write. It is a unit of work we have defined for this program, not a CPU instruction or a Python statement. Here the input length is bounded by eight, so the indices and all work within a round are bounded too.

## Try it

With three input marks, the program needs four steps: three copies and one final write. Run it, then try a budget of three steps. The target will contain the copied marks, but the construction will have failed before appending the new one.

{{experiment:row}}

Now try eight input marks with nine available steps. Copying fits; the additional mark would need address 16, outside the reserved memory. That attempt fails too. More time does not create more space.

The partial target is visible so we can understand the failure. It is not returned as a successful successor. Reset prepares fresh input and blank target cells for another attempt.

## Check the result

Open the execution record to see the actual addresses read and written. The record also shows each charged step. **Check this execution** verifies that the source was preserved, the expected accesses occurred in order, and the target contains a copy followed by one additional mark.

This check concerns one completed run. It does not yet prove a general theorem about arbitrary inputs. Its rules and limits are described in [proof and evidence](../../../concepts/proof-and-evidence.md).

The sixteen cells are the program's data storage. The interpreter, indices, budget, and execution record also occupy memory; they are outside this data-cell account. We will keep those distinctions explicit rather than call sixteen cells the total cost. See [resource bounds](../../../concepts/resource-bounds.md).

## The supporting definitions

These definitions implement the memory and budget operations used above. They are available to inspect, but the construction itself remains the seven-line program.

{{source:engine/memory.py}}

## Where this leads

We have described a row, represented it in memory, and written a program that constructs its successor under stated constraints. We can inspect a successful execution and identify exactly where a failed attempt stops.

Next we will develop counting and addition. We will keep using small programs whose reads, writes, assumptions, and costs are visible.
