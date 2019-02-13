# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,file_name='./data/interface.xlsx',sheet_id=0):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.data = self.get_data()

    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        return self.data.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_cell_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据case_id，找到对应行的内容
    def get_row_data_by_caseid(self,case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_data_by_rownum(row_num)
        return row_data

    #根据case_id，找到对应的行号
    def get_row_num(self,case_id):
        # 第0行是头，所以从第1行开始
        num = 1
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num += 1

    #根据行号，找到该行的内容
    def get_row_data_by_rownum(self,row_num):
        tables = self.data
        row_data = tables.row_values(row_num)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            col_data = self.data.col_values(col_id)
        else:
            col_data = self.data.col_values(0)
        return col_data


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_lines())
    print(opers)
    print(opers.get_cell_value(1,10))
    print(opers.get_cell_value(1,9))
    opers.write_cell_value(1,10,'Pass')