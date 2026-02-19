import csv

#list of servers
hosts = [["server_1","192.168.1.1"],["server_2","10.1.1.1"]]

with open('hosts.csv', mode='w') as hosts_file:
    writer = csv.writer(hosts_file)
    writer.writerows(hosts)
    