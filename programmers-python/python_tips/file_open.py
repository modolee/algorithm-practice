with open('zip.py') as file:
  for line in file.readlines():
    print(line.strip().split('\t'))