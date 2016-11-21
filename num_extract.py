import re

file = '/home/vagrant/phone_num.txt'
with open (file) as f:
     content = f.readlines()

print content

for num in content:
     num = num.strip('\n')
    
     matches = re.findall('(\d{3})[-\.\s]??(\d{3})[-\.\s]??(\d{4})|(\(\d{3}\)\s*)(\d{3})[-\.\s]??(\d{4})|(\d{3})[-\.\s]??(\d{4})', num)

     print matches
