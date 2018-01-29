import os, re

file_num = 1

def matcher(content):
    rex = 'Content-Type:\stext/plain;\scharset=UTF-8\s(.*?)Content-Type:\stext.html'
    complied_rex = re.compile(rex)
    email_content = content.replace('\n', ' ').replace('\r', ' ')
    match = complied_rex.search(email_content)
    if match != None and match.group(1) != ' ':
        return match.group(1)
    else:
        return

def file_write(body_text, category, file_num):
    path = 'data/dataset/' + category + '/'+ category +'-'+ str(file_num)
    file = open(path, 'w')
    file.write(body_text)
    print(str(file_num) +' '+ category + ' emails written')
    file.close()

def start(category_name, file_num):
    files = os.listdir('data/myemails/' + category_name + '/')
    for filename in files:
        f = open('data/myemails/' + category_name + '/' + filename, 'rt')
        content = f.read()
        f.close()
        email_body = matcher(content)
        if email_body != None:
            file_write(email_body, category_name, file_num)
            file_num += 1


start('primary', file_num)
