# -*- coding: utf-8 -*-
class CommonUtil:
    def is_contain(self,str1,str2):
        '''
        判断一个字符串是否在另外一个字符串中
        str1:查找的字符串
        str2:被查找的字符串
        return: True or False
        '''
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag