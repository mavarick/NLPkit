#encoding:utf8

def lexical_diversity(text):
    return len(text) * 1.0 / len(set(text))


def percentage(count, total):
    return 100 * count / total


# get words' frequency
# nltk.FreqDist(text)

# get conditianal frequency
# nltk.ConditionalFreqDist(text)

# get english words
# nltk.corpus.words.words()
## stopwords
# nltk.corpus.stopwords.words()
## names
# nltk.corpus.names.words()
## pronounce
# nltk.corpus.cmudict.entries()

# WordNet
## 获得包含word的所有词条
# from nltk.corpus import wordnet as wn
# wn.lemmas('car')
# 上位词和下位词
# wn.synsets('tree')
# wn.synset('tree.n.01').part_meronyms() #
# wn.synset('tree.n.01').member_holonyms()
# 反义词
# wn.synset('demand.n.02').antonyms()
# 动词的多种含义
# wn.synset('eat.v.01').entailments()

# 感觉： WordNet还是非常的牛叉！可以找到实体之间的关联！



