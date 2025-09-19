import time
import sys

# Lyrics with timestamps in seconds (adjust the numbers!)
lyrics = [
    (0, "Mmm, they're rottin' my brain, love"),
    (5, "These hoes are the same"),
    (10, "I admit it, another ho got me finished"),
    (15, "Broke my heart, oh, no, you didn't"),
    (20, "Fuck sippin', I'ma down a whole bottle"),
    (25, "Hard liquor, hard truth, can't swallow"),
    (30, "Need a bartender, put me out my sorrow"),
    (35, "Wake up the next day in the Monte Carlo"),
    (40, "With a new woman, tell me she from Colorado"),
    (45, "And she love women, she'll be gone by tomorrow"),
    (50, "Who am I kiddin'?"),
]

def karaoke(lyrics):
    start_time = time.time()
    for timestamp, line in lyrics:
        while time.time() - start_time < timestamp:
            time.sleep(0.05)
        sys.stdout.write(line + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    karaoke(lyrics)
