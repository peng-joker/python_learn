import os
import datetime
import requests
import logging
from django.utils import timezone
from django.conf import settings
from ..models import RagflowKnowledgeBase, Tag, WecomFile, SyncLog

logger = logging.getLogger(__name__)

def get_ragflow_api_key():
    """获取RagFlow API密钥"""
    return os.environ.get('RAGFLOW_API_KEY', '')

def fetch_ragflow_knowledge_bases():
    """从RagFlow获取知识库列表（示例实现）"""
    # 实际开发中需替换为真实的RagFlow API调用
    api_key = get_ragflow_api_key()
    if not api_key:
        logger.error("RagFlow API配置缺失")
        return []
    
    try:
        # 模拟数据，实际项目中应调用真实API
        sample_kbs = [
            {
                'kb_id': 'kb1',
                'name': '公司资料库',
                'description': '包含公司介绍、组织架构等基本资料',
                'doc_count': 15,
                'tag': '公司资料'
            },
            {
                'kb_id': 'kb2',
                'name': '产品知识库',
                'description': '包含产品说明、规格、路线图等',
                'doc_count': 28,
                'tag': '产品'
            }
        ]
        return sample_kbs
    except Exception as e:
        logger.exception(f"获取RagFlow知识库异常: {str(e)}")
        return []

def sync_ragflow_kb():
    """同步RagFlow知识库到系统"""
    log_entry = SyncLog.objects.create(
        log_type='ragflow_import',
        status='failed',  # 初始状态为失败，后续更新
        started_at=timezone.now()
    )
    
    try:
        # 获取RagFlow知识库
        knowledge_bases = fetch_ragflow_knowledge_bases()
        
        imported = 0
        updated = 0
        failed = 0
        
        for kb_data in knowledge_bases:
            try:
                # 处理标签
                tag_name = kb_data.pop('tag', None)
                tag = None
                if tag_name:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                
                # 创建或更新知识库记录
                kb_obj, created = RagflowKnowledgeBase.objects.update_or_create(
                    kb_id=kb_data['kb_id'],
                    defaults={
                        'name': kb_data['name'],
                        'description': kb_data.get('description', ''),
                        'doc_count': kb_data.get('doc_count', 0),
                        'tag': tag,
                        'last_synced': timezone.now()
                    }
                )
                
                if created:
                    imported += 1
                else:
                    updated += 1
                    
            except Exception as e:
                logger.exception(f"处理知识库记录失败: {str(e)}")
                failed += 1
        
        # 更新日志
        log_entry.status = 'success' if failed == 0 else 'partial'
        log_entry.items_processed = len(knowledge_bases)
        log_entry.items_succeeded = imported + updated
        log_entry.items_failed = failed
        log_entry.details = f"导入: {imported}, 更新: {updated}, 失败: {failed}"
        log_entry.completed_at = timezone.now()
        log_entry.save()
        
        return {'imported': imported, 'updated': updated, 'failed': failed}
        
    except Exception as e:
        logger.exception(f"同步RagFlow知识库异常: {str(e)}")
        log_entry.status = 'failed'
        log_entry.details = f"同步过程中发生异常: {str(e)}"
        log_entry.completed_at = timezone.now()
        log_entry.save()
        return {'imported': 0, 'updated': 0, 'failed': 0}

def upload_file_to_ragflow(file_obj, kb_id):
    """上传文件到RagFlow知识库（示例实现）"""
    # 实际开发中需替换为真实的RagFlow API调用
    api_key = get_ragflow_api_key()
    if not api_key:
        logger.error("RagFlow API配置缺失")
        return False
    
    try:
        # 此处应该是实际的API调用实现
        # 模拟上传成功
        logger.info(f"模拟上传文件 {file_obj.name} 到知识库 {kb_id}")
        return True
    except Exception as e:
        logger.exception(f"上传文件到RagFlow异常: {str(e)}")
        return False

def sync_files_to_ragflow(files_queryset):
    """将企微网盘文件同步到RagFlow知识库"""
    log_entry = SyncLog.objects.create(
        log_type='wecom_to_ragflow',
        status='failed',  # 初始状态为失败，后续更新
        started_at=timezone.now()
    )
    
    try:
        total = files_queryset.count()
        success = 0
        failed = 0
        
        for file_obj in files_queryset:
            # 获取文件标签关联的知识库
            kb_list = []
            for tag in file_obj.tags.all():
                kb = RagflowKnowledgeBase.objects.filter(tag=tag).first()
                if kb:
                    kb_list.append(kb)
            
            if not kb_list:
                logger.warning(f"文件 {file_obj.name} 没有关联的知识库")
                failed += 1
                continue
            
            file_success = True
            # 同步到每个关联的知识库
            for kb in kb_list:
                result = upload_file_to_ragflow(file_obj, kb.kb_id)
                if not result:
                    file_success = False
                    logger.error(f"文件 {file_obj.name} 同步到知识库 {kb.name} 失败")
            
            if file_success:
                file_obj.synced_to_ragflow = True
                file_obj.sync_time = timezone.now()
                file_obj.save()
                success += 1
            else:
                failed += 1
        
        # 更新日志
        log_entry.status = 'success' if failed == 0 else 'partial'
        log_entry.items_processed = total
        log_entry.items_succeeded = success
        log_entry.items_failed = failed
        log_entry.details = f"成功: {success}, 失败: {failed}"
        log_entry.completed_at = timezone.now()
        log_entry.save()
        
        return {'total': total, 'success': success, 'failed': failed}
        
    except Exception as e:
        logger.exception(f"同步文件到RagFlow异常: {str(e)}")
        log_entry.status = 'failed'
        log_entry.details = f"同步过程中发生异常: {str(e)}"
        log_entry.completed_at = timezone.now()
        log_entry.save()
        return {'total': 0, 'success': 0, 'failed': 0} 