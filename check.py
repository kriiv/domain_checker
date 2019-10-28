import whois, csv

with open('domains.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader: # row is a domain to be checked
    w = whois.whois(row)
    print(row)
    if w['status'] == None:
      print ('Available')
      li = open('available.txt', 'a')
      li.write(row+'\n')
      li.close()
    
