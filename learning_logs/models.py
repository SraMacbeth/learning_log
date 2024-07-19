from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta holds extra information for managing a model; here it allows us to set a special attribute telling Django to use Entries when it needs to refer to more than one entry. Without this, Django would refer to multiple entries as Entrys"""
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        """we tell Django to show just the first 50 characters of text. We also add an ellipsis to clarify that we’re not always displaying the entire entry"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."