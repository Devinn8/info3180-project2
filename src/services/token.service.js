export default{
    async getCrsfToken(){
        let res = await fetch('/api/v1/csrf-token', {
            method: 'GET'
        })

        return await res.json()
    }
}