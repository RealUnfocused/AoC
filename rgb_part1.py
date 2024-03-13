import re

f = open("puzzleinput.txt")
text = f.read()
f.close()
lines = text.split("\n")

def cleardict(dict: dict):
        for i in dict:
            dict[i] = 0

def getpower(dict : dict):
    power = 1
    for i in dict:
        power *= dict[i]
    return power

def part1():
    max_dict = {
        "red":12,
        "green":13,
        "blue":14,
    }

    currentcount_dict = {
        "red":0,
        "green":0,
        "blue":0,
    }

    def compare(dict1 : dict, dict2 : dict):
      for x in dict1:
        if dict2[x] > dict1[x]:
          return False

      return True

    sum = 0
    impossibleGame = 0
    for i in range(len(lines)):
        lines[i] = lines[i].replace(f"Game {i+1}:", "")
        segment = lines[i].split(";")
        for n in range(len(segment)):
            cleardict(currentcount_dict)
            minisegment = segment[n].split(",")
            for j in minisegment:
                colortype = re.search("red|green|blue", j)
                currentcount_dict[colortype.group()] += int(re.search("\d+", j).group())
            if compare(max_dict, currentcount_dict) == False:
                impossibleGame = (i+1)
                break
        if (i+1) != impossibleGame:
           sum += (i+1)

    print(sum)

def part2():
    min_dict = {
        "red": 0, 
        "blue":0, 
        "green":0
       }
    sum = 0
    for i in range(len(lines)):
        lines[i] = lines[i].replace(f"Game {i+1}:", "")
        segment = lines[i].split(";")
        cleardict(min_dict)
        for n in range(len(segment)):
            minisegment = segment[n].split(",")
            for j in minisegment:
                colortype = re.search("red|green|blue", j).group()
                amount = int(re.search("\d+", j).group())
                if min_dict[colortype] < amount:
                    min_dict[colortype] = amount
        sum += getpower(min_dict)
    print(sum)


part1()
part2()