file_lines = (line for line in open("data/Individual_Incident_2004.csv", "r", encoding="utf8"))
list_line = (s.rstrip().split(",") for s in file_lines)

next(list_line)
print(next(list_line))
