#!/usr/bin/python3
import psutil


cpu = psutil.cpu_percent(interval=1)

def bar_mode():
    if cpu < 1:
        print("|_ _ _ _ _ _ _ _ _ _|")
    elif cpu > 10 and cpu <20:
        print("|# _ _ _ _ _ _ _ _ _|"+str(cpu))
    elif cpu >20 and cpu <30:
        print("|# # _ _ _ _ _ _ _ _|")
    elif cpu >30 and cpu <40:
        print("|# # # _ _ _ _ _ _ _|"+str(cpu))
    elif cpu >40 and cpu <50:
        print("|# # # # _ _ _ _ _ _|"+str(cpu))
    elif cpu >50 and cpu <60:
        print("|# # # # # _ _ _ _ _|"+str(cpu))
    elif cpu >60 and cpu < 70:
        print("|# # # # # # _ _ _ _|"+str(cpu))
    elif cpu >70 and cpu <80:
        print("|# # # # # # # _ _ _|"+str(cpu))
    elif cpu >80 and cpu <90:
        print("|# # # # # # # # _ _|"+str(cpu))
    elif cpu >90 and cpu <100:
        print("|# # # # # # # # # _|"+str(cpu))
    elif cpu == 100:
        print("|# # # # # # # # # #|"+str(cpu))


def percent_mode():
    print(cpu, end='')

percent_mode()




