#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from .models import Post

from django.urls import reverse

from django.utils import timezone

import requests
from bs4 import BeautifulSoup
import operator
from datetime import datetime






def index(request):
	
	site = 'https://bash.im/'
	response = requests.get(site)
	soup = BeautifulSoup(response.text, 'html.parser')
	bash_posts = []
	for article in soup.find_all('article'):
		post = dict.fromkeys(['id', 'text', 'date_pub', 'rating'])
		post['id'] = int(article.get('data-quote'))
		text = article.find('div').text.split('\n')
		post['text'] = text[8]
		#post['date_pub'] = text[4]
		post['date_pub'] = datetime.strptime(text[4], '        %d.%m.%Y в %H:%M')
		if(str(text[21]).isdigit()):
			post['rating'] = int(text[21])
		else:
			post['rating'] = 0
		if(post['rating'] > 400):		# rating limit
			bash_posts.append(post)
	
	bash_posts.sort(key=operator.itemgetter('date_pub'))
	bash_posts = bash_posts[::-1]
	
	posts_list = Post.objects.order_by('-pub_date')
	
	return render(request, 'posts/list.html', {'posts_list': posts_list, 'bash_posts': bash_posts})



def start_search(request):
	
	site = 'https://bash.im/'
	response = requests.get(site)
	soup = BeautifulSoup(response.text, 'html.parser')
	bash_posts = []
	for article in soup.find_all('article'):
		post = dict.fromkeys(['id', 'text', 'date_pub', 'rating'])
		post['id'] = int(article.get('data-quote'))
		text = article.find('div').text.split('\n')
		post['text'] = text[8]
		#post['date_pub'] = text[4]
		post['date_pub'] = datetime.strptime(text[4], '        %d.%m.%Y в %H:%M')
		if(str(text[21]).isdigit()):
			post['rating'] = int(text[21])
		else:
			post['rating'] = 0
		if(post['rating'] > 400 and request.POST['keyword'] in post['text']):		# 400 is rating limit
			bash_posts.append(post)
	
	bash_posts.sort(key=operator.itemgetter('date_pub'))
	bash_posts = bash_posts[::-1]
	
	posts_list = []
	for post in Post.objects.all():
		if(request.POST['keyword'] in post.post_text):
			posts_list.append(post)
	
	return render(request, 'posts/list.html', {'posts_list': posts_list, 'bash_posts': bash_posts})



