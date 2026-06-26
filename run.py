import shutil
import pytest
import os
import webbrowser
from conf.setting import REPORT_TYPE

if __name__ == '__main__':

    if REPORT_TYPE == 'allure':
        # pytest.main(
        #     ['-s', '-v', '--alluredir=./report/temp', './testcase/Single interface', '--clean-alluredir',
        #      '--junitxml=./report/results.xml'])
        pytest.main(
            ['-s', '-v', '--alluredir=./report/temp', './testcase/Single interface', '--clean-alluredir'])
        shutil.copy('./environment.xml', './report/temp')
        #原来的代码，一次性的，必须每跑完展示
        #os.system(f'allure serve ./report/temp')
        #优化后，先生成，在打开
        os.system(f'allure generate ./report/temp -o ./report/allure-report --clean')
        #os.system(f'allure open ./report/allure-report')

    elif REPORT_TYPE == 'tm':
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', '--pytest-tmreport-path=./report/tmreport'])
        webbrowser.open_new_tab(os.getcwd() + '/report/tmreport/testReport.html')
