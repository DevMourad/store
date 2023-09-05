from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin


admin.site.site_header = 'لوحة التحكم'
admin.site.site_title = 'لوحة التحكم'
msg = 'عذرًا، هذه النسخة مخصصة للتجربة فقط. لا يُسمح لك بإضافة أو تعديل أو حذف أي شيء في هذه النسخة.'


class CartProductInline(admin.TabularInline):
    model = CartProduct

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(User)
class UsAdmin(ImportExportModelAdmin, UserAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        response = super(UsAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(UsAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(UsAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(UsAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(SettingSite)
class SettingSiteAdmin(ImportExportModelAdmin):
    list_display = ['pk', 'site_title', 'phone', 'email']
    fieldsets = [
        ('معلومات الموقع', {
            'fields': ['site_title', 'site_name', 'description', 'keywords', 'currency', 'color'],
        }),
        ('الصور والرموز', {
            'fields': ['icon', 'logo', 'main_image', 'about_us_image'],
        }),
        ('معلومات التواصل', {
            'fields': ['address', 'phone', 'email', 'whatsapp', 'instagram', 'facebook', 'phone_feature',],
        }),
        ('صفحة استلام الطلبية', {
            'fields': ['imogie', 'contact_section', 'end_order', 'created_on'],
        }),
    ]
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


    def response_add(self, request, obj, post_url_continue=None):
        response = super(SettingSiteAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(SettingSiteAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))
    
@admin.register(Constants)
class ContstantsAdmin(ImportExportModelAdmin):
    list_display = ['pk', 'about_us_title', 'subscription_title', 'title_products']
    fieldsets = (
        (' قسم من نحن', {
            'fields': ('about_us_title', 'about_us_content'),
        }),
        ('عناوين متنوعة', {
            'fields': ('subscription_title', 'title_products', 'title_special_products', 'title_lists', 'title_footer'),
        }),
        ('عناوين صفحة الاتصال', {
            'fields': ('contact_title', 'contact_form_title')}),
        
        ('عناوين صفحة استلام الطلبية', {
            'fields': ('command_title', 'command_details', 'contact_note', 'phone_button'),
        }),
        ('عناوين صفحة تأكيد الطلبية', {
            'fields': ('checkout_title', 'checkout_button', 'created_on'),
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


    def response_add(self, request, obj, post_url_continue=None):
        response = super(ContstantsAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(ContstantsAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))
    

@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name', 'phone', 'subject')
    search_fields = ['name', 'phone', 'subject']
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(MessageAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(MessageAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(MessageAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(MessageAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(Subscription)
class SubscriptionAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name', 'phone', 'created_on')
    search_fields = ['name', 'phone']
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(SubscriptionAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(SubscriptionAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(SubscriptionAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(SubscriptionAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('pk', 'name', 'price', 'created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(ProductAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(ProductAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(ProductAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(ProductAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(BigProduct)
class BigProductAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'product', 'created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(BigProductAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(BigProductAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(BigProductAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(BigProductAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(ListProducts)
class ListProductsAdmin(ImportExportModelAdmin):
    search_fields = ['title']
    list_display = ('pk', 'title', 'created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(ListProductsAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(ListProductsAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(ListProductsAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(ListProductsAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(Features)
class FeaturesAdmin(ImportExportModelAdmin):
    search_fields = ['title', 'icon']
    list_display = ('pk', 'title', 'icon','created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(FeaturesAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(FeaturesAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(FeaturesAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(FeaturesAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(ProductType)
class ProductTypeAdmin(ImportExportModelAdmin):
    search_fields = ['name']
    list_display = ('pk', 'name', 'created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(ProductTypeAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(ProductTypeAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(ProductTypeAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(ProductTypeAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(CartProduct)
class CartProductAdmin(ImportExportModelAdmin):
    search_fields = ['product']
    list_display = ('pk', 'product', 'order', 'quantity', 'created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(CartProductAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(CartProductAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(CartProductAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(CartProductAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(Shipping)
class ShippingAdmin(ImportExportModelAdmin):
    search_fields = ['city', 'price']
    list_display = ('pk', 'city', 'price', 'created_on')
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(ShippingAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(ShippingAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(ShippingAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(ShippingAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    search_fields = ['customer', 'city', 'state']
    list_display = ('pk', 'customer', 'state', 'city', 'phone_number',  'address', 'created_on')
    inlines = [CartProductInline]
    
    def response_add(self, request, obj, post_url_continue=None):
        response = super(OrderAdmin, self).response_add(request, obj, post_url_continue)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_delete(self, request, obj_display, obj_id):
        response = super(OrderAdmin, self).response_delete(request, obj_display, obj_id)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def response_action(self, request, queryset):
        response = super(OrderAdmin, self).response_action(request, queryset)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        if len(s._queued_messages) > 0:
            s._queued_messages = [s._queued_messages[0]]
        return response

    def response_change(self, request, obj):
        response = super(OrderAdmin, self).response_change(request, obj)
        s = messages.get_messages(request)
        s.storages = [s.storages[0]]
        s._queued_messages = [s._queued_messages[0]]
        return response

    def delete_model(self, request, obj):
        messages.error(request, (msg))

    def delete_queryset(self, request, queryset):
        messages.error(request, (msg))

    def save_model(self, request, obj, form, change):
        messages.error(request, (msg))
