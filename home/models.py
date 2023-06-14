from django.db import models

class HomePagePoster(models.Model):
    '''Home page model'''
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True, max_length=350)
    poster = models.ImageField(upload_to='Posters/')
    albums_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title
#
#
# class myuser(models.Model):
#     password = models.CharField(max_length=128)
#     registered_at = models.DateTimeField(auto_now=True)
#     username = models.CharField(max_length=128)
#     email = models.CharField(max_length=128)
#
# class category(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.CharField(max_length=128)
#
# class difficulty(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.CharField(max_length=128)
#
#
# class tag(models.Model):
#     name = models.CharField(max_length=128)
#
# class meditation(models.Model):
#     title = models.CharField(max_length=128)
#     description = models.DateTimeField(auto_now=True)
#     duration = models.CharField(max_length=128)
#     author = models.CharField(max_length=128)
#     difficulty = models.ForeignKey(to=difficulty, on_delete=models.CASCADE)
#     category = models.ForeignKey(to=category, on_delete=models.SET_NULL, null=True)
#     tag = models.ForeignKey(to=tag, on_delete=models.SET_NULL, null=True)
#
# class notification(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     text = models.CharField(max_length=128)
#     is_read = models.BooleanField()
#     created_at = models.DateTimeField(auto_now=True)
#
# class favourite(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     meditation = models.ForeignKey(to=meditation, on_delete=models.CASCADE)
#
# class review(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     meditation = models.ForeignKey(to=meditation, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=128)
#     grade = models.IntegerField()
#
# class media(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     meditation = models.ForeignKey(to=meditation, on_delete=models.CASCADE)
#     file = models.FileField()
#
# class subscription(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     type = models.CharField(max_length=128)
#     start_date = models.DateTimeField(auto_now=True)
#     end_date = models.DateTimeField(auto_now=True)
#
# class payment(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     method = models.CharField(max_length=128)
#     payment_date = models.DateTimeField(auto_now=True)
#     summ = models.DecimalField(max_digits=2, decimal_places=2)
#
# class meditation_history(models.Model):
#     user = models.ForeignKey(to=myuser, on_delete=models.CASCADE)
#     meditation = models.ForeignKey(to=meditation, on_delete=models.CASCADE)
#     duration = models.CharField(max_length=128)
#     start_time = models.DateTimeField(auto_now=True)
#     end_time = models.DateTimeField(auto_now=True)
