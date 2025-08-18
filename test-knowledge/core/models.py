from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

class Tag(models.Model):
    """标签模型，企微网盘标签和ragflow知识库标签的对应关系"""
    name = models.CharField(max_length=100, verbose_name="标签名称", unique=True)
    wecom_tag_id = models.CharField(max_length=100, verbose_name="企微标签ID", null=True, blank=True)
    ragflow_tag_id = models.CharField(max_length=100, verbose_name="Ragflow标签ID", null=True, blank=True)
    description = models.TextField(verbose_name="描述", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签管理"

class WecomFile(models.Model):
    """企微网盘文件模型"""
    FILE_TYPE_CHOICES = [
        ('doc', '文档'),
        ('image', '图片'),
        ('video', '视频'),
        ('audio', '音频'),
        ('other', '其他'),
    ]
    
    file_id = models.CharField(max_length=255, verbose_name="文件ID", unique=True)
    name = models.CharField(max_length=255, verbose_name="文件名")
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES, verbose_name="文件类型")
    size = models.BigIntegerField(verbose_name="文件大小(字节)")
    path = models.CharField(max_length=1000, verbose_name="企微路径")
    url = models.URLField(verbose_name="文件URL", blank=True)
    local_path = models.FileField(upload_to='wecom_files/', verbose_name="本地路径", blank=True)
    tags = models.ManyToManyField(Tag, related_name="wecom_files", verbose_name="标签")
    creator = models.CharField(max_length=100, verbose_name="创建者", blank=True)
    created_at = models.DateTimeField(verbose_name="创建时间", null=True, blank=True)
    synced_to_ragflow = models.BooleanField(default=False, verbose_name="已同步到Ragflow")
    sync_time = models.DateTimeField(null=True, blank=True, verbose_name="最后同步时间")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "企微文件"
        verbose_name_plural = "企微网盘文件"

class RagflowKnowledgeBase(models.Model):
    """Ragflow知识库模型"""
    kb_id = models.CharField(max_length=255, verbose_name="知识库ID", unique=True)
    name = models.CharField(max_length=255, verbose_name="知识库名称")
    description = models.TextField(verbose_name="描述", blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, related_name="ragflow_kb", verbose_name="关联标签")
    doc_count = models.IntegerField(verbose_name="文档数量", default=0)
    last_synced = models.DateTimeField(verbose_name="上次同步时间", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ragflow知识库"
        verbose_name_plural = "Ragflow知识库管理"

class SyncLog(models.Model):
    """同步日志记录"""
    LOG_TYPE_CHOICES = [
        ('wecom_import', '企微导入'),
        ('ragflow_import', 'Ragflow导入'),
        ('wecom_to_ragflow', '企微同步到Ragflow'),
    ]
    
    STATUS_CHOICES = [
        ('success', '成功'),
        ('failed', '失败'),
        ('partial', '部分成功'),
    ]
    
    log_type = models.CharField(max_length=20, choices=LOG_TYPE_CHOICES, verbose_name="日志类型")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="状态")
    details = models.TextField(verbose_name="详细信息", blank=True)
    items_processed = models.IntegerField(verbose_name="处理条目数", default=0)
    items_succeeded = models.IntegerField(verbose_name="成功条目数", default=0)
    items_failed = models.IntegerField(verbose_name="失败条目数", default=0)
    started_at = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="完成时间")
    
    def __str__(self):
        return f"{self.get_log_type_display()} - {self.started_at}"
    
    class Meta:
        verbose_name = "同步日志"
        verbose_name_plural = "同步日志记录" 