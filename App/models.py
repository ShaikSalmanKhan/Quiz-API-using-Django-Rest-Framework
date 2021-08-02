from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category_name.title()} "

    class Meta:
        verbose_name_plural="Categories"    
    


class Question(models.Model):
    question          =   models.CharField(max_length=255,null=True)
    choices           = (
        ( 'True' ,'True' ),
        ( 'False','False'),
	) 
    correct_answer    =   models.CharField(choices=choices, max_length=5)	
    created           =   models.DateTimeField(auto_now_add=True)
    updated           =   models.DateTimeField(auto_now=True)
    active            =   models.BooleanField(default=True)
    category          =   models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category",blank=True, null=True)
    
    def __str__(self):
        return f"{self.question.title()} |  {self.correct_answer} "

