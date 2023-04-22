import store from '../store/store'
export default{
    async getAllPosts(){
        let res = await fetch(`/api/v1/posts`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
            }
        })

        return res.status === 200 ? res.json() : null
    },
    async addLike(id, csrf){
        let res = await fetch(`/api/v1/posts/${id}/like`, {
            method: "POST",
            body: JSON.stringify({
                "car_id": id,
                "user_id": store.getters.getUser || localStorage.getItem('id')
            }),
            headers: {
                'Content-type': 'application/json',
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
                'X-CSRFToken': csrf
            }
        })

        return res.json()
    },
}