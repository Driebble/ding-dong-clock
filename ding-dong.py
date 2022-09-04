import schedule
import time
from playsound import playsound

def job0():
    playsound('media/127107__joedeshon__grandfather-clock-chime-12.wav')
    print("Ding dong!")

def job1():
    playsound('media/127096__joedeshon__grandfather-clock-chime-01.wav')
    print("Ding dong!")

def job2():
    playsound('media/127097__joedeshon__grandfather-clock-chime-02.wav')
    print("Ding dong!")

def job3():
    playsound('media/127098__joedeshon__grandfather-clock-chime-03.wav')
    print("Ding dong!")

def job4():
    playsound('media/127099__joedeshon__grandfather-clock-chime-04.wav')
    print("Ding dong!")

def job5():
    playsound('media/127100__joedeshon__grandfather-clock-chime-05.wav')
    print("Ding dong!")

def job6():
    playsound('media/127101__joedeshon__grandfather-clock-chime-06.wav')
    print("Ding dong!")

def job7():
    playsound('media/127102__joedeshon__grandfather-clock-chime-07.wav')
    print("Ding dong!")

def job8():
    playsound('media/127103__joedeshon__grandfather-clock-chime-08.wav')
    print("Ding dong!")

def job9():
    playsound('media/127104__joedeshon__grandfather-clock-chime-09.wav')
    print("Ding dong!")

def job10():
    playsound('media/127105__joedeshon__grandfather-clock-chime-10.wav')
    print("Ding dong!")

def job11():
    playsound('media/127106__joedeshon__grandfather-clock-chime-11.wav')
    print("Ding dong!")

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