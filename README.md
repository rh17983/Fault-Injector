# Fault-Injector
## Quick Start
1. Install the packages: pipenv install
2. Run the environment: pipenv shell

#### Notes:
1. The scrips must be run locally on the target machine
2. See package requirements in the Pipfile (python 2.7 required!)

## 1. CPU Hog fault injection

#### ToDo:
Run: python cpu_hog.py fault-injection-intensity-pattern fault-injection-interval

where:<br>
1. fault-injection-intensity-pattern is a string indicating one of the following injection intensity patterns: {linear, expo, random}
2. fault-injection-interval is a positive integer indicating the time period (in seconds) between the sequential injections

#### Examples:
* Linear pattern: python cpu_hog.py linear 60
* Exponential pattern: python cpu_hog.py expo 60
* Random pattern: python cpu_hog.py random 10


## 2. Packet Loss fault injection
#### ToDo:

Run: python packet_loss.py fault-injection-intensity-pattern initial-loss-rate network-interface

where:<br>
1. fault-injection-intensity-pattern is a string indicating one of the following injection intensity patterns: {linear, expo, random}
2. initial-loss-rate is an integer in the range [0 - 99] indicating the initial loss rate (%)
3. network-interface is a logical name of the target network interface (use "sudo lshw -C network" command to get the info needed)

#### Examples:
* Linear pattern: python packet_loss.py linear 25 ens3
* Exponential pattern: python packet_loss.py expo 2 ens3
* Random pattern: python packet_loss.py random 0 ens3


## 3. Memory Leak fault injection
#### ToDo:
1. Copy to the target machine and compile the code files of the corresponding fault injection patterns:
    * Linear pattern: gcc -o memleaknormal memleaknormal.c
    * Exponential pattern: gcc -o memleakexpo memleakexpo.c
    * Random pattern: gcc -o memleakrandom memleakrandom.c
2. Run the corresponding program:
    * Linear pattern: ./memleaknormal
    * Exponential pattern: ./memleakexpo
    * Random pattern: ./memleakrandom