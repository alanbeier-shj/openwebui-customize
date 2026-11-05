import { WEBUI_API_BASE_URL } from '$lib/constants';

const headers = (token: string) => ({
	Accept: 'application/json',
	'Content-Type': 'application/json',
	authorization: `Bearer ${token}`
});

export const getResources = async (token: string = '') => {
	const response = await fetch(`${WEBUI_API_BASE_URL}/resources`, {
		method: 'GET',
		headers: headers(token)
	});
	if (!response.ok) throw await response.json();
	return response.json();
};

export const getAllResources = async (token: string = '') => {
	const response = await fetch(`${WEBUI_API_BASE_URL}/resources/all`, {
		method: 'GET',
		headers: headers(token)
	});
	if (!response.ok) throw await response.json();
	return response.json();
};

export const createResource = async (token: string, resource: Record<string, unknown>) => {
	const response = await fetch(`${WEBUI_API_BASE_URL}/resources`, {
		method: 'POST',
		headers: headers(token),
		body: JSON.stringify(resource)
	});
	if (!response.ok) throw await response.json();
	return response.json();
};

export const updateResource = async (token: string, id: string, resource: Record<string, unknown>) => {
	const response = await fetch(`${WEBUI_API_BASE_URL}/resources/${id}/update`, {
		method: 'POST',
		headers: headers(token),
		body: JSON.stringify(resource)
	});
	if (!response.ok) throw await response.json();
	return response.json();
};

export const deleteResource = async (token: string, id: string) => {
	const response = await fetch(`${WEBUI_API_BASE_URL}/resources/${id}/delete`, {
		method: 'DELETE',
		headers: headers(token)
	});
	if (!response.ok) throw await response.json();
	return response.json();
};
