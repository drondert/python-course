import urllib.request

LOG_URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

result_list = []
with urllib.request.urlopen(LOG_URL) as file_log:
    for line in file_log:
        line_log = line.decode('utf-8').replace('"', '').split()
        result_list.append((line_log[0], line_log[5], line_log[6]))
