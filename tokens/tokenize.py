# encoding:utf8

'''
jieba tokenizing

refer: https://github.com/fxsjy/jieba
'''

import jieba
user_dict_file = "user_dict_file"
jieba.load_userdict(user_dict_file)

def tokenize(text, method="jieba", **kargs):
    '''
    :param text:  page content
    :param method:  `jieba`
    :param kargs:
      for jieba: the arguments contains:
        cut_all=True  # 全模式, 无法消除歧义问题
        cut_all=False # 精确模式
    :return: tokens list, with element type: (word, flag)
    '''
    seg_list= jieba.cut(text, **args)
    return seg_list


import jieba.analyse
def extract_keywords(text, method='tfidf', withWeight=True, topK=20, allowPOS=None):
    '''
    :param text:   page content, according jieba intro, code could be utf8, unicode, gbk
    :param method: `tfidf`, `textrank`
    :param withWeight: True, return tuple with element (word, weight); False, only word
    :param topK: number of keywords
    :param allowPOS: part of speech tagging. (ns, n, vn, v)
        ns:
        n:
        vn:
        v:
    :return: keyword list with element: (word, weight) if withWeight=True, or list of only word

    NOTICE
    TFIDF extracting keywords should use idf data, default is about 4M(jieba/extra_dict/idf.txt.big)
    if you want to change it, use:
        `jieba.analyse.TFIDF(idf_path=None)`

    OTHER, include:
        STOP WORD  :: https://github.com/fxsjy/jieba
    '''
    if method == "tfidf":
        return jieba.analyse.extract_tags(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
    elif method == "textrank":
        return jieba.analyse.textrank(text, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
    raise Exception("No existed method: {}".format(method))





