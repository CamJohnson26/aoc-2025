# Part 1: 21 mins
# Part 2: 19 mins

lines = []
with open('inputs/day-7.txt', 'r') as f:
    lines = f.readlines()

def get_next_beam(prev_line, cur_line, history=None):
    new_beams = []
    for i, prev_char in enumerate(prev_line):
        if prev_char == 'S' or prev_char == '|':
            parents_count = 1
            if history is not None:
                parents_count = history[i]
            new_beams.append((i, parents_count))
    new_line = list(cur_line.strip())
    history = [0] * len(new_line)
    split_count = 0
    for (beam_index, parents_count) in new_beams:
        if new_line[beam_index] == '^':
            split_count += 1
            if beam_index - 1 >= 0:
                new_line[beam_index - 1] = '|'
                history[beam_index - 1] = history[beam_index - 1] + parents_count
            if beam_index + 1 < len(new_line):
                new_line[beam_index + 1] = '|'
                history[beam_index + 1] = history[beam_index + 1] + parents_count
        else:
            new_line[beam_index] = '|'
            history[beam_index] = history[beam_index] + parents_count
    return "".join(new_line), split_count, history

parsed_input = []
prev_line = None
prev_history = None
total_splits = 0
for line in lines:
    if prev_line is not None:
        prev_line, splits, prev_history = get_next_beam(prev_line, line, prev_history)
        parsed_input.append(prev_line)
        total_splits += splits
        print(prev_line)
        print("".join([str(s) for s in prev_history]))
    else:
        prev_line = line

for line in parsed_input:
    print(line)
print(total_splits)
print(sum(prev_history))