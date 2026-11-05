<script lang="ts">
	import ResourceCard from './ResourceCard.svelte';
	import type { Resource } from '$lib/resources/types';

	export let resources: Resource[] = [];

	$: categories = resources.reduce<{ name: string; items: Resource[] }[]>((acc, resource) => {
		const group = acc.find((entry) => entry.name === resource.category);
		if (group) {
			group.items.push(resource);
		} else {
			acc.push({ name: resource.category, items: [resource] });
		}
		return acc;
	}, []);
</script>

<div class="space-y-8">
	{#each categories as category (category.name)}
		<section>
			<div class="mb-3 flex items-center gap-2">
				<h2 class="text-sm font-semibold text-gray-900 dark:text-gray-100">{category.name}</h2>
				<span class="text-[0.75rem] text-gray-400 dark:text-gray-500">{category.items.length}</span>
			</div>

			<div class="grid grid-cols-1 gap-3 md:grid-cols-2 xl:grid-cols-3">
				{#each category.items as resource (resource.id)}
					<ResourceCard {resource} />
				{/each}
			</div>
		</section>
	{/each}
</div>
