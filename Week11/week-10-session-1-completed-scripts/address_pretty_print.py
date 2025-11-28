import sys

# usage: python address_pretty_print.py <input.txt> <output.txt>
# eg. python address_pretty_print.py addresses.txt out.txt
# addresses.txt is in the testdir/ folder

filename = sys.argv[1]
outfile = sys.argv[2]

# read in the address data (see addresses.txt for the format)
# process each line into a well formatted address, such as you could use on a label
# write the formatted addresses to the output file

addresses = []

with open(filename) as f:
    for line in f:
        addresses.append(line.strip().split(","))

addresses = addresses[1:]

with open(outfile, "w") as f:
    for each in addresses:
        nicer = [x.title() for x in each if x]
        nicer[-1] = nicer[-1].upper()
        out_string = "\n".join(nicer)
        f.write(out_string+"\n\n\n")
        