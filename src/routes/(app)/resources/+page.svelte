<script lang="ts">
	import { onMount } from 'svelte';
	import Spinner from '$lib/components/common/Spinner.svelte';
	import ResourceCenter from '$lib/components/resources/ResourceCenter.svelte';
	import { getResources, type Resource } from '$lib/resources';
	import { user } from '$lib/stores';

	let resources: Resource[] = [];
	let loading = true;

	onMount(async () => {
		try {
			resources = await getResources();
		} finally {
			loading = false;
		}
	});
</script>

<div class="mx-auto w-full max-w-6xl px-4 py-6 md:px-6">
	<header class="mb-6">
		<div class="flex items-start justify-between gap-4">
			<div>
				<h1 class="text-lg font-semibold text-gray-900 dark:text-gray-100">资源中心</h1>
				<p class="mt-1 text-[0.8125rem] text-gray-500 dark:text-gray-400">这里汇总了可供使用的平台、工具及其使用手册。</p>
			</div>
			{#if $user?.role === 'admin'}
				<a
					href="/admin/resources"
					class="shrink-0 rounded-lg border border-gray-200 px-3 py-1.5 text-[0.8125rem] font-medium text-gray-700 transition hover:bg-gray-50 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800"
				>
					管理资源
				</a>
			{/if}
		</div>
	</header>

	{#if loading}
		<div class="flex justify-center py-16">
			<Spinner className="size-5" />
		</div>
	{:else if resources.length === 0}
		<div class="rounded-lg border border-dashed border-gray-200 py-16 text-center text-sm text-gray-500 dark:border-gray-700 dark:text-gray-400">
			暂无可用的资源
		</div>
	{:else}
		<ResourceCenter {resources} />
	{/if}
</div>
