# coding: utf-8


class BaseCalculator(object):

    def get_expression(self):
        raise NotImplementedError()

    def parse_expression(self, expr):
        raise NotImplementedError()

    def compile_token(self, token):
        raise NotImplementedError()

    def evaluate(self, structure):
        raise NotImplementedError()

    def put_result(self, expr, result):
        raise NotImplementedError()

    def __call__(self):
        expr = self.get_expression()
        token = self.parse_expression(expr)
        compiled_structure = self.compile_token(token)
        result = self.evaluate(compiled_structure)
        self.put_result(expr, result)
