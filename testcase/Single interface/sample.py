def extract_data(self, testcase_extarct, response):
    """
    提取接口的返回值，支持正则表达式和json提取器
    :param testcase_extarct: testcase文件yaml中的extract值
    :param response: 接口的实际返回值
    :return:
    """
    try:
        pattern_lst = ['(.*?)', '(.+?)', r'(\d)', r'(\d*)']
        for key, value in testcase_extarct.items():

            # 处理正则表达式提取
            for pat in pattern_lst:
                if pat in value:
                    ext_lst = re.search(value, response)
                    if pat in [r'(\d+)', r'(\d*)']:
                        extract_data = {key: int(ext_lst.group(1))}
                    else:
                        extract_data = {key: ext_lst.group(1)}
                    self.read.write_yaml_data(extract_data)
            # 处理json提取参数
            if '$' in value:
                ext_json = jsonpath.jsonpath(json.loads(response), value)[0]
                if ext_json:
                    extarct_data = {key: ext_json}
                    logs.info('提取接口的返回值：', extarct_data)
                else:
                    extarct_data = {key: '未提取到数据，请检查接口返回值是否为空！'}
                self.read.write_yaml_data(extarct_data)
    except Exception as e:
        logs.error(e)