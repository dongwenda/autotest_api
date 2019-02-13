# -*- coding: utf-8 -*-
from common.runmethod import RunMethod
from common.get_data import GetData
from common.common_util import CommonUtil
from common.dependent_data import DependentData
from common.send_mail import SendEmail

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    def go_on_run(self):
        pass_count = []
        fail_count = []

        #10行就，返回10，
        rows_count = self.data.get_lines()
        #第0行是头信息，从1行开始
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                requestData = self.data.get_data(i)
                headers = self.data.is_header(i)
                expect = self.data.get_expect(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    dependData = DependentData()
                    #获取依赖响应数据
                    dependResData = dependData.get_data_by_key(i)
                    #获取依赖的field
                    dependField = self.data.get_dependField(i)
                    requestData[dependField] = dependResData
                res = self.run_method.run_main(method,url,requestData,headers)
                print(type(res))
                if self.com_util.is_contain(expect,res):
                    print("=测试Pass=")
                    self.data.write_result(i,'Pass')
                    pass_count.append(i)
                else:
                    print("=测试Fail=")
                    self.data.write_result(i,res)
                    fail_count.append(i)

        sendMail = SendEmail()
        sendMail.send_main(pass_count,fail_count)

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()