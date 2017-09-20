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
            return (False, None)

        last_time = self.sync_between_data_log(data_path, log_path)
        if last_time:
            return (True, last_time)
        else:
            return (False, None)

    def sync_between_data_log(self, data_path, log_path):
        self.log_file = open(log_path, 'r+', encoding='utf-8')
        if self.log_file:
            log_time_list = self.log_file.read().split('\n')
            if log_time_list:
                data_pattern = re.compile(r'(^|\n\n)?(\d+)(\n<p.*>.+</p>)')

                self.data_file = open(data_path, 'r+', encoding='utf-8')
                if log_time_list[-1]:
                    last_log_time = log_time_list[-1]
                else:
                    last_log_time = log_time_list[-2]
                data_list = data_pattern.split(self.data_file.read())

                idx = data_list.index(last_log_time)
                print(idx)
                self.data_file.seek(0)
                self.data_file.truncate()
                self.data_file.write(''.join(data_list[:idx + 2]))

                return int(last_log_time)
            else:
                self.data_file = open(data_path, 'w+', encoding='utf-8')
                return None

    def write_tweet_list(self, tw_list):
        for id, data in reversed(tw_list):
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


if __name__ == '__main__':
    with open('realDonaldTrump.log', 'r+t') as f:
        print(f.read().split('\n'))