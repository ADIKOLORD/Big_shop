from django.contrib import admin, messages
from django.db.models import QuerySet

from .models import Product, Category, Customer, Comment, Review

# class ModelAdmin(admin.ModelAdmin):
'''
    fields -> Кайсы поляларды толтурганга болот. Же добавить эткенде кайсылар корунсун
    
    exclude -> Кайсы полялар добавить эткенде корунбосун
    
    readonly_fields -> Кайсыларды изменить этсе болбойт! 
    
    list_display -> Отображение на панеле
    
    list_display_links -> Переобразовать в ссылку
    
    search_fields -> Поиск болгондо кайсылардан издеш керек!
    
    list_editable -> Панелде сразу редактирование кылса болот
    
    list_filter -> Фильтр для отображения
    
    list_per_page -> Бир страницада канча запись болуш керек
    
    prepopulated_fields -> Ключ болуп турган поляга, значениеде турган полянын ичиндеги жазылат!

    actions -> Кайсы дествиялар болуш керек
    
    # Добавление дествии
    @admin.action(description='Отображение на панеле действии')
    def имя_что_делает(self, request, qs: QuerySet):
        pass

'''


class ProductAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # fields -> Кайсы поляларды толтурганга болот. Же добавить эткенде кайсылар корунсун
    ''
    # exclude -> Кайсы полялар добавить эткенде корунбосун
    exclude = []

    # readonly_fields -> Кайсыларды изменить этсе болбойт!
    readonly_fields = []

    # list_display -> Отображение на панеле
    list_display = ('title', 'new_price', 'category', 'watch')

    # prepopulated_fields -> Ключ болуп турган поляга, значениеде турган полянын ичиндеги жазылат!
    prepopulated_fields = {'description': ('title',)}

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['title', 'category']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('title', 'description')

    # list_editable -> Панелде сразу редактирование кылса болот
    # list_editable = ('price',)

    # list_filter -> Фильтр для отображения
    list_filter = ('category',)

    # list_per_page -> Бир страницада канча запись болуш керек
    list_per_page = 10

    # actions -> Кайсы дествиялар болуш керек
    actions = ['set_category_man',
               'set_category_woman',
               'set_category_sport',
               'set_category_electric',
               'set_clone_model',
               ]

    # Добавление дествии
    @admin.action(description='Установить категорию Sport')
    def set_category_sport(self, request, qs: QuerySet):
        count_updates = qs.update(category=3)
        # self.message_user -> Функция болгондо кандай сообщение чыгарына жооп берет.
        self.message_user(request,
                          f'Было обновлено {count_updates} записей',
                          # level -> INFO Записьти жашыл кылат, ERROR кызыл
                          level=messages.INFO
                          )

    @admin.action(description='Установить категорию Man')
    def set_category_man(self, request, qs: QuerySet):
        qs.update(category=1)

    @admin.action(description='Установить категорию Woman')
    def set_category_woman(self, request, qs: QuerySet):
        qs.update(category=2)

    @admin.action(description='Установить категорию Electric')
    def set_category_electric(self, request, qs: QuerySet):
        qs.update(category=4)

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)


class CustomerAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # list_display -> Отображение на панеле
    list_display = ('name', 'company')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['name', 'company']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('name', 'message')

    # list_editable -> Панелде сразу редактирование кылса болот

    # list_filter -> Фильтр для отображения


class CommentAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # list_display -> Отображение на панеле
    list_display = ('name', 'product')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['name', ]

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('name', 'website', 'comment')

    # list_editable -> Панелде сразу редактирование кылса болот

    # list_filter -> Фильтр для отображения


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Comment, CommentAdmin)


class ReviewAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # list_display -> Отображение на панеле
    list_display = ('name', 'rating', 'product')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['name']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('name', 'review')

    # list_editable -> Панелде сразу редактирование кылса болот
    list_editable = ('rating',)

    # list_filter -> Фильтр для отображения
    list_filter = ('rating',)

    # list_per_page -> Бир страницада канча запись болуш керек
    list_per_page = 10

    # actions -> Кайсы дествиялар болуш керек
    actions = [
        'set_rating_1',
        'set_rating_2',
        'set_rating_3',
        'set_rating_4',
        'set_rating_5',
        'set_clone_model',
    ]

    # Добавление дествии

    @admin.action(description='Установить рейтинг 1')
    def set_rating_1(self, request, qs: QuerySet):
        qs.update(rating=1)

    @admin.action(description='Установить рейтинг 2')
    def set_rating_2(self, request, qs: QuerySet):
        qs.update(rating=2)

    @admin.action(description='Установить рейтинг 3')
    def set_rating_3(self, request, qs: QuerySet):
        qs.update(rating=3)

    @admin.action(description='Установить рейтинг 4')
    def set_rating_4(self, request, qs: QuerySet):
        qs.update(rating=4)

    @admin.action(description='Установить рейтинг 5')
    def set_rating_5(self, request, qs: QuerySet):
        qs.update(rating=5)

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


admin.site.register(Review, ReviewAdmin)
