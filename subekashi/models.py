from django.db import models


class Song(models.Model) :
    title = models.CharField(default = "", max_length = 500)
    channel = models.CharField(default = "", max_length = 500)
    url = models.CharField(default = "", max_length = 500, blank = True, null = True)
    lyrics = models.CharField(default = "", max_length = 10000, blank = True, null = True)
    imitate = models.CharField(default = "", max_length = 1000, blank = True, null = True)
    imitated = models.CharField(default = "", max_length = 1000, blank = True, null = True)
    posttime = models.DateTimeField(blank = True, null = True)
    uploaddata = models.DateField(blank = True, null = True)
    isoriginal = models.BooleanField(default = False)
    isjoke = models.BooleanField(default = False)
    isdeleted = models.BooleanField(default = False)
    isarchived = models.BooleanField(default = True)
    isdraft = models.BooleanField(default = False)
    isinst = models.BooleanField(default = False)
    issubeana = models.BooleanField(default = True)
    ip = models.CharField(default = "", max_length = 100)

    def __str__(self) :
        return self.title


class Channel(models.Model) :
    name = models.CharField(default = "", max_length = 100)
    ismain = models.BooleanField(default = True)
    isnickname = models.BooleanField(default = True)
    subs = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='main')

    def __str__(self) :
        return self.name
    

class Version(models.Model) :
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    before = models.CharField(default = "", max_length = 10000)
    after = models.CharField(default = "", max_length = 10000)
    editedtime = models.DateTimeField(blank = True, null = True)
    ip = models.CharField(default = "", max_length = 100)

class Ai(models.Model) :
    lyrics = models.CharField(default = "", max_length = 100)
    score = models.IntegerField(default = 0)
    genetype = models.CharField(default = "", max_length = 100)
    
    def __str__(self):
        return self.lyrics


class Ad(models.Model) :
    url = models.CharField(default = "", max_length = 100)
    view = models.IntegerField(default = 0)
    click = models.IntegerField(default = 0)
    dup = models.IntegerField(default = 0)
    isdisplay = models.BooleanField(default = False)
    
    def __str__(self):
        return self.url


class Singleton(models.Model) :
    key = models.CharField(default = "", max_length = 100)
    value = models.CharField(default = "", max_length = 500)