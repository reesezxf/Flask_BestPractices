# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 2:46 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : customException.py
# @Software: PyCharm


from flask import request, json
from werkzeug.exceptions import HTTPException

# Common CustomException
Bad_Request = (400, '参数类型错误')
NOT_AUTHORIZED = (401, '未登录-认证信息失败-令牌过期')
FORBIDDEN = (403, '无权限')
ServerError = (500, '服务器内部异常')
NOT_TOKEN = (666, '没token玩个毛')
ICU = (996, '没救了')
KEY_NE = (99999, '小B崽子key都没传够')
DATA_IS_EXISTENCE = (777, '数据已经存在')
DATABASE_ERROR = (1066, '数据库异常')

# Api CustomException
already_regist = (999, '手机号已注册')
tel_length_err = (1000, '手机号应为11位')
not_tel = (1001, '手机号未注册')
psw_length_err = (1002, '密码少于6位')
psw_err = (1003, '密码错误')
psw2_err = (1004, '2次密码不一致')

# CMS CustomException
LOGIN_ERROR = (2001, '登录失败-服务器非常正常-请重试!')


class CustomException(HTTPException):
    code = 500
    error_code = 999
    msg = '服务器在路上'

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(CustomException, self).__init__(self.msg, None)


def ab_code(data):
    C = {
        400: Bad_Request,
        401: NOT_AUTHORIZED,
        403: FORBIDDEN,
        500: ServerError,
        666: NOT_TOKEN
    }
    code = C.get(data)[0]
    msg = C.get(data)[1]
    raise CustomException(code=code, msg=msg)
