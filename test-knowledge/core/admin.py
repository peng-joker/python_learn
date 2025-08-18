from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Tag, WecomFile, RagflowKnowledgeBase, SyncLog
from .services.wecom_sync import sync_wecom_files
from .services.ragflow_sync import sync_ragflow_kb, sync_files_to_ragflow

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'wecom_tag_id', 'ragflow_tag_id', 'file_count', 'kb_name')
    search_fields = ('name', 'wecom_tag_id', 'ragflow_tag_id')
    list_filter = ('created_at',)
    
    def file_count(self, obj):
        return obj.wecom_files.count()
    file_count.short_description = "企微文件数"
    
    def kb_name(self, obj):
        kb = obj.ragflow_kb.first()
        if kb:
            return kb.name
        return "-"
    kb_name.short_description = "关联知识库"

class TagListFilter(admin.SimpleListFilter):
    title = '标签'
    parameter_name = 'tag'
    
    def lookups(self, request, model_admin):
        tags = Tag.objects.all()
        return [(tag.id, tag.name) for tag in tags]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tags__id=self.value())
        return queryset

@admin.register(WecomFile)
class WecomFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_type', 'size_display', 'creator', 'created_at', 'tag_list', 'synced_status')
    list_filter = ('file_type', TagListFilter, 'synced_to_ragflow')
    search_fields = ('name', 'file_id', 'creator')
    filter_horizontal = ('tags',)
    readonly_fields = ('file_id', 'size', 'created_at', 'sync_time')
    actions = ['sync_selected_to_ragflow']
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
    def size_display(self, obj):
        """将文件大小转换为可读格式"""
        size = obj.size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024 or unit == 'GB':
                return f"{size:.2f} {unit}"
            size /= 1024
    size_display.short_description = "文件大小"
    
    def tag_list(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    tag_list.short_description = "标签"
    
    def synced_status(self, obj):
        if obj.synced_to_ragflow:
            return format_html('<span style="color:green;">已同步</span>')
        return format_html('<span style="color:red;">未同步</span>')
    synced_status.short_description = "同步状态"
    
    def sync_selected_to_ragflow(self, request, queryset):
        result = sync_files_to_ragflow(queryset)
        self.message_user(request, f"已处理 {result['total']} 个文件，成功：{result['success']}，失败：{result['failed']}")
    sync_selected_to_ragflow.short_description = "将选中文件同步到Ragflow"

@admin.register(RagflowKnowledgeBase)
class RagflowKnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'kb_id', 'tag_name', 'doc_count', 'last_synced')
    search_fields = ('name', 'kb_id')
    list_filter = ('last_synced',)
    
    def tag_name(self, obj):
        if obj.tag:
            return obj.tag.name
        return "-"
    tag_name.short_description = "关联标签"

@admin.register(SyncLog)
class SyncAdmin(admin.ModelAdmin):
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('sync_wecom/', self.sync_wecom_view, name='sync_wecom'),
            path('sync_ragflow/', self.sync_ragflow_view, name='sync_ragflow'),
            path('sync_to_ragflow/', self.sync_to_ragflow_view, name='sync_to_ragflow'),
        ]
        return my_urls + urls
    
    def sync_wecom_view(self, request):
        result = sync_wecom_files()
        self.message_user(request, f"企微文件同步完成。导入：{result['imported']}，更新：{result['updated']}，失败：{result['failed']}")
        return HttpResponseRedirect(reverse('admin:index'))
        
    def sync_ragflow_view(self, request):
        result = sync_ragflow_kb()
        self.message_user(request, f"Ragflow知识库同步完成。导入：{result['imported']}，更新：{result['updated']}，失败：{result['failed']}")
        return HttpResponseRedirect(reverse('admin:index'))
        
    def sync_to_ragflow_view(self, request):
        files = WecomFile.objects.filter(tags__isnull=False, synced_to_ragflow=False)
        result = sync_files_to_ragflow(files)
        self.message_user(request, f"文件同步到Ragflow完成。处理：{result['total']}，成功：{result['success']}，失败：{result['failed']}")
        return HttpResponseRedirect(reverse('admin:index'))

    list_display = ('log_type_display', 'status', 'started_at', 'completed_at', 'success_rate')
    list_filter = ('log_type', 'status')
    readonly_fields = ('log_type', 'status', 'details', 'items_processed', 
                      'items_succeeded', 'items_failed', 'started_at', 'completed_at')
    
    def log_type_display(self, obj):
        return obj.get_log_type_display()
    log_type_display.short_description = "同步类型"
    
    def success_rate(self, obj):
        if obj.items_processed == 0:
            return "0%"
        rate = (obj.items_succeeded / obj.items_processed) * 100
        return f"{rate:.1f}%"
    success_rate.short_description = "成功率"

# 自定义Admin站点
admin.site.site_header = "公司知识库管理系统"
admin.site.site_title = "知识库管理"
admin.site.index_title = "管理控制台" 