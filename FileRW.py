import os
import re
import types


class FileRW:

    def __init__(self):
        self.filter = TweetFilter()
        pass

    def get_all_account(self):
        tw_path = os.path.join(os.getcwd(), 'tweets')
        tw_list = []
        if os.path.isdir(tw_path):
            file_list = os.listdir(tw_path)
            for f in file_list:
                dir_path = os.path.join(tw_path, f)
                if os.path.isdir(dir_path):
                    data_path = os.path.join(dir_path, 'data')
                    log_path = os.path.join(dir_path, 'log')
                    if os.path.exists(data_path) and os.path.exists(log_path):
                        (last_year, last_month) = self.sync_between_data_log(
                            data_path, log_path)
                        if last_year and last_month:
                            tw_list.append((f, last_year, last_month))
                        else:
                            os.remove(data_path)
                            os.remove(log_path)
                            os.rmdir(dir_path)
                    else:
                        if os.path.exists(data_path):
                            os.remove(data_path)
                        elif os.path.exists(log_path):
                            os.remove(log_path)
                        os.rmdir(dir_path)
        else:
            os.mkdir(tw_path)

        return tw_list

    def delete_later_tweet(self, path, last_id, file=None):
        if file:
            data_file = file
            data_file.seek(0)
        else:
            data_file = open(path, 'r+', encoding='utf-8')

        data_pattern = re.compile(r'(^|\n\n)?(\d+)(\n)(\d+)(\n)(<p .+>.+</p>)')
        data_list = data_pattern.split(data_file.read())

        try:
            idx = data_list.index(last_id)
            data_file.seek(0)
            data_file.truncate()
            data_file.write(''.join(data_list[:idx + 5]))
        except ValueError:
            print('the data in log file is not in data file')

    def check_last_month(self, data_file, log_file, year, month):
        if log_file.tell() > 0:
            log_file.seek(0)
            log_list = log_file.readlines()
            last_date = log_list[-1].split('-')
            last_month = last_date[1]
            last_year = last_date[0]
            if int(last_month) == month and int(last_year) == year:
                new_last_month = None
                for i, log in enumerate(reversed(log_list)):
                    if re.match(r'\d+-\d+\n', log):
                        new_last_month = len(log_list) - i - 1
                        break

                if new_last_month:
                    new_last_id = log_list[new_last_month - 1].strip()
                    self.delete_later_tweet(None, new_last_id, file=data_file)

                    log_list[new_last_month] = log_list[new_last_month].strip()
                    log_file.seek(0)
                    log_file.truncate()
                    log_file.write(''.join(log_list[:new_last_month+1]))
                else:
                    data_file.seek(0)
                    data_file.truncate()
                    log_file.seek(0)
                    log_file.truncate()

    def sync_between_data_log(self, data_path, log_path):
        log_file = open(log_path, 'r+', encoding='utf-8')
        if log_file:
            log_list = log_file.read().split('\n')
            if log_list and len(log_list) >= 2:
                last_log_id = log_list[-2]
                self.delete_later_tweet(data_path, last_log_id)

                year_month = log_list[-1].split('-')
                return (int(year_month[0]), int(year_month[1]))
            else:
                return (None, None)

    def write_tweet_list(self, account, tw_list, year, month):
        dir_path = os.path.join(os.getcwd(), 'tweets', account)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

        data_file = open(os.path.join(dir_path, 'data'), 'a+', encoding='utf-8')
        log_file = open(os.path.join(dir_path, 'log'), 'a+', encoding='utf-8')

        self.check_last_month(data_file, log_file, year, month)

        data = ''
        log = ''
        date = str(year) + '-' + str(month)
        for i, t, d in reversed(tw_list):
            if len(data) > 0:
                data += '\n\n' + str(i) + '\n' + str(t) + '\n' + d
            else:
                data += str(i) + '\n' +str(t) + '\n' + d

            if len(log) > 0:
                log += '\n' + str(i)
            else:
                log += str(i)

        if data_file.tell() > 0:
            data_file.write('\n\n' + data)
        else:
            data_file.write(data)

        if log_file.tell() > 0:
            log_file.write('\n' + log + '\n' + date)
        else:
            log_file.write(log + '\n' + date)

    def filter_tweets(self, account, form, batch_size=100):
        dir_path = os.path.join(os.getcwd(), 'tweets', account)
        filtered_list = []

        with open(os.path.join(dir_path, 'data'), 'r') as data_file:
            i = 0
            s = ''
            tweets = []
            
            for line in data_file:
                s += line
                result = re.search(r'\d+\n\d+\n(<p .+>.+</p>)', s)
                if result:
                    s = ''
                    i += 1
                    tweets.append(result.group(1))

                if i == 100:
                    i = 0
                    filtered_list += self.filter.filtering(tweets, form)

            if i > 0:
                filtered_list += self.filter.filtering(tweets, form)
        
        return filtered_list


if __name__ == '__main__':
    # fw = FileRW()
    # l = fw.get_all_account()
    # print('저장된 리스트')
    # print(l)

    # d = [('222', '2221', '<p class=shit>asdf</p>'), ('223', '2222',
    #                                               '<p class=shit>wq1</p>'), ('224', '2223', '<p class=shit>bvn</p>'), ('227', '2224', '<p class=shit>ghj</p>')]
    # fw.write_tweet_list('test', d, 2017, 11)

    t = '222\n2221\n<p class=shit>asdf1</p>\n\n222\n2221\n<p class=shit>asdf2</p>'
    ret = re.search(r'\d+\n\d+\n(<p .+>.+</p>)', t)
    print(ret.group(1))
