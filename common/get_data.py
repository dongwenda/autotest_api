# -*- coding: utf-8 -*-
from common.operation_xlsw import OperationExcel
from common.data_config import *
from common.operation_json import OperationJson
from operation_header import OperationHeader


class GetData:

    def __init__(self):
        self.opers = OperationExcel()

    #获取行数，第一行是头字段，行数从1开始
    def get_lines(self):
        return self.opers.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        col = get_run_col()
        run = self.opers.get_cell_value(row,col)
        if run == 'yes':
            return True
        else:
            return False

    # 是否携带header
    def is_header(self,row):
        col = get_header_col()
        header = self.opers.get_cell_value(row,col)
        if header == 'write':
            op_header = OperationHeader()
            return op_header.write_cookie()
        elif header == 'yes':
            return get_header_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = get_method_col()
        method = self.opers.get_cell_value(row,col)
        return method

    #获取url
    def get_url(self,row):
        col = get_url_col()
        url = self.opers.get_cell_value(row,col)
        return url

    #获取请求数据
    def get_data(self,row):
        col = get_data_col()
        data = self.opers.get_cell_value(row,col)
        if data == '':
            return None
        return self.get_data_from_json(row,data)

    #通过获取关键字拿到data数据
    def get_data_from_json(self,data):
        opera_json = OperationJson()
        request_data = opera_json.get_data(data)
        return request_data

    #获取预期结果
    def get_expect(self,row):
        col = get_expect_col()
        expect =self.opers.get_cell_value(row,col)
        if expect == '':
            return None
        return expect

    #写入执行结果
    def write_result(self,row,value):
        col = get_result_col()
        self.opers.write_cell_value(row,col,value)

    #获取依赖数据的key
    def get_dependKey(self,row):
        col = get_dataDepend_col()
        dependKey = self.opers.get_cell_value(row,col)
        if dependKey == "":
            return None
        else:
            return dependKey

    def is_depend(self,row):
        col = get_caseDepend_col()
        depend_caseID = self.opers.get_cell_value(row,col)
        if depend_caseID == "":
            return None
        else:
            return depend_caseID
    def get_dependField(self,row):
        col = get_fieldDepend_col()
        fieldDepend = self.opers.get_cell_value(row,col)
        if fieldDepend == "":
            return None
        else:
            return fieldDepend

if __name__ == '__main__':
    g = GetData()
    print(g.get_lines())
