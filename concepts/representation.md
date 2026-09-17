# Representation

A representation is a finite arrangement of stored symbols with a stated meaning.

The opening uses a row of marks. Each mark is stored as `1` in a data cell. The input length specifies how many consecutive cells belong to the row, starting at its source address. Unused cells contain `0`.

For example, source address 0 and length 3 describe the marks stored at addresses 0, 1, and 2. Remaining capacity is not part of that row. Length zero represents the empty row.

This example reserves sixteen cells: eight for input and eight for output. It uses ordinary array storage rather than a packed integer encoding. The host Python representation occupies more than sixteen bytes; the [resource account](resource-bounds.md) separates those costs.
