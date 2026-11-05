<script lang="ts">
	import { onMount } from 'svelte';
	import { toast } from 'svelte-sonner';
	import Plus from '$lib/components/icons/Plus.svelte';
	import Pencil from '$lib/components/icons/Pencil.svelte';
	import Trash from '$lib/components/icons/Trash.svelte';
	import {
		getAllResources,
		createResource,
		updateResource,
		deleteResource
	} from '$lib/apis/resources';
	import type { Resource } from '$lib/resources/types';

	let resources: Resource[] = [];
	let loading = true;
	let showForm = false;
	let editing: Resource | null = null;

	const emptyForm = () => ({
		name: '',
		description: '',
		icon: '',
		category: '',
		action_type: 'open_url',
		url: '',
		contact_name: '',
		contact_method: '',
		contact_value: '',
		manual_url: '',
		enabled: true,
		sort_order: 0
	});

	let form: any = emptyForm();

	const load = async () => {
		loading = true;
		try {
			resources = await getAllResources(localStorage.token);
		} catch (error) {
			toast.error('加载资源失败');
		} finally {
			loading = false;
		}
	};

	const openCreate = () => {
		form = emptyForm();
		editing = null;
		showForm = true;
	};

	const openEdit = (resource: Resource) => {
		form = { ...resource };
		editing = resource;
		showForm = true;
	};

	const closeForm = () => {
		showForm = false;
		editing = null;
		form = emptyForm();
	};

	const save = async () => {
		if (!form.name.trim()) {
			toast.error('请输入资源名称');
			return;
		}
		try {
			if (editing) {
				await updateResource(localStorage.token, editing.id, form);
				toast.success('资源已更新');
			} else {
				await createResource(localStorage.token, form);
				toast.success('资源已创建');
			}
			closeForm();
			await load();
		} catch (error) {
			toast.error('保存失败');
		}
	};

	const remove = async (resource: Resource) => {
		if (!window.confirm(`确定删除“${resource.name}”吗？`)) return;
		try {
			await deleteResource(localStorage.token, resource.id);
			toast.success('资源已删除');
			await load();
		} catch (error) {
			toast.error('删除失败');
		}
	};

	onMount(load);
</script>

