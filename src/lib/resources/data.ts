import type { Resource } from './types';

// 资源中心配置（方案 B：静态配置）。
// 管理员在这里维护资源；后续升级到方案 A 时，这份数据会迁移到后端并由管理界面在线维护。
export const staticResources: Resource[] = [
	{
		id: 'qwenpaw',
		name: 'QwenPaw 智能体平台',
		description: '资源消耗较大，请联系管理员开通账号后使用。',
		icon: '🤖',
		category: '智能体平台',
		action_type: 'apply',
		url: 'https://example.com/qwenpaw/login',
		contact_name: '平台管理员',
		contact_method: '企业微信',
		contact_value: 'example-contact',
		manual_url: 'https://example.com/qwenpaw/manual',
		enabled: true,
		sort_order: 10
	},
	{
		id: 'deepseek-harness',
		name: 'DeepSeek Harness 终端智能体平台',
		description: '下载安装包后到本地自行安装使用。',
		icon: '🖥️',
		category: '终端智能体',
		action_type: 'download',
		url: 'https://example.com/deepseek-harness/setup.zip',
		manual_url: 'https://example.com/deepseek-harness/manual',
		enabled: true,
		sort_order: 20
	},
	{
		id: 'fastgpt',
		name: 'FastGPT 网站',
		description: '点击前往官网注册并登录使用。',
		icon: '⚡',
		category: '大模型平台',
		action_type: 'open_url',
		url: 'https://example.com/fastgpt',
		manual_url: 'https://example.com/fastgpt/manual',
		enabled: true,
		sort_order: 30
	},
	{
		id: 'md2word',
		name: 'Markdown 转 Word 工具',
		description: '在线将 Markdown 文档转换为 Word。',
		icon: '📝',
		category: '文档工具',
		action_type: 'open_url',
		url: 'https://example.com/tools/md-to-word',
		enabled: true,
		sort_order: 40
	},
	{
		id: 'word2md',
		name: 'Word 转 Markdown 工具',
		description: '在线将 Word 文档转换为 Markdown。',
		icon: '📄',
		category: '文档工具',
		action_type: 'open_url',
		url: 'https://example.com/tools/word-to-md',
		enabled: true,
		sort_order: 50
	},
	{
		id: 'ppt-translate',
		name: 'PPT 翻译工具',
		description: '上传 PPT 文件进行翻译。',
		icon: '🌐',
		category: '文档工具',
		action_type: 'open_url',
		url: 'https://example.com/tools/ppt-translate',
		enabled: true,
		sort_order: 60
	},
	{
		id: 'ai-ppt',
		name: 'AI PPT 制作工具',
		description: '使用 AI 快速生成演示文稿。',
		icon: '🎨',
		category: '演示工具',
		action_type: 'open_url',
		url: 'https://example.com/tools/ai-ppt',
		manual_url: 'https://example.com/tools/ai-ppt/manual',
		enabled: true,
		sort_order: 70
	}
];
