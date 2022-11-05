from django.db import models


class Advocate(models.Model):
  username = models.CharField(max_length=100, unique=True)
  name = models.CharField(max_length=50, null=False, blank=False)
  profile_pic = models.ImageField(upload_to="advocates", default="avatar.png")
  short_bio = models.CharField(max_length=250, null=False, blank=False)
  long_bio = models.TextField(blank=False, null=False)
  advocate_years_exp = models.IntegerField(null=False, blank=False)
  company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="advocate_of_a_company")
  youtube = models.URLField(null=True, blank=True)
  twitter = models.URLField(null=True, blank=True)
  github = models.URLField(null=True, blank=True)
  linkedin = models.URLField(null=True, blank=True)
  website = models.URLField(null=True, blank=True)
  # url = models.CharField(max_length=200, null=True, blank=True)
  
  class Meta:
    ordering = ["id"]

  def __str__(self):
    return self.name
  
  @property
  def set_links(self):
    link_dict = {}
    if self.youtube:
      link_dict.update({"youtube": self.youtube})
    if self.twitter:
      link_dict.update({"twitter": self.twitter})
    if self.github:
      link_dict.update({"github": self.github})
    if self.linkedin:
      link_dict.update({"linkedin": self.linkedin})
    if self.website:
      link_dict.update({"website": self.website})
    return link_dict  

class Company(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False)
  logo = models.ImageField(upload_to="companies", default="avatar.png")
  summary = models.TextField(blank=False, null=False)
  # url = models.CharField(max_length=200, null=True, blank=True)
  advocates = models.ManyToManyField(Advocate, related_name="companies_advocates", blank=True)
  
  youtube = models.URLField(null=True, blank=True)
  twitter = models.URLField(null=True, blank=True)
  github = models.URLField(null=True, blank=True)
  linkedin = models.URLField(null=True, blank=True)
  website = models.URLField(null=True, blank=True)
  
  class Meta:
    ordering = ["id"]
  

  def __str__(self):
    return self.name

  @property
  def set_links(self):
    link_dict = {}
    if self.youtube:
      link_dict.update({"youtube": self.youtube})
    if self.twitter:
      link_dict.update({"twitter": self.twitter})
    if self.github:
      link_dict.update({"github": self.github})
    if self.linkedin:
      link_dict.update({"linkedin": self.linkedin})
    if self.website:
      link_dict.update({"website": self.website})
    return link_dict  