from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        msg = '姓名:'+request.POST['name']+'\n邮箱:'+request.POST['email']+'\n标题'+request.POST['subject']+'\n内容:'+request.POST['message']
        send_mail('官网客户信息',msg,settings.EMAIL_FROM,
            ['302930114@qq.com'])
        return HttpResponse('OK')
    return render(request, 'main/index.html')

def anliall(request):
    return render(request, 'main/anliall.html')
	
def oushi(request):
    return render(request, 'main/anli.html', context={
                        'mulu': 'oushi',
                        'leixing': '欧式'
})
def katong(request):
    return render(request, 'main/anli.html', context={
                        'mulu': 'katong',
                        'leixing': '卡通'
})
def zhongshi(request):
    return render(request, 'main/anli.html', context={
                        'mulu': 'zhongshi',
                        'leixing': '中式'
})
def xiandai(request):
    return render(request, 'main/anli.html', context={
                        'mulu': 'xiandai',
                        'leixing': '现代'
})
def jianyue(request):
    return render(request, 'main/anli.html', context={
                        'mulu': 'jianyue',
                        'leixing': '简约'
})


def about(request):
    return render(request, 'main/about.html')

def about1(request):
    return render(request, 'main/about1.html')
	
def about2(request):
    return render(request, 'main/about2.html')
	
def about3(request):
    return render(request, 'main/about3.html')

def about4(request):
    return render(request, 'main/about4.html')



def news(request):
    return render(request, 'main/news.html', context={
    'muqian': 'news','title': '新闻中心','n1': " 绿色环保新型内墙面装饰材料——硅藻泥壁材", 'n2': u"聚焦日德等国新型绿色建材发展状况",'n3': u"警惕!室内污染对孩子的危害",'n4': 
u"警惕!室内污染对孩子的危害",'n5': u"中国软件开发行业前景分析",'n6': u"软件开发的成败更多的是在于人，而不是技术",
'n7': u"中银监及人行联手发10号文 规范第三方支付",'n8': u"软件开发的成败更多的是在于人，而不是技术"})

def news1(request):
    return render(request, 'main/news.html', context={
    'muqian': 'news1','title': '企业动态','n1': u" 绿色环保新型内墙面装饰材料——硅藻泥壁材", 'n2': u"聚焦日德等国新型绿色建材发展状况",'n3': u"警惕!室内污染对孩子的危害",'n4': 
u"警惕!室内污染对孩子的危害",'n5': u"中国软件开发行业前景分析",'n6': u"软件开发的成败更多的是在于人，而不是技术",
'n7': u"中银监及人行联手发10号文 规范第三方支付",'n8': u"软件开发的成败更多的是在于人，而不是技术"})

def news2(request):
    return render(request, 'main/news.html', context={
    'muqian': 'news2','title': '行业新闻','n1': u" 绿色环保新型内墙面装饰材料——硅藻泥壁材", 'n2': u"聚焦日德等国新型绿色建材发展状况",'n3': u"警惕!室内污染对孩子的危害",'n4': 
u"警惕!室内污染对孩子的危害",'n5': u"中国软件开发行业前景分析",'n6': u"软件开发的成败更多的是在于人，而不是技术",
'n7': u"中银监及人行联手发10号文 规范第三方支付",'n8': u"软件开发的成败更多的是在于人，而不是技术"})

def news3(request):
    return render(request, 'main/news.html', context={
    'muqian': 'news3','title': '品牌动态','n1': u" 绿色环保新型内墙面装饰材料——硅藻泥壁材", 'n2': u"聚焦日德等国新型绿色建材发展状况",'n3': u"警惕!室内污染对孩子的危害",'n4': 
u"警惕!室内污染对孩子的危害",'n5': u"中国软件开发行业前景分析",'n6': u" 注册域名留心四五点",
'n7': u"中银监及人行联手发10号文 规范第三方支付",'n8': u"软件开发的成败更多的是在于人，而不是技术"})

def jiameng(request):
    return render(request, 'main/jiameng.html')
	
def cont(request):
    return render(request, 'main/cont.html')
	
def VR(request):
    return render(request, 'main/VR.html')
	
def VRxiandai(request):
    return render(request, 'main/VRxiandai.html')
def VRzhongshi(request):
    return render(request, 'main/VRzhongshi.html')
def VRmeishi(request):
    return render(request, 'main/VRmeishi.html')
def VRbeiou(request):
    return render(request, 'main/VRbeiou.html')
def VRoushi(request):
    return render(request, 'main/VRoushi.html')
def VRdizhonghai(request):
    return render(request, 'main/VRdizhonghai.html')
def VRbieshu(request):
    return render(request, 'main/VRbieshu.html')