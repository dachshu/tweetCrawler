import os
import re


class FileRW:
    def __init__(self):
        self.data_file = None
        self.log_file = None
        self.account = None

    def is_exist(self, account):
        self.account = account
        data_path = os.path.join(os.getcwd(), account + '.data')
        log_path = os.path.join(os.getcwd(), account + '.log')
        if not (os.path.exists(data_path) and os.path.exists(log_path)):
            self.data_file = open(data_path, 'w+', encoding='utf-8')
            self.log_file = open(log_path, 'w+', encoding='utf-8')
            return (False, None, None)

        (last_id, last_time) = self.sync_between_data_log(data_path, log_path)
        if last_id and last_time:
            return (True, last_id, last_time)
        else:
            return (False, None, None)

    def sync_between_data_log(self, data_path, log_path):
        self.log_file = open(log_path, 'r+', encoding='utf-8')
        if self.log_file:
            log_id_list = self.log_file.read().split('\n')
            if log_id_list:
                data_pattern = re.compile(r'(^|\n\n)?(\d+)(\n)(\d+)(\n)(<p.*>.+</p>)')

                self.data_file = open(data_path, 'r+', encoding='utf-8')
                if log_id_list[-1]:
                    last_log_id = log_id_list[-1]
                else:
                    last_log_id = log_id_list[-2]
                data_list = data_pattern.split(self.data_file.read())

                idx = data_list.index(last_log_id)
                self.data_file.seek(0)
                self.data_file.truncate()
                self.data_file.write(''.join(data_list[:idx + 5]))

                return (int(last_log_id), int(data_list[idx+2]))
            else:
                self.data_file = open(data_path, 'w+', encoding='utf-8')
                return (None, None)

    def write_tweet_list(self, tw_list):
        for tweet_id, time, data in reversed(tw_list):
            self.write_tweet(tweet_id, time, data)

    def write_tweet(self, tweet_id, time, data):
        full_data = str(tweet_id) + '\n' + str(time) + '\n' + data

        try:
            if self.data_file.tell() == 0:
                self.data_file.write(full_data)
            else:
                self.data_file.write('\n\n' + full_data)

            if self.log_file.tell() == 0:
                self.log_file.write(str(tweet_id))
            else:
                self.log_file.write('\n' + str(tweet_id))
        except:
            print('write err')


if __name__ == '__main__':
    with open('realDonaldTrump.log', 'r+t') as f:
        print(f.read().split('\n'))