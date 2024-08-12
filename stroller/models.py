from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Stroller(models.Model):
    model_name = models.CharField(max_length=30, unique=True, verbose_name="Назва моделі")
    title_name = models.CharField(max_length=150, verbose_name="Назва заголовку")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Не редагувати!")
    description = RichTextField()

    is_featured = models.BooleanField(default=False)
    featured_photo = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    featured_description = models.CharField(max_length=120, blank=True, null=True)

    title_image = models.ImageField(upload_to='stroller_photo', blank=True, null=True)

    stroller_photo_1 = models.ImageField(upload_to='stroller_photo')
    stroller_photo_2 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    stroller_photo_3 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    stroller_photo_4 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    stroller_photo_5 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    stroller_photo_6 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    stroller_photo_7 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)
    stroller_photo_8 = models.ImageField(upload_to='stroller_photo', blank=True, null=True)

    stroller_color_1 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_2 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_3 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_4 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_5 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_6 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_7 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_8 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_9 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_10 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_11 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_12 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_13 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_14 = models.ImageField(upload_to='stroller_color', blank=True, null=True)
    stroller_color_15 = models.ImageField(upload_to='stroller_color', blank=True, null=True)

    features = RichTextField()
    weight_cradle = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Вага люльки")
    weight_walking_unit = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                              verbose_name="Вага прогулянкового блоку")
    weight_frame_with_wheels = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                                   verbose_name="Вага рами з колесами")
    width_frame = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Ширина рами")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редагування")
    sized_stroller = models.ImageField(upload_to='stroller_photo', blank=True, null=True,
                                       verbose_name="Фото коляски з розмірами")

    header_first = models.CharField(max_length=150, blank=True, null=True, verbose_name='Перший заголовок опису')
    description_first = RichTextField(verbose_name="Перший опис", blank=True, null=True)
    photo_first = models.ImageField(upload_to='stroller_photo', blank=True, null=True, verbose_name="Перше фото опису")
    header_second = models.CharField(max_length=150, blank=True, null=True, verbose_name='Другий заголовок опису')
    description_second = RichTextField(verbose_name="Другий опис", blank=True, null=True)
    photo_second = models.ImageField(upload_to='stroller_photo', blank=True, null=True, verbose_name="Друге фото опису")
    header_third = models.CharField(max_length=150, blank=True, null=True, verbose_name='Третій заголовок опису')
    description_third = RichTextField(verbose_name="Третій опис", blank=True, null=True)
    photo_third = models.ImageField(upload_to='stroller_photo', blank=True, null=True, verbose_name="Третє фото опису")
    header_fourth = models.CharField(max_length=150, blank=True, null=True, verbose_name='Четвертий заголовок опису')
    description_fourth = RichTextField(verbose_name="Четвертий опис", blank=True, null=True)
    photo_fourth = models.ImageField(upload_to='stroller_photo', blank=True, null=True,
                                     verbose_name="Четверте фото опису")

    gallery_photo_1 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_2 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_3 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_4 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_5 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_6 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_7 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")
    gallery_photo_8 = models.ImageField(upload_to='gallety_photo', blank=True, null=True,
                                        verbose_name="Фото для галереї")

    class Meta:
        verbose_name = 'Коляски'
        verbose_name_plural = 'Коляски'
        ordering = ['-updated_at']

    def __str__(self):
        return self.model_name

    def get_absolute_url(self):
        return reverse('catalog:stroller_detail', args=[self.slug])