<div class="mx-auto w-full max-w-5xl px-4 py-6 md:px-6">
	<header class="mb-5 flex items-center justify-between">
		<div>
			<h1 class="text-lg font-semibold text-gray-900 dark:text-gray-100">资源中心管理</h1>
			<p class="mt-1 text-[0.8125rem] text-gray-500 dark:text-gray-400">配置资源中心页面上展示的所有内容。</p>
		</div>

		<button
			type="button"
			on:click={openCreate}
			class="inline-flex items-center gap-1.5 rounded-lg bg-gray-900 px-3 py-1.5 text-[0.8125rem] font-medium text-white transition hover:bg-gray-700 dark:bg-gray-100 dark:text-gray-900 dark:hover:bg-gray-300"
		>
			<Plus className="size-3.5" strokeWidth="2" />
			新增资源
		</button>
	</header>

	{#if showForm}
		<div class="mb-6 rounded-lg border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
			<h2 class="mb-4 text-sm font-medium text-gray-900 dark:text-gray-100">
				{editing ? '编辑资源' : '新增资源'}
			</h2>

			<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
				<label class="block">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">名称 *</span>
					<input bind:value={form.name} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
				</label>

				<label class="block">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">分类</span>
					<input bind:value={form.category} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
				</label>

				<label class="block">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">图标（emoji）</span>
					<input bind:value={form.icon} placeholder="例如 🤖" class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
				</label>

				<label class="block">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">类型</span>
					<select bind:value={form.action_type} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100">
						<option value="open_url">打开网址</option>
						<option value="download">下载安装包</option>
						<option value="apply">联系开通</option>
					</select>
				</label>

				<label class="block md:col-span-2">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">主链接</span>
					<input bind:value={form.url} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
				</label>

				<label class="block md:col-span-2">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">描述</span>
					<textarea bind:value={form.description} rows="2" class="w-full resize-none rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100"></textarea>
				</label>

				<label class="block md:col-span-2">
					<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">操作手册链接（可选）</span>
					<input bind:value={form.manual_url} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
				</label>

				{#if form.action_type === 'apply'}
					<label class="block">
						<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">联系人</span>
						<input bind:value={form.contact_name} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
					</label>
					<label class="block">
						<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">联系方式类型</span>
						<input bind:value={form.contact_method} placeholder="例如 微信" class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
					</label>
					<label class="block">
						<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">联系方式</span>
						<input bind:value={form.contact_value} class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
					</label>
					<label class="block">
						<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">排序</span>
						<input bind:value={form.sort_order} type="number" class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
					</label>
				{:else}
					<label class="block">
						<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">排序</span>
						<input bind:value={form.sort_order} type="number" class="w-full rounded-lg border border-gray-200 bg-transparent px-3 py-2 text-sm text-gray-900 outline-none focus:border-gray-400 dark:border-gray-700 dark:text-gray-100" />
					</label>
					<label class="block">
						<span class="mb-1 block text-[0.75rem] font-medium text-gray-500 dark:text-gray-400">启用</span>
						<label class="flex items-center gap-2 py-2 text-sm text-gray-700 dark:text-gray-200">
							<input bind:checked={form.enabled} type="checkbox" class="size-4" />
							显示在资源中心
						</label>
					</label>
				{/if}
			</div>

			<div class="mt-4 flex justify-end gap-2">
				<button
					type="button"
					on:click={closeForm}
					class="rounded-lg border border-gray-200 px-3 py-1.5 text-[0.8125rem] font-medium text-gray-700 transition hover:bg-gray-50 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800"
				>
					取消
				</button>
				<button
					type="button"
					on:click={save}
					class="rounded-lg bg-gray-900 px-3 py-1.5 text-[0.8125rem] font-medium text-white transition hover:bg-gray-700 dark:bg-gray-100 dark:text-gray-900 dark:hover:bg-gray-300"
				>
					保存
				</button>
			</div>
		</div>
	{/if}

	{#if loading}
		<div class="py-12 text-center text-sm text-gray-500 dark:text-gray-400">加载中…</div>
	{:else if resources.length === 0}
		<div class="rounded-lg border border-dashed border-gray-200 py-12 text-center text-sm text-gray-500 dark:border-gray-700 dark:text-gray-400">
			还没有资源，点击“新增资源”开始配置
		</div>
	{:else}
		<div class="space-y-2">
			{#each resources as resource (resource.id)}
				<div class="flex items-center gap-3 rounded-lg border border-gray-100 bg-white px-4 py-3 dark:border-gray-800 dark:bg-gray-900">
					<div class="flex size-9 shrink-0 items-center justify-center rounded-lg bg-gray-100 text-lg dark:bg-gray-800">
						{resource.icon || '🔗'}
					</div>
					<div class="min-w-0 flex-1">
						<div class="flex items-center gap-2">
							<span class="truncate text-sm font-medium text-gray-900 dark:text-gray-100">{resource.name}</span>
							<span class="rounded-md bg-gray-100 px-1.5 py-0.5 text-[0.6875rem] text-gray-500 dark:bg-gray-800 dark:text-gray-400">
								{resource.category || '未分类'}
							</span>
							{#if !resource.enabled}
								<span class="rounded-md bg-gray-200 px-1.5 py-0.5 text-[0.6875rem] text-gray-500 dark:bg-gray-700 dark:text-gray-400">已停用</span>
							{/if}
						</div>
						<p class="truncate text-[0.75rem] text-gray-500 dark:text-gray-400">{resource.description || resource.url || '无描述'}</p>
					</div>

					<div class="flex shrink-0 items-center gap-1">
						<button type="button" on:click={() => openEdit(resource)} class="rounded-md p-1.5 text-gray-500 transition hover:bg-gray-100 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-gray-100" aria-label="编辑">
							<Pencil className="size-4" strokeWidth="1.5" />
						</button>
						<button type="button" on:click={() => remove(resource)} class="rounded-md p-1.5 text-gray-500 transition hover:bg-gray-100 hover:text-red-600 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-red-400" aria-label="删除">
							<Trash className="size-4" strokeWidth="1.5" />
						</button>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
