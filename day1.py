data = open("input2.txt").read()
totals = [sum([int(c) for c in elf.split("\n")]) for elf in data.strip().split("\n\n")]
print(f"Part 1: {max(totals)}")
print(f"Part 2: {sum(sorted(totals, reverse=True)[:3])}")
