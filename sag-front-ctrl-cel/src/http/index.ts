import axios, { AxiosInstance } from 'axios';

// const token = localStorage.getItem('jwt');

const httpClient: AxiosInstance = axios.create({
    baseURL: 'http://localhost:5000/',
    // headers: {
    //     Authorization: token ? `Bearer ${token}` : '',
    // },
});

httpClient.interceptors.request.use((config) => {
    const token = localStorage.getItem('jwt');
    if(token) {
        config.headers = {
            Authorization: `Bearer ${token}`,
        }
    }
    return config;
})

export default httpClient;