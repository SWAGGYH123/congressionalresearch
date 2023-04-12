import requests
import os.path
import time
import sys

sys.setrecursionlimit((10**5))

api_key=["FSCA2C5X7hRZoVOwi8BCfEXtHwgfdSgPrtwOu7a4","vydf7CegTv33TKBbnwvpQewlYr4JZj0eN8M4FfuL","9rcbF2pb0s8yjSLsrxVbhBRZnLMUeSZMZbd8gvdQ","EyRlJX4I6NxixGDc4MkgmYYyXEzaycRNPdC2xJ94","zmyfV3l1bl3yKl5aEedRK2fRdsda0n70raIWUqbg","KxcZ5qgCc5J5HRzjXTyrYstElMApwhII9kc3sYc6","TcugNhb2j79pp90VXufVsWsAZMvMuaY9dYL8CI8h","uIS0M4IEKFQTrVYKYHTAe6GhzzJerVyukLNnu9yk","cwBvd3YwxOyaMRZwjfD42QwrOdQscsNfaNmgbWDk", "xsDjvNP2dOsymG7KnNpU162cebXLhJVCy9hnKeGf","BDpeski1RMWicesQJxjITW78WpO47Pr9c9V4NQ6j","gB3QjiqwP8T5riJGkt6eJWZIAeGwUhbZMjkmacCW","5s7cUS87p2RRIJItDE4sQEBsqKqIPb3bsMOWYuzr","LEebtLpIElrV7bOAq4Qjt8erURgY0dSHryRsGetu","7TXfidk6qUh7Tq1hbKybfTFKAyWVbBaEKlGCMTjr","Bu0874sptMqfCOErxtA2a0e65AnfKUVpiAglyf6u","0DFqr6VsceuwVwOEiYg1uTRLZRLVsLT1mFxAUBTA","kubvZx6ebSo14vjNdXvwucvgoSw9ToJnCzXmpmab","apgKUtNatxMUGZFbSFDzf2ULCCw0i8xvs6pzkq7P","zcdtcKgMYFJxruQnYsOomd0j7TtG5LZ5SCLv5JwN"]

