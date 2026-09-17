def successor(memory, source, target, length, budget):
    for i in range(length):
        budget.step()
        mark = memory.read(source + i)
        memory.write(target + i, mark)
    budget.step()
    memory.write(target + length, 1)
