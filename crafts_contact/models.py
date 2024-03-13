from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()

    def __str__(self):
        return self.name + " - " + self.subject
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #Send confirmation to user
        subject = "Thank you for getting in touch"
        html_message = render_to_string(
            "contact/contact_email.hmtl",
            {"name": self.name, "subject": self.subject},
        )
        plain_message = strip_tags(html_message)

        send_mail(
            subject=subject,
            message=plain_message,
            html_message=html_message,
            fail_silently=False,
            auth_user = 'Login',
            auth_password = 'Password',
        )

