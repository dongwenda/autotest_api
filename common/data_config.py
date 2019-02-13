# -*- coding: utf-8 -*-
class global_var:
    #case_id
    name = 0
    url = 1
    run = 2
    method = 3
    header = 4
    case_depend = 5
    data_depend = 6
    field_depend = 7
    data = 8
    expect = 9
    result = 10




#获取案例名称的列数
def get_name_col():
    return global_var.name

#获取url的列数
def get_url_col():
    return global_var.url

#获取是否执行的列数
def get_run_col():
    return global_var.run

#获取请求方法的列数
def get_method_col():
    return global_var.method

#获取header的列数
def get_header_col():
    return global_var.header

#获取依赖的案例的列数
def get_caseDepend_col():
    return global_var.case_depend

#获取依赖案例的字段的列数
def get_dataDepend_col():
    return global_var.data_depend

#获取依赖field的字段
def get_fieldDepend_col():
    return global_var.field_depend

#获取请求数据的列数
def get_data_col():
    return global_var.data

#获取预期结果的列数
def get_expect_col():
    return global_var.expect

#获取执行结果的列数
def get_result_col():
    return global_var.result

def get_header_value():
    header = {
        "header":"is header",
        "cookie":"is cookie"
    }
    return header
