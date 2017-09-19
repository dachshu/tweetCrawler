import os
import re


class FileRW:
    def __init__(self):
        self.data_file = None
        self.log_file = None
        self.name = None

    def IsExist(self, name):
        self.name = name
        data_path = os.path.join(os.getcwd(), name + '.data')
        log_path = os.path.join(os.getcwd(), name + '.log')
        if not (os.path.exists(data_path) and os.path.exists(log_path)):
            return False

        last_time = self.SyncBetweenDataLog(data_path, log_path)
        return (True, last_time)

    def SyncBetweenDataLog(self, data_path, log_path):
        self.log_file = open(log_path, 'a+')
        if self.log_file:
            log_time_list = self.log_file.readlines()
            if log_time_list:
                data_pattern = re.compile(r'(?:^)?(\d+)(\n<p>.+</p>\n\n)')

                self.data_file = open(data_path, 'a+')
                last_log_time = log_time_list[-1]
                data_list = data_pattern.split(self.data_file.read())

                idx = data_list.index(last_log_time)
                self.data_file.seek(0)
                self.data_file.truncate()
                self.data_file.write(''.join(data_list[:idx+2]))

                return float(last_log_time)
            else:
                self.data_file = open(data_path, 'w+')
                return None

    def WriteTweet(self, time, data):
        pass


if __name__ == "__main__":
    pattern = re.compile(r'(?:^)?(\d+)(\n<p>.+</p>\n\n)')
    d = pattern.split(
        '1241252436\n<p>wefwefsdaoij</p>\n\n3259983460\n<p>wefnbnnnbkn</p>\n\n12542356\n<p>dsfoijwe</p>\n\n')
    print(d)
    i = d.index('3259983460')
    with open("test.txt", 'a+') as f:
        f.seek(0)
        print(f.tell())
        f.truncate()
        f.write(''.join(d[:i+2]))
