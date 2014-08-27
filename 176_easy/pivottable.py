_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def parse_data(data):
  arr = {}
  for line in data:
    if line[0] in arr:
      if line[1] in arr[line[0]]:
        arr[line[0]][line[1]] += int(line[2])
      else:
        arr[line[0]][line[1]] = int(line[2])
    else:
      arr[line[0]] = { line[1] : int(line[2]) }
  return arr

def print_array(arr):
  print ("Tower\t" + "\t".join(_days)).expandtabs(8)
  print "-" * (8*8)
  for line in sorted(arr):
    s = line + "\t"
    for day in _days:
      s += str(arr[line][day]) + "\t"
    print s.expandtabs(8)

def main():
  file = open("windfarm.txt", "r")
  data = [line.strip().split() for line in file.readlines()]
  file.close()
  arr = parse_data(data)
  print_array(arr)

if __name__ == "__main__":
    main()
