# 첫번째 풀이 - 정규식과 메소드를 사용
import re
import collections
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

# 두번째 풀이 - 리스트컴프리헨션 사용, collections.defaultdict() 사용 , max()의 key 사용 -> key = 리스트.get

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub("[^\w]"," ",paragraph)
                .lower().split()
                    if word not in banned]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return max(counts, key = counts.get)
  
# 세번째 풀이 - collections.Counter() 사용 -> most_common메소드
def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
  # paragraph = paragraph.lower()
  # paragraph = re.sub('[^\w]'," ",paragraph)
  # str_list = paragraph.split(" ")
  words = [word for word in re.sub("[^\w]"," ",paragraph)
              .lower().split()
                  if word not in banned]
  counts = collections.Counter(words)
  return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
