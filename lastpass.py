# Generate last pass csv from OSX keychain plist.
import os
import sys

file = open(sys.argv[1])

class entry:
	pass

def extract_val(line):
	return line.split('=')[1].replace("\"", "").strip()

def generate_csv(lines):
	# print lines
	e = entry()
	for line in lines:
		if "svce" in line:
			e.name = extract_val(line)
		elif "acct" in line:
			e.username = extract_val(line)

	print ",,%s,%s,,,%s,Imported" % (e.username, lines[-1].replace("\"", "").strip(), e.name)


print "url,type,username,password,hostname,extra,name,grouping"

current_lines = []
for line in file:
	if line.startswith("keychain:") and current_lines:
		generate_csv(current_lines)
		current_lines = []
	current_lines.append(line)
	