def json_scrape_hr_bills(cong, num, n,x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/hr/{num}?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Bills', f'{cong}_hr_{num}_general.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    if ((cong==111 and ((num==3 or num==4) or (num==5 or num==6) or (num==7 or num==8) or (num==9 or num==10))) or (cong==112 and ((num==6 or num==13) or (num==17 or num==18) or (num==19 or num==20)))) or (((cong==113 and ((num==8 or num==9) or (num==13 or num==14) or (num==16 or num==17) or (num==18 or num==19))) or (cong==114 and ((num==1 or num==4) or (num==11 or num==13) or (num==14 or num==15) or (num==16 or num==17) or (num==18 or num==19)))) or ((cong==115 and ((num==9 or num==11) or (num==13 or num==14) or (num==16 or num==17) or num==18)) or (cong==116 and ((num==10 or num==15) or (num==16 or num==17) or num==18)))):
        num+=1
        json_scrape_hr_bills(cong, num, n,x)
    elif os.path.isfile(f'E:\Research\Bills\{cong}_hr_{num}_general.json') == True:
        print("complete")
        n+=1
        num+=1
        if n==950:
            x+=1
            time.sleep(3660)
            if x==(len(api_key)-1):
                x=0
            n=1
            json_scrape_hr_bills(cong, num,n,x)
        if response.status_code == 200:  
            json_scrape_hr_bills(cong, num, n,x)
        else:
            cong+=1
            if cong==117:
                return   
            else:
                json_scrape_hr_bills(cong, 1, n,x)   
    else:
        print("finished")
        return
    
def json_scrape_s_bills(cong, num,n,x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/s/{num}?api_key={api_key[x]}')
    writeFile =open(os.path.join('/Users/Hugo/Desktop/Research/Research/Bills', f'{cong}_s_{num}_general.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    if os.path.isfile(f'/Users/Hugo/Desktop/Research/Research/Bills/{cong}_s_{num}_general.json') == True:
        print("complete")
        n+=1
        if n==975:
            time.sleep(3660)
            num+=1
            n=1
            json_scrape_s_bills(cong, num, n, x)
        elif response.status_code == 200:
            num+=1
            json_scrape_s_bills(cong, num, n, x)
        else:
            cong+=1
            if cong==117:
                return  
            else:
                json_scrape_s_bills(cong, 1, n, x)      
    else:
        os.remove(os.path.join('/Users/Hugo/Desktop/Research/Research/Bills', f'{cong}_s_{num}_general.json'))
        print("finished")
        return

def json_scrape_hjres_bills(cong, num, n, x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/hjres/{num}?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Bills', f'{cong}_hjres_{num}_general.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    n=1
    if os.path.isfile(f'E:\Research\Bills\{cong}_hjres_{num}_general.json') == True:
        print("complete")
        n+=1
        if n==975:
            time.sleep(3660)
            x+=1
            if x==(len(api_key)-1):
                x=0
            n=1
            json_scrape_hjres_bills(cong, num, n, x)
        if response.status_code == 200:
            num+=1
            json_scrape_hjres_bills(cong, num, n, x)
        else:
            cong+=1
            if cong==117:
                return   
            else:     
                json_scrape_hjres_bills(cong, 1, n, x)
    else:
        print("finished")
        return
    
def json_scrape_sjres_bills(cong, num, n, x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/sjres/{num}?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Bills', f'{cong}_sjres_{num}_general.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    n=1
    if os.path.isfile(f'E:\Research\Bills\{cong}_sjres_{num}_general.json') == True:
        print("complete")
        n+=1
        if n==975:
            time.sleep(3660)
            x+=1
            if x==(len(api_key)-1):
                x=0
            n=1
            json_scrape_sjres_bills(cong, num, n,x)
        if response.status_code == 200:
            num+=1
            json_scrape_sjres_bills(cong, num,n,x)
        else:
            cong+=1
            if cong==117:
                return
            else:
                json_scrape_sjres_bills(cong, 1,n,x)        
    else:
        print("finished")
        return

def json_scrape_hr_cosponsors(cong, num, n,x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/hr/{num}/cosponsors?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Cosponsor', f'{cong}_hr_{num}_cosponsors.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    n=1
    if ((cong==111 and ((num==3 or num==4) or (num==5 or num==6) or (num==7 or num==8) or (num==9 or num==10))) or (cong==112 and ((num==6 or num==13) or (num==17 or num==18) or (num==19 or num==20)))) or (((cong==113 and ((num==8 or num==9) or (num==13 or num==14) or (num==16 or num==17) or (num==18 or num==19))) or (cong==114 and ((num==1 or num==4) or (num==11 or num==13) or (num==14 or num==15) or (num==16 or num==17) or (num==18 or num==19)))) or ((cong==115 and ((num==9 or num==11) or (num==13 or num==14) or (num==16 or num==17) or num==18)) or (cong==116 and ((num==10 or num==15) or (num==16 or num==17) or num==18)))):
        num+=1
        json_scrape_hr_cosponsors(cong, num, n,x)
        if os.path.isfile(f'E:\Research\Cosponsor\{cong}_hr_{num}_general.json') == True:
            print("complete")
            n+=1
            num+=1
            if n==975:
                time.sleep(3660)
                x+=1
                if x==(len(api_key)-1):
                    x=0
                n=1
                json_scrape_hr_cosponsors(cong, num, n,x)
            if response.status_code == 200:  
                json_scrape_hr_cosponsors(cong, num, n,x)
            else:
                cong+=1
                if cong==117:
                    return  
                else:
                    json_scrape_hr_cosponsors(cong, 1, n,x)      
        else:
            print("finished")
            return
    
def json_scrape_s_cosponsors(cong, num, n,x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/s/{num}/cosponsors?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Cosponsor', f'{cong}_s_{num}_cosponsors.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    if os.path.isfile(f'E:\Research\Cosponsor\{cong}_s_{num}_cosponsors.json') == True:
        print("complete")
        n+=1
        if response.status_code == 200:
            num+=1
            json_scrape_s_cosponsors(cong, num,n,x)
            if n==975:
                time.sleep(3660)
                num+=1
                n=1
                if x==(len(api_key)-1):
                    x=0
                json_scrape_s_cosponsors(cong, num,n,x)
        else:
            cong+=1
            if cong==117:
                return
            else:
                json_scrape_s_cosponsors(cong, 1,n,x)        
    else:
        print("incomplete")
        return

def json_scrape_hjres_cosponsors(cong, num, n,x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/hjres/{num}/cosponsors?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Cospsonsor', f'{cong}_hjres_{num}_cosponsors.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    n=1
    if os.path.isfile(f'E:\Research\Cosponsor\{cong}_hjres_{num}_cosponsors.json') == True:
        print("complete")
        n+=1
        if response.status_code == 200:
            num+=1
            json_scrape_hjres_cosponsors(cong, num,n,x)
            if n==975:
                time.sleep(3660)
                num+=1
                if x==(len(api_key)-1):
                    x=0
                json_scrape_hjres_cosponsors(cong, num,n,x)
                n=1
        else:
            cong+=1
            if cong==117:
                return  
            else:
                json_scrape_hjres_cosponsors(cong, 1,n,x)      
    else:
        print("incomplete")
        return
    
def json_scrape_sjres_cosponsors(cong, num, n,x):
    response = requests.get(f'https://api.congress.gov/v3/bill/{cong}/sjres/{num}/cosponsors?api_key={api_key[x]}')
    writeFile =open(os.path.join('E:\\Research\\Cosponsor', f'{cong}_sjres_{num}_cosponsors.json'), 'w')
    writeFile.write(response.text)
    writeFile.close()
    if os.path.isfile(f'E:\Research\Cosponsor\{cong}_sjres_{num}_cosponsors.json') == True:
        print("complete")
        n+=1
        num+=1
        if n==975:
            time.sleep(3660)
            x+=1
            if x==(len(api_key)-1):
                x=0
            n=1
            json_scrape_sjres_cosponsors(cong, num, n,x)
        if response.status_code == 200:
            num+=1
            json_scrape_sjres_cosponsors(cong, num,n,x)
        else:
            cong+=1
            if cong==117:
                return     
            else:
                json_scrape_sjres_cosponsors(cong, 1,n,x)   
    else:
        print("finished")
        return



#json_scrape_hr_bills(112, 1222, 1, 6)
json_scrape_s_bills(114, 2946, 1, 10)
#json_scrape_hjres_bills(111, 1, 1, 0)
#json_scrape_sjres_bills(111, 1, 1, 11)
#json_scrape_hr_cosponsors(111, 1, 1, 0)
#json_scrape_s_cosponsors(111, 1, 1, 11)
#json_scrape_hjres_cosponsors(111, 1, 1, 0)
#json_scrape_sjres_cosponsors(111, 1, 1, 11)