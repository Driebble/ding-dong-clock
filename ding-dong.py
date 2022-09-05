import schedule
import time
import pygame

pygame.init()
pygame.mixer.init()

vol = 0.25

def job0():
    sound = pygame.mixer.Sound("media/127107__joedeshon__grandfather-clock-chime-12.wav")
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 12 o'clock.")
    time.sleep(38)
    sound.fadeout(5000)

def job1():
    sound = pygame.mixer.Sound("media/127096__joedeshon__grandfather-clock-chime-01.wav")
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 1 o'clock.")
    time.sleep(16)
    sound.fadeout(5000)

def job2():
    sound = pygame.mixer.Sound('media/127097__joedeshon__grandfather-clock-chime-02.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 2 o'clock.")
    time.sleep(18)
    sound.fadeout(5000)

def job3():
    sound = pygame.mixer.Sound('media/127098__joedeshon__grandfather-clock-chime-03.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 3 o'clock.")
    time.sleep(20)
    sound.fadeout(5000)

def job4():
    sound = pygame.mixer.Sound('media/127099__joedeshon__grandfather-clock-chime-04.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 4 o'clock.")
    time.sleep(22)
    sound.fadeout(5000)

def job5():
    sound = pygame.mixer.Sound('media/127100__joedeshon__grandfather-clock-chime-05.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 5 o'clock.")
    time.sleep(24)
    sound.fadeout(5000)

def job6():
    sound = pygame.mixer.Sound('media/127101__joedeshon__grandfather-clock-chime-06.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 6 o'clock.")
    time.sleep(26)
    sound.fadeout(5000)

def job7():
    sound = pygame.mixer.Sound('media/127102__joedeshon__grandfather-clock-chime-07.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 7 o'clock.")
    time.sleep(28)
    sound.fadeout(5000)

def job8():
    sound = pygame.mixer.Sound('media/127103__joedeshon__grandfather-clock-chime-08.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 8 o'clock.")
    time.sleep(30)
    sound.fadeout(5000)

def job9():
    sound = pygame.mixer.Sound('media/127104__joedeshon__grandfather-clock-chime-09.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 9 o'clock.")
    time.sleep(32)
    sound.fadeout(5000)

def job10():
    sound = pygame.mixer.Sound('media/127105__joedeshon__grandfather-clock-chime-10.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 10 o'clock.")
    time.sleep(34)
    sound.fadeout(5000)

def job11():
    sound = pygame.mixer.Sound('media/127106__joedeshon__grandfather-clock-chime-11.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong! It's 11 o'clock.")
    time.sleep(36)
    sound.fadeout(5000)

schedule.every().day.at("23:59:59").do(job0)
schedule.every().day.at("00:59:59").do(job1)
schedule.every().day.at("01:59:59").do(job2)
schedule.every().day.at("02:59:59").do(job3)
schedule.every().day.at("03:59:59").do(job4)
schedule.every().day.at("04:59:59").do(job5)
schedule.every().day.at("05:59:59").do(job6)
schedule.every().day.at("06:59:59").do(job7)
schedule.every().day.at("07:59:59").do(job8)
schedule.every().day.at("08:59:59").do(job9)
schedule.every().day.at("09:59:59").do(job10)
schedule.every().day.at("10:59:59").do(job11)
schedule.every().day.at("11:59:59").do(job0)
schedule.every().day.at("12:59:59").do(job1)
schedule.every().day.at("13:59:59").do(job2)
schedule.every().day.at("14:59:59").do(job3)
schedule.every().day.at("15:59:59").do(job4)
schedule.every().day.at("16:59:59").do(job5)
schedule.every().day.at("17:59:59").do(job6)
schedule.every().day.at("18:59:59").do(job7)
schedule.every().day.at("19:59:59").do(job8)
schedule.every().day.at("20:59:59").do(job9)
schedule.every().day.at("21:59:59").do(job10)
schedule.every().day.at("22:59:59").do(job11)

while 1:
    schedule.run_pending()
    time.sleep(1)