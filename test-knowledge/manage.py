#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knowledge_base.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入Django。请确保已安装Django，"
            "并且它在PYTHONPATH中。"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main() 