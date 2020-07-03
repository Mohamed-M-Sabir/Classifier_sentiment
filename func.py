punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
    return s


def get_neg(s):
    s = strip_punctuation(s)
    s = s.lower().split(" ")
    c = 0
    for i in s:
        if i in negative_words:
            c += 1
    return c


def get_pos(s):
    s = strip_punctuation(s)
    s = s.lower().split(" ")
    c = 0
    for i in s:
        if i in positive_words:
            c += 1
    return c

file = open("files/project_twitter_data.csv", "r")
mostr = file.readlines()
result = open('files/resulting_data.csv', 'w')
result.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

for i in mostr[1:]:
    m = i.split(',')
    m[2] = m[2].replace('\n', '')
    result.write("{}, {}, {}, {}, {}\n".format(m[1], m[2], get_pos(m[0]), get_neg(m[0]),get_pos(m[0])-get_neg(m[0])))

