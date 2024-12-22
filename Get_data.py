import string
import numpy as np
import requests
from bs4 import BeautifulSoup

def get_data(from_time, to_time):
    with open('NationStates.txt', 'r') as f:
        NationStates = [line.strip() for line in f]


    # url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=cromreland;q=census;scale=0;mode=history;from=0"
    url_1 = "https://www.nationstates.net/cgi-bin/api.cgi?nation="
    url_2 = ";q=census;scale="
    url_3 = ";mode=history;from="
    url_4 = ";to="
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    index_list = ["0", "2", "6", "47", "48"]

    data = [[0, 0, 0, 0, 0, 0, 0] for i in NationStates]
    i = j = 0

    def get_isuues_answered(url):
        # print(response.status_code)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        index = int(soup.nation.issues_answered.string)
        return index
    def get_time_of_life(url):
        # print(response.status_code)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        index = int(soup.nation.lastlogin.string) - int(soup.nation.firstlogin.string)
        return index 

    
    i = 0
    for state in NationStates:
        j = 0
        data[i][j] = get_isuues_answered(url_1 + state)
        j += 1
        data[i][j] = get_time_of_life(url_1 + state)
        j += 1
        response = requests.get(url_1 + state + url_2 + "0+2+6+47+48" + url_3 + from_time + url_4 + to_time, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for index in index_list:
            s = soup.find(id = index)
            if s.score is not None:
                s = s.score.string
            else:
                s = "999"
            if ("." in s) or ("," in s):
                data[i][j] = int(s.translate(str.maketrans('', '', ".,")))/100
            else:
                data[i][j] = int(s)
            j += 1
        print(i)
        i += 1
    np.save("States", NationStates)
    np.save("data", data)
