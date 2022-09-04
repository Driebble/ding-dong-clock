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
    print("Ding dong!")
    time.sleep(38)
    sound.fadeout(5000)
    print("Stopped.")

def job1():
    sound = pygame.mixer.Sound("media/127096__joedeshon__grandfather-clock-chime-01.wav")
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(16)
    sound.fadeout(5000)
    print("Stopped.")

def job2():
    sound = pygame.mixer.Sound('media/127097__joedeshon__grandfather-clock-chime-02.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(18)
    sound.fadeout(5000)
    print("Stopped.")

def job3():
    sound = pygame.mixer.Sound('media/127098__joedeshon__grandfather-clock-chime-03.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(20)
    sound.fadeout(5000)
    print("Stopped.")

def job4():
    sound = pygame.mixer.Sound('media/127099__joedeshon__grandfather-clock-chime-04.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(22)
    sound.fadeout(5000)
    print("Stopped.")

def job5():
    sound = pygame.mixer.Sound('media/127100__joedeshon__grandfather-clock-chime-05.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(24)
    sound.fadeout(5000)
    print("Stopped.")

def job6():
    sound = pygame.mixer.Sound('media/127101__joedeshon__grandfather-clock-chime-06.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(26)
    sound.fadeout(5000)
    print("Stopped.")

def job7():
    sound = pygame.mixer.Sound('media/127102__joedeshon__grandfather-clock-chime-07.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(28)
    sound.fadeout(5000)
    print("Stopped.")

def job8():
    sound = pygame.mixer.Sound('media/127103__joedeshon__grandfather-clock-chime-08.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(30)
    sound.fadeout(5000)
    print("Stopped.")

def job9():
    sound = pygame.mixer.Sound('media/127104__joedeshon__grandfather-clock-chime-09.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(32)
    sound.fadeout(5000)
    print("Stopped.")

def job10():
    sound = pygame.mixer.Sound('media/127105__joedeshon__grandfather-clock-chime-10.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(34)
    sound.fadeout(5000)
    print("Stopped.")

def job11():
    sound = pygame.mixer.Sound('media/127106__joedeshon__grandfather-clock-chime-11.wav')
    sound.set_volume(vol)
    sound.play()
    print("Ding dong!")
    time.sleep(36)
    sound.fadeout(5000)
    print("Stopped.")

schedule.every().day.at("00:00").do(job0)
schedule.every().day.at("01:00").do(job1)
schedule.every().day.at("02:00").do(job2)
schedule.every().day.at("03:00").do(job3)
schedule.every().day.at("04:00").do(job4)
schedule.every().day.at("05:00").do(job5)
schedule.every().day.at("06:00").do(job6)
schedule.every().day.at("07:00").do(job7)
schedule.every().day.at("08:00").do(job8)
schedule.every().day.at("09:00").do(job9)
schedule.every().day.at("10:00").do(job10)
schedule.every().day.at("11:00").do(job11)
schedule.every().day.at("12:00").do(job0)
schedule.every().day.at("13:00").do(job1)
schedule.every().day.at("14:00").do(job2)
schedule.every().day.at("15:00").do(job3)
schedule.every().day.at("16:00").do(job4)
schedule.every().day.at("17:00").do(job5)
schedule.every().day.at("18:00").do(job6)
schedule.every().day.at("19:00").do(job7)
schedule.every().day.at("20:00").do(job8)
schedule.every().day.at("21:00").do(job9)
schedule.every().day.at("22:00").do(job10)
schedule.every().day.at("23:00").do(job11)

while 1:
    schedule.run_pending()
    time.sleep(1)