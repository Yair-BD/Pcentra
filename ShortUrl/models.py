from django.db import models

class Url(models.Model):
    original_url = models.URLField(help_text="Enter Url Adress", unique=False) # For one url adrres can be different short URLs
    short_url = models.CharField(max_length=30)
    click_time = models.IntegerField()

    def __str__(self):
        return f'{self.original_url.replace("https://", "")} Count of hit {str(self.click_time)} ' # For readable objects