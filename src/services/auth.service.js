import store from '../store/store'
export default {
    /**
     * 
     * @param {*} payload Contain's the user's password and username
     * @returns JWT Token if successful else returns errors
     */
    async login(payload, csrf){
        let res = await fetch('/api/v1/auth/login', {
            method: "POST",
            body: JSON.stringify(payload),
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrf
            },
        })

        return res.json()
    },

    async register(payload, csrf){
        let res = await fetch('/api/v1/register', {
            method: "POST",
            body: payload,
            headers: {
                'X-CSRFToken': csrf
            }
        })

        return res.json()
    },

    async logout(csrf){
        let res = await fetch('/api/v1/auth/logout', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Bearer ${ store.getters.getAuth || localStorage.getItem('authToken')}`,
                'X-CSRFToken': csrf
            },
        })

        return res.status === 200 ? res.json() : null
    },

    handleLogout(){
        localStorage.removeItem('authToken')
        localStorage.removeItem('id')
        store.commit('setAuth', { auth: null })
        store.commit('setUser', { user: null })
        window.history.pushState({}, "/login")
    }
}