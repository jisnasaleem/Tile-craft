from django.db import models

class pmodel(models.Model):
    iname = models.CharField(max_length=20)
    ccode = models.CharField(max_length=20)
    scode = models.CharField(max_length=20)
    bcode = models.CharField(max_length=20)
    desp = models.CharField(max_length=20)
    mrp = models.CharField(max_length=20)
    qty = models.CharField(max_length=20)
    p_image= models.FileField(upload_to='pictures')
    size = models.CharField(max_length=20)
    class Meta:
        db_table = "tbl_item"
