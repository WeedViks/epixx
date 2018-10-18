# url.py
import urllib.request
def url_open(url):
    lst = list()    
    try:     
        with urllib.request.urlopen(url) as webpage:
            for line in webpage: 
                line = line.decode('utf-8')
                line = line.strip()
                lst.append(line)
        return lst
    except:        
        return None 
        
if __name__ == '__main__':
    print(url_open("http://dfedorov.spb.ru/python3/src/romeo.txt"))
    
