import re
from glob import glob

output_dict = {}
filenames = glob("input*.txt") #creates a list of all files matching the phrase "input*" from current dir

#creates object for both high risk and low risk phrases using regular expressions
high_risk_ph = re.compile(r'voldemort | mundane | pinocchio | dark\slord | ki\w+en ', re.I | re.X)
low_risk_ph = re.compile(r'esolutions | gangster | ugliest | destiny | shooter | plan ', re.I | re.X)

for file in filenames:
	reader = open(file).read()
	#uses regex object to get the list of matched phrases and adds the length of that list to outputfile dict
	output_dict[file] = len(high_risk_ph.findall(reader)*2) + len(low_risk_ph.findall(reader))

#writes out dict into output.txt(creates if does not exist)file in a clean format[Key(k) : Value(v)]
with open('output.txt', 'w') as writeout:
    for k, v in output_dict.items():
    	writeout.write(str(k) + ' : '+ str(v) + '\n')
