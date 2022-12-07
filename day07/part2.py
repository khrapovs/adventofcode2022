with open("data.txt", mode="r") as f:
    signals = f.read().split("\n")

MARKER_LEN = 14


def detect_marker(signal: str) -> int:
    nunique, pos = 0, 0
    while (pos + MARKER_LEN <= len(signal)) and (nunique < MARKER_LEN):
        nunique = len(set(signal[pos : pos + MARKER_LEN]))
        pos += 1
    return pos + MARKER_LEN - 1


def detect_marker2(signal: str) -> int:
    for pos in range(len(signal) - MARKER_LEN):
        marker = signal[pos : pos + MARKER_LEN]
        if len(set(marker)) == MARKER_LEN:
            return pos + MARKER_LEN
        else:
            continue


answer = [detect_marker(signal) for signal in signals]

print(answer)
