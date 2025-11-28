# Uses /proc on Linux to get system CPU info
# The file '/proc/cpuinfo' provides local information about the cpu.
# You can view the complete file using 'more /proc/cpuinfo'
#
# Report selected information on the cpu
# eg. 'model name', 'cpu cores', 'cpu MHz'

file_name = '/proc/cpuinfo'

with open(file_name, "rt") as info:
    for line in info:
        if line == "\n":
            break
        elif line.startswith("model name") or line.startswith("cpu cores"):
            print(line.strip())
