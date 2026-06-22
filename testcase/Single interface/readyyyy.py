# -*- coding: utf-8 -*-
import yaml
import traceback
import os


def get_testcase_yaml(file):
    testcase_list = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            print(data)
            print(len(data))
            if len(data) <= 1:
                yam_data = data[0]
                base_info = yam_data.get('baseInfo')
                for ts in yam_data.get('testCase'):
                    param = [base_info, ts]
                    testcase_list.append(param)
                return testcase_list
            else:
                return data
    except Exception as e:
        print(f'报错：{traceback.format_exc()}')


res = get_testcase_yaml('login.yaml')
rsp = res[0][1]
print(res)
print(len(res))
print(rsp)
for i,j in rsp.items():
    print(i,'-----',j)