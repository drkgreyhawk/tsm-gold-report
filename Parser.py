import os
import re

##### CONFIG YOUR SCRIPT HERE #####
# TSM account file location
account_folder_location = "C:/Program Files (x86)/World of Warcraft/_retail_/WTF/Account/[ACCOUNT_NAME]/SavedVariables/TradeSkillMaster.lua"
# The faction you want the gold report from
faction = "Horde"
# The server you want the gold report from
server = "Hyjal"
##### END CONFIG #####


temp_file = "temp.txt"

def findGold():
	file = open(temp_file, "r")
	lines = file.readlines()
	file.close()

	number_of_lines = 0
	total_copper = 0

	for line in lines:
		line = line.strip()
		temp_string = re.findall(r'\d+[\"]', line)
		for copper in temp_string:
			total_copper += int(copper.replace('"', ""))

	gold = total_copper / 10000

	print("According to the last TSM report your " + server + ", " + faction + " characters have a total of: ")
	print(str(f'{gold:,}') + "g")

	os.remove(temp_file)


def main():
	file = open(account_folder_location,"r")
	lines = file.readlines()
	file.close()

	for line in lines:
		line = line.strip()
		if line.find(faction + " - " + server + "@internalData@goldLog") != -1:
			new_file = open(temp_file, "a+")
			new_file.write(f"{line}\n")
			new_file.close()

	findGold()

main()
input()
