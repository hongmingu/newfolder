from django.db import models

class Post(models.Model):

    postText = models.TextField(max_length=2000)
    postCreatedDate = models.DateTimeField(auto_now_add=True)
    postRelationship = models.OneToOneField('relationship.ContentRelationship', on_delete=models.CASCADE)

    def __str__(self):
        return self.postText