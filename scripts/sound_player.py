import os

class SoundPlayer():
    # init class with path to audio file
    def __init__(self, path):
        self.path = path
        self.check_is_valid_path(self.path)

    # play audio file and log message
    def play_sound(self):
        print('Playing sound from:', self.path)
        os.system("afplay " + self.path)

    def play_repeated_sound(self, number_of_repeats):
        for number in range(number_of_repeats):
            if number < number_of_repeats:
                self.play_sound()

    def check_is_valid_path(self, path):
        if not os.path.exists(path):
            print("Path doesn't exist:", self.path)

if __name__ == '__main__':
    path = "/Users/raghda/code/Madniel/the-way-of-yoga/scripts/mixkit-positive-interface-beep-221.mp3"
    detector = SoundPlayer(path)
    detector.play_repeated_sound(1)
