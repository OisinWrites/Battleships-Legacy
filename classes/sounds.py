from playsound import playsound


def play_waves():
    playsound('utils/sounds/audio/ocean.wav')


def play_missile_launch():
    playsound('utils/sounds/audio/underwater-missile.wav')


def play_missile_hit():
    playsound('utils/sounds/audio/sea-explosion.wav')


def play_missile_miss():
    playsound('utils/sounds/audio/splash.wav')


def play_ship_explosion():
    playsound('utils/sounds/audio/ship-explode.wav')


def play_ship_sink():
    playsound('utils/sounds/audio/ship-sinking.wav')
