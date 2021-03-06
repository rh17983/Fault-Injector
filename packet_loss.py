import time
import os
import sys
from random import randrange

if len(sys.argv) < 4:
    print("Expect 2 arguments: 1 - pattern type (linear, expo, random); 2 - initial loss rate (%); 3 - network interface name")
    sys.exit(1)

pattern = sys.argv[1]
rate = int(sys.argv[2])
net_interface = str(sys.argv[3])

if pattern != "linear" and pattern != "expo" and pattern != "random":
    print("The first argument should have one of the following values: linear, expo, random")
    sys.exit(1)

if rate < 0 or rate > 100:
    print("The second argument should have the value in a range between 0 and 100")
    sys.exit(1)

if pattern == "linear":
    rate_inc = 1

if pattern == "expo":
    rate_inc = 2

if pattern == "random":
    rate_inc = 2


def run_packet_loss_rate_change_command(rate, net_interface):
    command = "sudo tc qdisc change dev " + net_interface + " root netem loss " + str(rate) + "%"
    print(command)
    os.system(command)


command = "sudo tc qdisc add dev " + net_interface + " root netem loss " + str(rate) + "%"
os.system(command)

iteration = 0
while True:

    if pattern == "linear":
        rate = rate + rate_inc

    if pattern == "expo":
        rate = rate_inc ** iteration

    if pattern == "random":
        rate = rate + rate_inc * randrange(2)

    if rate > 100:
        rate = 100

    run_packet_loss_rate_change_command(rate, net_interface)

    time.sleep(60)
    iteration += 1
