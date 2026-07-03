import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export default API;

export const sendMessage = async (question) => {
    const response = await API.post("/chat/", {
        question
    });

    return response.data;
};