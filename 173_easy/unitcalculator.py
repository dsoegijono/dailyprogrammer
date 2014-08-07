
length = { "metres" : 1.0, "inches" : 0.0254, "miles" : 1609.34, "attoparsecs" : 0.0309 }
weight = { "kilograms" : 1.0 , "pounds" : 2.2 , "ounces" : 35.27 , "hogsheads of beryllium" : 0.0023 }


def main():
  inp = raw_input("> ")
  temp = inp.split()
  q = float(temp[0])
  fr = temp[1].lower()
  to = (' '.join(temp[3:])).lower()

  if fr in length:
    if to in length:
      res = q * length[fr] / length[to]
      print_result(q, fr, res, to)
    else:
      print_error(q, fr, to)
  elif fr in weight:
    if to in weight:
      res = q * weight[fr] / weight[to]
    else:
      print_error(q, fr, to)
  else:
    print "ERROR: Incorrect unit(s)"

  print inp

def print_result(q, fr, res, to):
  print str(q) + " " + fr + " is " + str(res) + " " + to

def print_error(q, fr, to):
  print str(q) + " " + fr + " can't be converted to " + to

if __name__ == "__main__":
    main()
