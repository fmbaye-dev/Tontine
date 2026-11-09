import axios from 'axios';

// 1. Fallback to a default if the env variable is missing (prevents 'undefinedapi/')
const baseEnv = process.env.NEXT_PUBLIC_DJANGO_API_URL || 'http://127.0.0.1:8000';

// 2. Ensure proper slash structure so it doesn't glue together as "8000api/"
const cleanBaseUrl = baseEnv.endsWith('/') ? `${baseEnv}api/` : `${baseEnv}/api/`;

const api = axios.create({
  baseURL: cleanBaseUrl,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;