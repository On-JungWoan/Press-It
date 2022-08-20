from django.shortcuts import render
import requests

def test(request):
    return render(request, 'main/index.html')

def t(request):
    if request.method == 'POST':
        print(request.POST.get('article_url'))    
        print(request.POST.get('min_len'))
    
    return render(request, 'main/test.html')

def makeSmr(request):
    #### parameters ####
    rapidapi_key = '4da86840b9msh71f5f3001df2bdbp11c887jsn7539dc2585c0'
    naver_client_id = '8YCSHXilHy0XXZAcRBrz'
    naver_client_secret = 'VBVdSQvJAo'    
    detail = False
    trans = True
            
    if request.method == 'POST':
        print(request.POST.get('article_url'))
        print(request.POST)
              
        article_url = request.POST.get('article_url')
        min_len = request.POST.get('min_len')
        max_len = request.POST.get('max_len')
        frm = request.POST.get('frm')
        to = request.POST.get('to')
    
    
    
    #### scripts ####
    
    ## TLDRThis ##
    url = "https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/"
    payload = {
      "url": article_url, # 주소
      "min_length": min_len, # 최소 길이
      "max_length": max_len, # 최대 길이
      "is_detailed": detail # 한 문장으로 반환할 것인지 여부
    }
    headers = {
      "content-type": "application/json",
      "X-RapidAPI-Key": rapidapi_key,
      "X-RapidAPI-Host": "tldrthis.p.rapidapi.com"
    }
    sum_response = requests.request("POST", url, json=payload, headers=headers).json()
    summary = sum_response['summary'][0].strip()

    
    ## Papago ##
    if trans==True:
        url = "https://openapi.naver.com/v1/papago/n2mt"
        payload = {
            "source": frm,
            "target": to,
            "text": summary,
        }
        headers = {
            "content-type": "application/json",
            "X-Naver-Client-Id": naver_client_id,
            "X-Naver-Client-Secret": naver_client_secret,
        }
        trans_response = requests.request("POST", url, json=payload, headers=headers).json()
        translation = trans_response['message']['result']['translatedText']

        context = {
            'summary' : translation,
            'original_text' : summary,
            'original_json' : sum_response,
            'translation_json' : trans_response
        }    
    else:
        context = {
              'original_text' : summary,
              'original_json' : sum_response,
        }        
    
    
    return render(request, 'main/test.html', context)