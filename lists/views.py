from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})




# def Json(request):
# 	x = [{'buyers': 8,
# 		  'buyers_change': 0,
# 		  'buyers_comparison': 8,
# 		  'chat_conversion': '3.25',
# 		  'chat_count': 142,
# 		  'chatted_buyers': 4,
# 		  'chatted_buyers_change': 0,
# 		  'chatted_buyers_comparison': 4,
# 		  'chatted_carts': 4,
# 		  'chatted_visitors': 123,
# 		  'chatted_visitors_change': 146,
# 		  'chatted_visitors_two_days_ago': (50,),
# 		  'conversion': '4.68',
# 		  'domain_name': u'domain2.com',
# 		  'has_shopping_cart': True,
# 		  'reporting_link': 'http://127.0.0.1:8000/reporting/dailystats?date=2015-04-01',
# 		  'sales_chatted': ('1960.30'),
# 		  'sales_chatted_average': '490.07',
# 		  'sales_chatted_change': -100,
# 		  'sales_chatted_comparison': ('1092830293048013096147.20'),
# 		  'sales_monthly_average': '7.74',
# 		  'sales_monthly_chatted_average': '5.25',
# 		  'sales_monthly_chatted_change': 100,
# 		  'sales_monthly_chatted_comparison':('0.00'),
# 		  'sales_monthly_chatted_total': ('21.00'),
# 		  'sales_monthly_total': ('61.90'),
# 		  'sales_monthly_total_change': 100,
# 		  'sales_monthly_total_comparison': ('0.00'),
# 		  'sales_total_comparison': ('1092830293048013096374.20'),
# 		  'session_count': 106,
# 		  'show_monthly': True,
# 		  'tags': [{'name': u'awesome taggggggggggggggg ggggggggggggggggg', 'tag_count': 5},
# 		  			{'name': u'not so awesome tag', 'tag_count': 5},
# 		  			{'name': u'awesome taggggggggggggggg ggggggggggggggggg', 'tag_count': 10}
# 		  			],
# 		  'total_carts': 8,
# 		  'total_sales': ('2275.50'),
# 		  'total_sales_average': '284.44',
# 		  'total_sales_change': -100,
# 		  'vis_change': 1,
# 		  'visitor_chat_count': 142,
# 		  'visitor_companies': [(u'ISP99', 99),
# 		                        (u'ISP98', 98),
# 		                        (u'ISP97', 97),
# 		                        (u'ISP96', 96),
# 		                        (u'ISP95', 95),
# 		                        (u'ISP94', 94),
# 		                        (u'ISP93', 93),
# 		                        (u'ISP92', 92),
# 		                        (u'ISP91', 91),
# 		                        (u'ISP90', 90),
# 		                        (u'ISP89', 89),
# 		                        (u'ISP88', 88),
# 		                        (u'ISP87', 87),
# 		                        (u'ISP86', 86),
# 		                        (u'ISP85', 85)],
# 		  'visitor_count': 171}]

# 	return render(request, 'dailycustomer.html', {'domains': x, "domain": "service.giosg.com", 'yesterday': datetime.datetime.now().strftime("%B %d, %Y")})

