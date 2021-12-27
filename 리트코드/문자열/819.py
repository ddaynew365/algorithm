import re
def mostCommonWord( paragraph: str, banned: list[str]) -> str:
    paragraph = paragraph.lower()
    paragraph = re.sub('[^\w]'," ",paragraph)
    str_list = paragraph.split(" ")
    count = dict()
    for i in str_list:
        if i not in banned and i != "":
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
    
    
    maxi = max(count.values())
    for i in count:
        if count[i] == maxi :
            return i

# ----------------------------
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # paragraph = paragraph.lower()
    # paragraph = re.sub('[^\w]'," ",paragraph)
    # str_list = paragraph.split(" ")
    words = [word for word in re.sub("[^\w]"," ",paragraph)
                .lower().split()
                    if word not in banned]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return max(counts, key = counts.get)
  
# --------------------------------
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
  # paragraph = paragraph.lower()
  # paragraph = re.sub('[^\w]'," ",paragraph)
  # str_list = paragraph.split(" ")
  words = [word for word in re.sub("[^\w]"," ",paragraph)
              .lower().split()
                  if word not in banned]
  counts = collections.Counter(words)
  return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
