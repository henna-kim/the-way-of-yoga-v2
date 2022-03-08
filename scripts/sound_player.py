import os

class SoundPlayer():
    # init class with path to audio file
    def __init__(self, path):
        self.path = path
        self.check_is_valid_path(self.path)

    # play audio file and log message
    def play_sound(self):
        print('Playing sound from:', self.path)
        os.system(self.path)

    def play_repeated_sound(self, number_of_repeats):
        for number in range(number_of_repeats):
            if number < number_of_repeats:
                self.play_sound()

    def check_is_valid_path(self, path):
        if not os.path.exists(path):
            print("Path doesn't exist:", self.path)

    def play_positive_sound(self):
        positive_file_path = "mixkit-positive-interface-beep-221.mp3"
        player = SoundPlayer(positive_file_path)
        player.play_sound()


    def play_negative_sound(self):
        negative_file_path = "mixkit-system-beep-buzzer-fail-2964.mp3"
        player = SoundPlayer(negative_file_path)
        player.play_repeated_sound(3)

if __name__ == '__main__':
    path = "mixkit-positive-interface-beep-221.mp3"
    detector = SoundPlayer(path)
    detector.play_repeated_sound(1)
