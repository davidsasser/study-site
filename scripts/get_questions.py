import urllib.request
from bs4 import BeautifulSoup
import gzip
import io
import requests

f = open("dec2015.json", "a")
f.write("[\n")

for i in range(0,50):
    f.write("\t{\n")
    q_id = 282+i
    q_no = 1+i
    line = '\t\t"' + str(q_no) + '"' + ': {\n'
    f.write(line)
    html = requests.get(f'https://netexam.pmgurus.com/ugc-net-online-questions.aspx?q=net-exam-paper-1-ugc-net-paper-1-Dec2015&gid=3&h=5&QID={q_id}&Qno={q_no}').content

    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find(id=f'question-{q_no}')

    q = soup.findAll("div", {"class": "card-stats-primary"})
    a1 = soup.find(id='label_1_1')
    a2 = soup.find(id='label_1_2')
    a3 = soup.find(id='label_1_3')
    a4 = soup.find(id='label_1_4')
    f.write('\t\t\t"q": "' + q[1].getText().strip().replace('\n', ' ').replace('\r', ' ') + '",\n')
    f.write('\t\t\t"answers": {\n')
    f.write('\t\t\t\t"1": "' + a1.getText().strip().replace('\n', ' ').replace('\r', ' ') + '",\n')
    f.write('\t\t\t\t"2": "' + a2.getText().strip().replace('\n', ' ').replace('\r', ' ') + '",\n')
    f.write('\t\t\t\t"3": "' + a3.getText().strip().replace('\n', ' ').replace('\r', ' ') + '",\n')
    f.write('\t\t\t\t"4": "' + a4.getText().strip().replace('\n', ' ').replace('\r', ' ') + '",\n')

    correct = str(a1).split('VerifyAnswer')[1].split(',')[2].split(')')[0].strip()
    correct = correct.split('\'')[1]
    if(correct == 'A'):  
        f.write('\t\t\t\t"correct": 1\n')
    if(correct == 'B'):  
        f.write('\t\t\t\t"correct": 2\n')
    if(correct == 'C'):  
        f.write('\t\t\t\t"correct": 3\n')
    if(correct == 'D'):  
        f.write('\t\t\t\t"correct": 4\n')
    f.write('\t\t\t}\n')
    f.write('\t\t}\n')
    if(i != 49 ):
        f.write('\t},\n')
    else:
        f.write('\t}\n')

f.write("]")
f.close()