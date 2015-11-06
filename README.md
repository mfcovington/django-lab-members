# Lab Members

Lab Members is a Django app to display lab personnel and information about them.

<!-- Detailed documentation is in the "docs" directory. -->

## Quick start

- Edit the project's `settings.py` file.

    - Add `lab_members` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'lab_members',
            'easy_thumbnails',
            'filer',
            'mptt',
            'sekizai',
            'friendlytagloader',
        )
        ```

    - Specify your media settings, if not already specified:

        ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

    - Add `easy_thumbnail` settings: 

        ```python
        # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
        THUMBNAIL_HIGH_RESOLUTION = True
        THUMBNAIL_QUALITY = 95
        THUMBNAIL_PROCESSORS = (
            'easy_thumbnails.processors.colorspace',
            'easy_thumbnails.processors.autocrop',
            'filer.thumbnail_processors.scale_and_crop_with_subject_location',
            'easy_thumbnails.processors.filters',
        )
        THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
        THUMBNAIL_SUBDIR = 'versions'
        ```

    - Add `sekizai` settings:

        - For **Django 1.7**, add `sekizai.context_processors.sekizai` to `TEMPLATE_CONTEXT_PROCESSORS`:

            ```python
            from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
            TEMPLATE_CONTEXT_PROCESSORS += ('sekizai.context_processors.sekizai',)
            ```

        - For **Django 1.8**, add `sekizai.context_processors.sekizai` to `TEMPLATES`:

            ```python
            TEMPLATES = [
                {
                    ...
                    'OPTIONS': {
                        'context_processors': [
                            ...
                            'sekizai.context_processors.sekizai',
                        ],
                    },
                },
            ]
            ```

- Include URL configurations for `lab_members` and media (if `DEBUG == True`) in your project's `urls.py` file:

    - For **Django 1.7**:

        ```python
        ...
        from django.conf import settings

        urlpatterns = patterns('',
            ...
            url(r'^lab_members/', include('lab_members.urls', namespace='lab_members')),
            ...
        )

        if settings.DEBUG:
            urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT}))
        ```
        
    - For **Django 1.8**:

        ```python
        ...
        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = patterns('',
            ...
            url(r'^lab_members/', include('lab_members.urls', namespace='lab_members')),
            ...
        )

        if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```


- Run `python manage.py makemigrations lab_members` to create the lab_members migrations.

- Run `python manage.py migrate` to create the lab_members models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/admin/
   to create a lab member (you'll need the Admin app enabled).

- Visit http://127.0.0.1:8000/lab_members/ to view a list of lab members.

*Version 0.2.5*
