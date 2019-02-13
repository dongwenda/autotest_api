# -*- coding: utf-8 -*-
from common.operation_xlsw import OperationExcel
from common.runmethod import RunMethod
from common.get_data import GetData
from jsonpath_rw import parse
import json

class DependentData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    #通过case_id去获取该case_id的整行数据
    def get_case_row_data(self):
        row_data = self.opera_excel.get_row_data_by_caseid(self.case_id)
        return row_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_from_json(row_num)
        headers = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = run_method.run_main(method,url,request_data,headers)
        return json.loads(res)

    #根据依赖的key去获取执行以来测试case的响应，最后返回
    def get_data_by_key(self,row):
        dependKey = self.data.get_dependKey(row)
        resData = self.run_dependent()
        json_exe = parse(dependKey)
        madle = json_exe.find(resData)
        return [math.value for math in madle][0]

