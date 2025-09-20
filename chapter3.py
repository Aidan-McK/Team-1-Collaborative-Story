import time
import sys

def show_delay(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def chapter_three():
    show_delay("The cursor blinked, slower now, like a heartbeat fading.")
    show_delay("Charles stared at the screen, fingers frozen, mind racing.")
    show_delay("The battery warning pulsed red...5% remaining.")
    show_delay("He typed faster, desperate to finish the final line.")
    show_delay("Outside, the storm had quieted, but inside, the tension grew.")
    show_delay("The screen flickered once more.")
    time.sleep(0.7)
    show_delay("Then, silence.")
    show_delay("The laptop shut down.")
    show_delay("But just before the darkness took over...")
    show_delay("...the story saved itself.")
    time.sleep(1)
    show_delay("Somehow.")
    show_delay("Somewhere.")
    show_delay("The final line had been written.")
    show_delay('"We were never outside."')

if __name__ == "__main__":
    chapter_three()