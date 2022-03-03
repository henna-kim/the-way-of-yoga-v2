from sound_player import SoundPlayer

def play_positive_sound():
    positive_file_path = "scripts/mixkit-positive-interface-beep-221.mp3"
    player = SoundPlayer(positive_file_path)
    player.play_sound()


def play_negative_sound():
    negative_file_path = "scripts/mixkit-system-beep-buzzer-fail-2964.mp3"
    player = SoundPlayer(negative_file_path)
    player.play_repeated_sound(3)

play_positive_sound()
