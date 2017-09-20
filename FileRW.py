import os
import re


class FileRW:
    def __init__(self):
        self.data_file = None
        self.log_file = None
        self.name = None

    def is_exist(self, name):
        self.name = name
        data_path = os.path.join(os.getcwd(), name + '.data')
        log_path = os.path.join(os.getcwd(), name + '.log')
        if not (os.path.exists(data_path) and os.path.exists(log_path)):
            self.data_file = open(data_path, 'w+', encoding='utf-8')
            self.log_file = open(log_path, 'w+', encoding='utf-8')
            return False

        last_time = self.SyncBetweenDataLog(data_path, log_path)
        if last_time:
            return (True, last_time)
        else:
            return False

    def sync_between_data_log(self, data_path, log_path):
        self.log_file = open(log_path, 'r+', encoding='utf-8')
        if self.log_file:
            log_time_list = self.log_file.readlines()
            if log_time_list:
                data_pattern = re.compile(r'(?:^)?(\d+)(\n<p>.+</p>)(\n\n)')

                self.data_file = open(data_path, 'r+', encoding='utf-8')
                last_log_time = log_time_list[-1]
                data_list = data_pattern.split(self.data_file.read())

                idx = data_list.index(last_log_time)
                self.data_file.seek(0)
                self.data_file.truncate()
                self.data_file.write(''.join(data_list[:idx + 2]))

                return float(last_log_time)
            else:
                self.data_file = open(data_path, 'w+', encoding='utf-8')
                return None

    def write_tweet_list(self, tw_list):
        for id, data in tw_list:
            self.write_tweet(id, data)

    def write_tweet(self, time, data):
        data_time = str(time)
        full_data = data_time + '\n' + data

        try:
            if self.data_file.tell() == 0:
                self.data_file.write(full_data)
            else:
                self.data_file.write('\n\n' + full_data)

            if self.log_file.tell() == 0:
                self.log_file.write(data_time)
            else:
                self.log_file.write('\n' + data_time)
        except:
            print('write err')


if __name__ == "__main__":
    frw = FileRW()

    frw.IsExist('test')
    #frw.WriteTweet(100, '<p>test string1</p>')
    #frw.WriteTweet(200, '<p>Test String2</p>')
    frw.WriteTweet(300, '<p>test String3</p>')
    frw.WriteTweet(400, '<p>Test string4</p>')

    print('end')
