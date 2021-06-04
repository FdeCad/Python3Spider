import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
headers={
        'authority': 'www.taobao.com',
        'cache - control': 'max - age = 0',
        'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
        'upgrade - insecure - requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'referer': 'https://login.taobao.com/',
        'sec - fetch - site': 'same - site',
        'sec - fetch - user': '?1',
        'sec - fetch - mode': 'navigate',
        'sec - fetch - dest': 'document',
        'accept - language': 'zh - CN, zh;q = 0.9, en;q = 0.8, en - GB;q = 0.7, en - US;q = 0.6',
        'cookie':'enc=MDEE5u92NDIRwGlqMIbQpF383fLM%2FAMuFXaV0qrZ5rrkJ5tL%2BHvF26SLUQHfNm0Rstn9DCBZHwcUPj3EgeNAPQ%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; lLtC1_=1; _m_h5_tk=b573121ef3bfea4ebe195f1a70fdb54d_1622715079531; _m_h5_tk_enc=9e260b44bba0550377fded127837d2c7; t=dacbceddfe1a439d0c7186d4d6053b4f; _tb_token_=e567833336ead; cookie2=10758fc022e8575781d53b9f7ee8a343; _samesite_flag_=true; cna=TFwlGAaB+iMCAW8mpBcGi2fT; sgcookie=E100fK7UZEV%2Fpi2yX%2BY4DTusq0U7AN7Rcir7oR1RAkbAFxUsHS9zX6hVF8BwcrmG4uLkaNx4tnC%2FP%2FoTxzblq9WzlQ%3D%3D; unb=3789347291; uc3=nk2=F5RBzL9uoE4vrA%3D%3D&vt3=F8dCuw77rE7vrcnv8Ec%3D&id2=UNcALA6lCeY%2FDA%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; csg=ed4db0ce; lgc=tb49282640; cookie17=UNcALA6lCeY%2FDA%3D%3D; dnk=tb49282640; skt=225bb7f922dfa9b7; existShop=MTYyMjcwODUyNA%3D%3D; uc4=id4=0%40UgDGpIWcVU2OFR38ZFdsOrg52Ub6&nk4=0%40FY4KqaBnOMUZqujezhjYO2F8Y06o; tracknick=tb49282640; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=012; _nk_=tb49282640; cookie1=BxJK1l2e8mSvTcM%2Bhva619GD26O8WDuXNaM3HValYEw%3D; mt=ci=4_1; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie14=Uoe2z%2BTKtUIDZA%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&existShop=false&cookie15=URm48syIIVrSKA%3D%3D&pas=0; tfstk=cvG5BPxOzgjWVdpFa4TVU-0rtqFCCtCbJLatPAeQO6hwBER4D61cm1r_ybkhxRL3l; l=eBa_N5R4O2lm0kuEBO5Churza77TPKdb4sPzaNbMiInca1yP9H3lSNCCWvYeWdtjgtCb6etz9nynXRLHR3fiO8SsbAqfjCrr2xvO.; isg=BCcnANPyC4biw7Ash4ija3gitlvxrPuOZC5DBfmZUrZS6EeqAX1f3bKiDuj2ANMG',
    }
r = requests.get('https://www.taobao.com',headers = headers)
print(r.status_code)
soup=BeautifulSoup(r.text,'lxml')
print(soup)
shangpinming = re.findall('"title":"(.*?)"',r.text)
# print(shangpinming)

