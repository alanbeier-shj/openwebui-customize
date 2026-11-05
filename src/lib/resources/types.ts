export type ResourceActionType = 'open_url' | 'download' | 'apply';

export interface Resource {
	id: string;
	name: string;
	description?: string;
	icon?: string;
	category: string;
	action_type: ResourceActionType;
	url: string;
	contact_name?: string;
	contact_method?: string;
	contact_value?: string;
	manual_url?: string;
	enabled: boolean;
	sort_order: number;
}
