import pygame
import time
import librosa
import soundfile as sf
import numpy as np
from scipy.signal import medfilt
import matplotlib.pyplot as plt

audio_file3 = "C:/Users/user/Downloads/Generative artificia (1).mp3"
audio_file4 = "C:/Users/user/Downloads/בינה מלאכותית גנרטיב.mp3"

audio_file1 = "C:/Users/user/Downloads/Between 1984 1988 Ne.mp3"
audio_file2 = "C:/Users/user/Downloads/בין 1984 1988 היה נת (1).mp3"

audio_file5 = "C:/Users/user/Downloads/Most dog owners have.mp3"
audio_file6 = "C:/Users/user/Downloads/לרוב בעלי הכלבים יש .mp3"


def func2(num):
    return num*3, num*5


def play_audio_from_time(file_path, start_time):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(start=start_time)


def play_audio(file_path):
    play_audio_from_time(file_path, 0)


def stop_audio():
    pygame.mixer.music.stop()


def play_audio_from_back_silence(file_path, pos, silence_start_en, silence_end_en, silence_start_he, silence_end_he):
    i = 0
    play_from = 0
    time_sleep = silence_start_he[i]
    if pos > silence_start_en[i]:
        while i < len(silence_start_en) - 1:
            if silence_end_en[i] < pos < silence_start_en[i + 1]:
                play_from = silence_end_he[i]
                time_sleep = silence_start_he[i + 1] - silence_end_he[i]
                break
            i += 1
    # play_audio_from_time(file_path, play_from)
    # time.sleep(time_sleep)
    # stop_audio()
    return play_from, time_sleep


def silence_times(file, hop_length):
    audio_data, sample_rate = librosa.load(file)
    print(len(audio_data))
    ind = 0
    epsilon = 0.01
    delta = sample_rate * hop_length
    silence = False
    curr_start = 0
    curr_end = 0
    silence_start = []
    silence_end = []
    j = 0
    while (ind < len(audio_data)):
        if abs(audio_data[ind]) < epsilon:
            if not silence:
                if j == 0 or silence_start[j - 1] != ind:
                    curr_start = ind
                silence = True
        else:
            if silence:
                if ind - curr_start > delta:
                    silence_start.append(curr_start / sample_rate)
                    silence_end.append(ind / sample_rate)
                    j = j + 1
                silence = False
        ind = ind + 1
    arr_start = []
    return silence_start, silence_end
    # הגדרת פרמטרים ל-VAD
    frame_length = int(0.03 * sample_rate)  # אורך מסגרת בשניות (כאן 30 מילישניות)
    hop_length = int(0.01 * sample_rate)  # צעד בין המסגרות בשניות (כאן 10 מילישניות)
    threshold = 0.0001  # סף דיוקנות לזיהוי שקט (ניתן לשנות לפי הצורך)

    # הדפסת הזמן של הרגע הראשון של שקט (בשניות)
    silence_time = silence_start / sample_rate
    print("הרגע הראשון של שקט: {:.2f} שניות".format(silence_time))


def audio_blocks(sience_start, silence_end):
    blocks = []
    blocks.append(0)
    i = 0
    while i < len(silence_end):
        blocks.append(silence_end)
    return blocks


def get_ten():
    return 10


def time_of_prev_sentence(file_en, file_he, pos):
    if pos < 0:
        return 5.3, 3.5
    else:
        arr_start_en, arr_end_en = silence_times(file_en, 0.5)
        arr_start_he, arr_end_he = silence_times(file_he, 0.5)
        return play_audio_from_back_silence(file_he, pos / 1000, silence_start_en=arr_start_en,
                                            silence_end_en=arr_end_en, silence_start_he=arr_start_he,
                                            silence_end_he=arr_end_he)


# print(time_of_prev_sentence(audio_file5, audio_file6, 4000))
# time_sleep = 0
# start_time = 0
# while True:
#     choice = int(input("אנא בחר אפשרות (1, 2, או 3): "))
#
#     if choice == 1:
#         start_time = 0
#         play_audio_from_time(audio_file1, start_time)
#     elif choice == 4:
#         print(pygame.mixer.music.get_pos())
#     elif choice == 5:
#         pos = pygame.mixer.music.get_pos()
#         stop_audio()
#         print(pos, "first\n")
#         play_audio_from_back_silence(audio_file2, start_time + pos / 1000, silence_start_en=arr_start_en,
#                                      silence_end_en=arr_end_en, silence_start_he=arr_start_he,
#                                      silence_end_he=arr_end_he)
#         print(pos, "second\n")
#         play_audio_from_time(audio_file1, start_time + pos / 1000)
#         start_time += pos / 1000
#     elif choice == 3:
#         stop_audio()
#         break
#     else:
#         print("אפשרות לא חוקית. אנא נסה שוב.")


def initialize_arrays_script(str1, str2, str3, str4, file_en, file_he):
    arr_start_en, arr_end_en = silence_times(file_en, 0.8)
    arr_start_he, arr_end_he = silence_times(file_he, 0.5)
    return ("let "+str1 + " = " + arr_start_en.__str__() + ";" + "\n" +
            "let "+str2 + " = " + arr_end_en.__str__() + ";" + "\n" +
            "let "+str3 + " = " + arr_start_he.__str__() + ";" + "\n" +
            "let "+str4 + " = " + arr_end_he.__str__() + ";")