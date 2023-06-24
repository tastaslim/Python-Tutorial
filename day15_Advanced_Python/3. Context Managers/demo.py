# # Our version of context manager
# # class Taslim:
# #     """"""
# #
# #     def __init__(self, path):
# #         """Constructor"""
# #         self.path = path
# #
# #     def __enter__(self):
# #         """
# #         Open the file
# #         """
# #         self.conn = open(self.path, 'w')
# #         return self.conn
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         """
# #         Close the file
# #         """
# #         self.conn.close()
# #         if exc_val:
# #             raise
# #
# #
# # if __name__ == '__main__':
# #     path_file = 'intro.txt'
# #     with Taslim(path_file) as conn:
# #         cursor = conn.write('Hello World')
# from contextlib import contextmanager, suppress
#
# """
# Once the with statement ends, control returns back to the file_open function and it continues with the code following
# the yield statement. That causes the finally statement to execute, which closes the file. If we happen to have an OSError
# while working with the file, it gets caught and finally statement still closes the file handler.
# """
#
#
# @contextmanager
# def open_file(path, mode):
#     print("Enter method called")
#     f_obj = ''
#     try:
#         f_obj = open(path, f'{mode}')
#         yield f_obj
#     except OSError:
#         print("We had an error!")
#     finally:
#         print('Closing file')
#         f_obj.close()
#     print("Exit method called")
#
#
# # with open_file('intro.txt', 'w') as f_obj1:
# #     f_obj1.write('some_data')
#
# # print(locale.getpreferredencoding(False))
#
# # No error will be thrown when file is not found. It is very handy when you don't want to stop execution of your program
# # in case of any specific error.
# with suppress(FileNotFoundError):
#     with open('not_found_file.txt') as f:
#         f.write('some_data')

from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as obj:
    with redirect_stdout(obj):
        help(redirect_stdout)
