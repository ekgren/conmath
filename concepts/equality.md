# Equality

Two rows are equal when they have the same length and the same marks in corresponding positions. They may live at different memory addresses.

Equal rows need not have identical surrounding storage. Unused capacity and the location of a row are properties of its representation, not additional marks in it.

Comparing rows requires reading their contents. We have not yet introduced an equality program or its resource proof. The opening's checker compares one bounded source and target according to the [successor claim](proof-and-evidence.md).
