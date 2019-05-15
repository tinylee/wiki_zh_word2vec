#!/usr/bin/env python
# -*- coding: utf-8  -*-
#逐行读取文件数据进行jieba分词

import jieba
import jieba.analyse
import jieba.posseg as pseg #引入词性标注接口 
import sys
import os


if __name__ == '__main__':
    rootdir = os.path.dirname(os.path.realpath(__file__))
    f = open(rootdir + '/wiki.zh.simp.txt', 'r', encoding='utf8')
    target = open(rootdir + '/wiki.zh.simp.seg.txt', 'w', encoding='utf8')
    print('open files.')

    lineNum = 1
    line = f.readline()
    while line:
        print('---processing ',lineNum,' article---')
        seg_list = jieba.cut(line,cut_all=False)
        line_seg = ' '.join(seg_list)
        target.writelines(line_seg)
        lineNum = lineNum + 1
        line = f.readline()

    print('well done.')
    f.close()
    target.close()
