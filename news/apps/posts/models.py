import datetime

from django.db import models

from django.utils import timezone


class Post(models.Model):
	post_title = models.CharField('post name', max_length = 200)
	post_text = models.TextField('post text')
	pub_date = models.DateTimeField('publication date')
	post_rating = models.DecimalField(max_digits = 4, decimal_places = 0, default=0)
	#pub_by_admin = models.BooleanField('Опубликовано админом', default=True)
	
	def __str__(self):
		return self.post_title
	
	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
	
	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'



#class Comment(models.Model):
#	article = models.ForeignKey(Article, on_delete = models.CASCADE)
#	author_name = models.CharField('author name', max_length = 50)
#	comment_text = models.CharField('comment text', max_length = 200)
#	
#	def __str__(self):
#		return self.author_name
#	
#	class Meta:
#		verbose_name = 'Комментарий'
#		verbose_name_plural = 'Комментарии'




