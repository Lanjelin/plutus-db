import string

def letters(number):
  letters = string.ascii_lowercase
  count = len(letters)
  first = number // count
  second = number % count
  return(letters[first]+letters[second])

SIZE_HINT = (35 * 500000)

addressNumber = 0
fileNumber = 0
done = False
with open("Bitcoin_addresses_LATEST.txt", "rt") as f:
  while not done:
    buffer = f.readlines(SIZE_HINT)
    if not buffer:
      # done reading file, shouldnt occur though
      break
    # we only need P2PKH addresses
    for i, j in enumerate(buffer):
      if not j.startswith('1'):
        buffer = buffer[:i]
        done = True
        break
      addressNumber += 1
    with open(f"database/database_{letters(fileNumber)}", "wt") as of:
      of.write("".join(buffer))
      print(f"database_{letters(fileNumber)}")
      fileNumber += 1

print(addressNumber)
