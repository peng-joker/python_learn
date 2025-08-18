import os
import datetime
import requests
import logging
from django.utils import timezone
from django.conf import settings
from ..models import WecomFile, Tag, SyncLog

logger = logging.getLogger(__name__)

def get_wecom_access_token():
    """获取企业微信访问令牌（示例实现）"""
    # 实际开发中需替换为真实的企业微信API调用
    # 此处仅为示例
    corpid = os.environ.get('WECOM_CORPID', '')
    corpsecret = os.environ.get('WECOM_CORPSECRET', '')
    
    if not corpid or not corpsecret:
        logger.error("企业微信配置缺失")
        return None
    
    try:
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        response = requests.get(url)
        data = response.json()
        
        if data.get('errcode') == 0:
            return data.get('access_token')
        else:
            logger.error(f"获取企业微信令牌失败: {data.get('errmsg')}")
            return None
    except Exception as e:
        logger.exception(f"获取企业微信令牌异常: {str(e)}")
        return None

def fetch_wecom_files(access_token=None):
    """从企业微信获取文件列表（示例实现）"""
    # 实际开发中需替换为真实的企业微信API调用
    # 此处仅为模拟数据
    if access_token is None:
        access_token = get_wecom_access_token()
        if not access_token:
            return []
    
    try:
        # 模拟数据，实际项目中应调用真实API
        sample_files = [
            {
                'file_id': 'file1',
                'name': '公司介绍.docx',
                'file_type': 'doc',
                'size': 1024 * 1024,
                'path': '/公司资料/公司介绍.docx',
                'url': 'https://example.com/files/intro.docx',
                'creator': '张三',
                'created_at': timezone.now() - datetime.timedelta(days=10),
                'tags': ['公司资料', '介绍']
            },
            {
                'file_id': 'file2',
                'name': '产品路线图.pdf',
                'file_type': 'doc',
                'size': 2 * 1024 * 1024,
                'path': '/产品/产品路线图.pdf',
                'url': 'https://example.com/files/roadmap.pdf',
                'creator': '李四',
                'created_at': timezone.now() - datetime.timedelta(days=5),
                'tags': ['产品', '规划']
            }
        ]
        return sample_files
    except Exception as e:
        logger.exception(f"获取企业微信文件异常: {str(e)}")
        return []

def sync_wecom_files():
    """同步企业微信网盘文件到系统"""
    log_entry = SyncLog.objects.create(
        log_type='wecom_import',
        status='failed',  # 初始状态为失败，后续更新
        started_at=timezone.now()
    )
    
    try:
        # 获取访问令牌
        access_token = get_wecom_access_token()
        if not access_token:
            log_entry.details = "获取企业微信访问令牌失败"
            log_entry.completed_at = timezone.now()
            log_entry.save()
            return {'imported': 0, 'updated': 0, 'failed': 0}
        
        # 获取企业微信文件
        files = fetch_wecom_files(access_token)
        
        imported = 0
        updated = 0
        failed = 0
        
        for file_data in files:
            try:
                # 处理标签
                tag_names = file_data.pop('tags', [])
                tags = []
                for tag_name in tag_names:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    tags.append(tag)
                
                # 创建或更新文件记录
                file_obj, created = WecomFile.objects.update_or_create(
                    file_id=file_data['file_id'],
                    defaults={
                        'name': file_data['name'],
                        'file_type': file_data['file_type'],
                        'size': file_data['size'],
                        'path': file_data['path'],
                        'url': file_data.get('url', ''),
                        'creator': file_data.get('creator', ''),
                        'created_at': file_data.get('created_at', timezone.now()),
                    }
                )
                
                # 设置标签
                file_obj.tags.set(tags)
                
                if created:
                    imported += 1
                else:
                    updated += 1
                    
            except Exception as e:
                logger.exception(f"处理文件记录失败: {str(e)}")
                failed += 1
        
        # 更新日志
        log_entry.status = 'success' if failed == 0 else 'partial'
        log_entry.items_processed = len(files)
        log_entry.items_succeeded = imported + updated
        log_entry.items_failed = failed
        log_entry.details = f"导入: {imported}, 更新: {updated}, 失败: {failed}"
        log_entry.completed_at = timezone.now()
        log_entry.save()
        
        return {'imported': imported, 'updated': updated, 'failed': failed}
        
    except Exception as e:
        logger.exception(f"同步企业微信文件异常: {str(e)}")
        log_entry.status = 'failed'
        log_entry.details = f"同步过程中发生异常: {str(e)}"
        log_entry.completed_at = timezone.now()
        log_entry.save()
        return {'imported': 0, 'updated': 0, 'failed': 0} 