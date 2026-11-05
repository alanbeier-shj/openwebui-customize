"""Seed the default external resource directory."""

import time
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = '2a3b4c5d6e7f'
down_revision: Union[str, None] = '1f2e3d4c5b6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


DEFAULT_RESOURCES = [
    {
        'id': 'qwenpaw',
        'name': 'QwenPaw 智能体平台',
        'description': '资源消耗较大，请联系管理员开通账号后使用。',
        'icon': '🤖',
        'category': '智能体平台',
        'action_type': 'apply',
        'url': 'https://example.com/qwenpaw/login',
        'contact_name': '平台管理员',
        'contact_method': '企业微信',
        'contact_value': 'example-contact',
        'manual_url': 'https://example.com/qwenpaw/manual',
        'sort_order': 10,
    },
    {
        'id': 'deepseek-harness',
        'name': 'DeepSeek Harness 终端智能体平台',
        'description': '下载安装包后到本地自行安装使用。',
        'icon': '🖥️',
        'category': '终端智能体',
        'action_type': 'download',
        'url': 'https://example.com/deepseek-harness/setup.zip',
        'manual_url': 'https://example.com/deepseek-harness/manual',
        'sort_order': 20,
    },
    {
        'id': 'fastgpt',
        'name': 'FastGPT 网站',
        'description': '点击前往官网注册并登录使用。',
        'icon': '⚡',
        'category': '大模型平台',
        'action_type': 'open_url',
        'url': 'https://example.com/fastgpt',
        'manual_url': 'https://example.com/fastgpt/manual',
        'sort_order': 30,
    },
    {
        'id': 'md2word',
        'name': 'Markdown 转 Word 工具',
        'description': '在线将 Markdown 文档转换为 Word。',
        'icon': '📝',
        'category': '文档工具',
        'action_type': 'open_url',
        'url': 'https://example.com/tools/md-to-word',
        'sort_order': 40,
    },
    {
        'id': 'word2md',
        'name': 'Word 转 Markdown 工具',
        'description': '在线将 Word 文档转换为 Markdown。',
        'icon': '📄',
        'category': '文档工具',
        'action_type': 'open_url',
        'url': 'https://example.com/tools/word-to-md',
        'sort_order': 50,
    },
    {
        'id': 'ppt-translate',
        'name': 'PPT 翻译工具',
        'description': '上传 PPT 文件进行翻译。',
        'icon': '🌐',
        'category': '文档工具',
        'action_type': 'open_url',
        'url': 'https://example.com/tools/ppt-translate',
        'sort_order': 60,
    },
    {
        'id': 'ai-ppt',
        'name': 'AI PPT 制作工具',
        'description': '使用 AI 快速生成演示文稿。',
        'icon': '🎨',
        'category': '演示工具',
        'action_type': 'open_url',
        'url': 'https://example.com/tools/ai-ppt',
        'manual_url': 'https://example.com/tools/ai-ppt/manual',
        'sort_order': 70,
    },
]


def upgrade():
    conn = op.get_bind()
    count = conn.execute(sa.text('SELECT COUNT(*) FROM external_resource')).scalar()
    if count:
        return

    table = sa.table(
        'external_resource',
        sa.column('id', sa.Text()),
        sa.column('name', sa.Text()),
        sa.column('description', sa.Text()),
        sa.column('icon', sa.Text()),
        sa.column('category', sa.Text()),
        sa.column('action_type', sa.Text()),
        sa.column('url', sa.Text()),
        sa.column('contact_name', sa.Text()),
        sa.column('contact_method', sa.Text()),
        sa.column('contact_value', sa.Text()),
        sa.column('manual_url', sa.Text()),
        sa.column('enabled', sa.Boolean()),
        sa.column('sort_order', sa.Integer()),
        sa.column('created_at', sa.BigInteger()),
        sa.column('updated_at', sa.BigInteger()),
    )

    now = int(time.time())
    rows = [
        {
            **item,
            'description': item.get('description'),
            'contact_name': item.get('contact_name'),
            'contact_method': item.get('contact_method'),
            'contact_value': item.get('contact_value'),
            'manual_url': item.get('manual_url'),
            'enabled': True,
            'created_at': now,
            'updated_at': now,
        }
        for item in DEFAULT_RESOURCES
    ]
    conn.execute(sa.insert(table), rows)


def downgrade():
    conn = op.get_bind()
    conn.execute(sa.text("DELETE FROM external_resource WHERE id IN ('qwenpaw', 'deepseek-harness', 'fastgpt', 'md2word', 'word2md', 'ppt-translate', 'ai-ppt')"))
