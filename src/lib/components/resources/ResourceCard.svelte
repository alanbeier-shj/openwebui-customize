<script lang="ts">
	import { toast } from 'svelte-sonner';
	import BookOpen from '$lib/components/icons/BookOpen.svelte';
	import Download from '$lib/components/icons/Download.svelte';
	import GlobeAlt from '$lib/components/icons/GlobeAlt.svelte';
	import Clipboard from '$lib/components/icons/Clipboard.svelte';
	import type { Resource } from '$lib/resources/types';

	export let resource: Resource;

	let copied = false;

	const copyContact = async () => {
		try {
			await navigator.clipboard.writeText(resource.contact_value ?? '');
			copied = true;
			toast.success('联系方式已复制');
			setTimeout(() => (copied = false), 2000);
		} catch {
			toast.error('复制失败，请手动复制');
		}
	};
</script>

<article class="resource-card flex flex-col rounded-lg border border-gray-100 bg-white p-4 shadow-sm transition hover:border-gray-200 hover:shadow-md dark:border-gray-800 dark:bg-gray-900">
	<div class="flex items-start gap-3">
		<div class="flex size-10 shrink-0 items-center justify-center rounded-lg bg-gray-100 text-xl dark:bg-gray-800">
			{#if resource.icon}
				<span aria-hidden="true">{resource.icon}</span>
			{:else}
				<GlobeAlt className="size-5" strokeWidth="1.5" />
			{/if}
		</div>

		<div class="min-w-0 flex-1">
			<div class="flex items-center gap-2">
				<h3 class="truncate text-sm font-medium text-gray-900 dark:text-gray-100">{resource.name}</h3>
				<span class="shrink-0 rounded-md bg-gray-100 px-1.5 py-0.5 text-[0.6875rem] leading-4 text-gray-500 dark:bg-gray-800 dark:text-gray-400">
					{resource.category}
				</span>
			</div>

			{#if resource.description}
				<p class="mt-1 text-[0.8125rem] leading-5 text-gray-500 dark:text-gray-400">{resource.description}</p>
			{/if}
		</div>
	</div>

	<div class="mt-4 flex flex-wrap items-center gap-2">
		{#if resource.action_type === 'open_url'}
			<a
				href={resource.url}
				target="_blank"
				rel="noreferrer"
				class="inline-flex items-center gap-1.5 rounded-lg bg-gray-900 px-3 py-1.5 text-[0.8125rem] font-medium text-white transition hover:bg-gray-700 dark:bg-gray-100 dark:text-gray-900 dark:hover:bg-gray-300"
			>
				<GlobeAlt className="size-3.5" strokeWidth="1.5" />
				打开
			</a>
		{:else if resource.action_type === 'download'}
			<a
				href={resource.url}
				download
				class="inline-flex items-center gap-1.5 rounded-lg bg-gray-900 px-3 py-1.5 text-[0.8125rem] font-medium text-white transition hover:bg-gray-700 dark:bg-gray-100 dark:text-gray-900 dark:hover:bg-gray-300"
			>
				<Download className="size-3.5" strokeWidth="1.5" />
				下载安装包
			</a>
			<span class="text-[0.75rem] text-gray-400 dark:text-gray-500">下载后本地安装</span>
		{:else if resource.action_type === 'apply'}
			<div class="flex w-full flex-wrap items-center gap-2 rounded-lg bg-gray-50 px-3 py-2 dark:bg-gray-800/60">
				<span class="text-[0.8125rem] text-gray-600 dark:text-gray-300">
					联系人：{resource.contact_name ?? '管理员'}
					{#if resource.contact_method && resource.contact_value}
						<span class="text-gray-400 dark:text-gray-500"> · {resource.contact_method} {resource.contact_value}</span>
					{/if}
				</span>
				<button
					type="button"
					on:click={copyContact}
					class="inline-flex items-center gap-1 rounded-md px-1.5 py-1 text-[0.75rem] font-medium text-gray-600 transition hover:bg-gray-200 dark:text-gray-300 dark:hover:bg-gray-700"
				>
					<Clipboard className="size-3.5" strokeWidth="1.5" />
					{copied ? '已复制' : '复制'}
				</button>
			</div>
			<a
				href={resource.url}
				target="_blank"
				rel="noreferrer"
				class="inline-flex items-center gap-1.5 rounded-lg bg-gray-900 px-3 py-1.5 text-[0.8125rem] font-medium text-white transition hover:bg-gray-700 dark:bg-gray-100 dark:text-gray-900 dark:hover:bg-gray-300"
			>
				<GlobeAlt className="size-3.5" strokeWidth="1.5" />
				打开登录地址
			</a>
		{/if}

		{#if resource.manual_url}
			<a
				href={resource.manual_url}
				target="_blank"
				rel="noreferrer"
				class="ml-auto inline-flex items-center gap-1.5 rounded-lg px-2 py-1.5 text-[0.8125rem] font-medium text-gray-500 transition hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100"
			>
				<BookOpen className="size-3.5" strokeWidth="1.5" />
				使用手册
			</a>
		{/if}
	</div>
</article>

<style>
	.resource-card {
		min-width: 0;
	}
</style>
