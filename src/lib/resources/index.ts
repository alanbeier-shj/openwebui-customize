import { getResources as fetchResources } from '$lib/apis/resources';
import type { Resource } from './types';

// 资源数据入口。页面和组件只依赖这里，数据来源可以在静态配置和后端接口之间切换。
export async function getResources(): Promise<Resource[]> {
	const token = typeof localStorage !== 'undefined' ? localStorage.token : '';
	return (await fetchResources(token)) as Resource[];
}

export type { Resource, ResourceActionType } from './types';
