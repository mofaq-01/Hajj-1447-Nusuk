with open('/home/ubuntu/report_project/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find section 3 comment
marker1 = 'SECTION 3'
idx1 = content.find(marker1)
print('SECTION 3 found at:', idx1)
if idx1 > 0:
    print('Context around SECTION 3:')
    print(repr(content[idx1-300:idx1+100]))
