from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .services.wecom_sync import sync_wecom_files
from .services.ragflow_sync import sync_ragflow_kb, sync_files_to_ragflow
from .models import WecomFile

def index(request):
    """首页重定向到管理页面"""
    return redirect('admin:index')

@login_required
@csrf_exempt
def sync_wecom_api(request):
    """API接口: 同步企微网盘文件"""
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)
    
    if not request.user.is_staff:
        return JsonResponse({'error': '权限不足'}, status=403)
    
    result = sync_wecom_files()
    
    return JsonResponse({
        'success': True,
        'imported': result['imported'],
        'updated': result['updated'],
        'failed': result['failed']
    })

@login_required
@csrf_exempt
def sync_ragflow_api(request):
    """API接口: 同步RagFlow知识库"""
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)
    
    if not request.user.is_staff:
        return JsonResponse({'error': '权限不足'}, status=403)
    
    result = sync_ragflow_kb()
    
    return JsonResponse({
        'success': True,
        'imported': result['imported'],
        'updated': result['updated'],
        'failed': result['failed']
    })

@login_required
@csrf_exempt
def sync_to_ragflow_api(request):
    """API接口: 同步文件到RagFlow"""
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持POST请求'}, status=405)
    
    if not request.user.is_staff:
        return JsonResponse({'error': '权限不足'}, status=403)
    
    files = WecomFile.objects.filter(tags__isnull=False, synced_to_ragflow=False)
    result = sync_files_to_ragflow(files)
    
    return JsonResponse({
        'success': True,
        'total': result['total'],
        'success': result['success'],
        'failed': result['failed']
    }) 