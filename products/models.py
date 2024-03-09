from django.db import models
from django.utils.translation import gettext as _

class Category(models.Model):
    parent =models.ForeignKey('self',verbose_name='parent', blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField (_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now=True)

    class Meta:
        db_table = 'categories'
        verbos_name = _('Category') # Show for admin
        verbos_name_plural = _('Categories')



class Products(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'products'
        verbos_name = _('product')
        verbos_name_plural = _'(products)'

class File(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='files')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('create time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update time'),auto_now=True)

    class Meta:
    db_table = 'files'
    verbos_name = _('file')
    verbos_name_plural = _('files')