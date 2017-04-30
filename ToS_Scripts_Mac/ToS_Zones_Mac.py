#Takes ES Zones file from E-mini Player and convert them to script for Thinkorswim

import sys
import os


global i
i = 0
TotalCount = 0
global is_strong
is_strong = False
Error = ""


fp = open(sys.argv[1],"r")
data = fp.readlines()
fp.close()

f_out = open(os.path.expanduser("~/Desktop/ToS_Zones_Mac/es-tos.txt"), "w")
f_out.write("#Paste this text into a TOS study\n")
f_out.write("#\n")


def plot_line(level1, level2, strong, color):
    line1 = 2*i-1
    line2 = 2*i
    f_out.write("plot Line" + str(line1) + " = " + level1 + ";\n")
    f_out.write("plot Line" + str(line2) + " = " + level2 + ";\n")
    f_out.write("Line" + str(line1) + ".SetDefaultColor(Color." + color + ");\n")
    f_out.write("Line" + str(line2) + ".SetDefaultColor(Color." + color + ");\n")

    if (not strong) and (level1 != level2):
        f_out.write("Line" + str(line1) + ".hide();\n")
        f_out.write("Line" + str(line2) + ".hide();\n")

    if (level1 != level2):
        f_out.write("AddCloud(Line"+str(line1)+", Line"+str(line2)+", "
                    + "Color." + color + ", Color." + color + ");\n")

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


for line in data:
    if TotalCount >= 30:
        break


    i += 1
    str_arr = line.split(",")


    if str_arr[3] is "Strong":
        is_strong = True
    else:
        is_strong = False


    if str_arr[2] is "R":
        plot_line(str_arr[0], str_arr[1], is_strong, "RED")
        TotalCount += 1

    elif str_arr[2] is "L":
        plot_line(str_arr[0], str_arr[1], is_strong, "YELLOW")
        TotalCount += 1

    elif str_arr[2] is "S":
        plot_line(str_arr[0], str_arr[1], is_strong, "GREEN")
        TotalCount += 1

    else:
        Error += "Line " + str(i) + " Not RLS"

f_out.close()

if Error is not "":
    print Error
