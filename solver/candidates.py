from solver.candidate import Candidate


def candidates(size: int):
    if size % 2 == 1:
        raise ValueError("size must be even")
    candidates: list[Candidate] = []
    for seed in range(2**size):
        candidate = Candidate(seed, size)
        if not candidate.valid():
            continue
        candidates.append(candidate)
    return candidates
