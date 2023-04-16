<template>
    <span id="msg" class=" form-control alert" >
    </span>
    <form id="movieForm" @submit.prevent="saveMovie">
        <fieldset class="form-group">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input id="title" type="text" name="title" class="form-control" />
            </div>
            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" rows="3" name="description" ></textarea>
            </div>
            <div class="form-group mb-3">
                <input id="poster" type="file" name="poster" class="form-control" accept="image/jpeg, image/jpg, image/png" />
            </div>
        </fieldset>
        <div class = "form-group">
            <button type="submit" class ="btn btn-primary">Submit</button>
        </div>
    </form>
</template>

<script setup>
    import { ref, onMounted } from "vue";
    let csrf_token = ref("");

    onMounted(() => {
        getCsrfToken();
    });
    
    function saveMovie() {
               let movieForm = document.getElementById('movieForm');
               let form_data = new FormData(movieForm);
               let alertcontainer =  document.querySelector('span#msg');
               fetch("/api/v1/movies", {
                   method: 'POST',
                   body: form_data,
                   headers: {
                       'X-CSRFToken': csrf_token.value
                   }
               })
               .then(function (response) {
                   return response.json();
               })
               .then(function (data) {
                   // display a success message
                   alertcontainer.classList.remove('hide');
                   if (Array.isArray(data.errors)){
                        //console.log("hey man");
                       alertcontainer.innerHTML = '';
                       self.errorlist = data.errors;
                       alertcontainer.classList.remove('alert-success');
                       alertcontainer.classList.add('alert-danger');
                       let errorlist = data.errors;
                       let fields = [];
                       for (let err=0; err<errorlist.length; err++){
                           const erroritem = document.createElement("li");
                           const node = document.createTextNode(errorlist[err]);
                           erroritem.appendChild(node);
                           alertcontainer.appendChild(erroritem);
                           fields.push(errorlist[err].split(" ")[3]);
                       }
                       console.log(fields);
                       if (fields.includes("description") && !fields.includes("poster") && fields.includes("title")){
                           document.querySelector('#description').classList.add('errhighlight');
                           document.querySelector('#poster').classList.remove('errhighlight');
                           document.querySelector('#title').classList.add('errhighlight');
                       }
                       if(fields.includes("poster") && !fields.includes("description") && fields.includes("title")){
                           document.querySelector('#poster').classList.add('errhighlight');
                           document.querySelector('#description').classList.remove('errhighlight');
                           document.querySelector('#title').classList.add('errhighlight');
                       }
                       if (fields.includes("description") && fields.includes("poster") && fields.includes("title")){
                           document.querySelector('#description').classList.add('errhighlight');
                           document.querySelector('#poster').classList.add('errhighlight');
                           document.querySelector('#title').classList.add('errhighlight');
                       }
                       if (fields.includes("description") && !fields.includes("poster") && !fields.includes("title")){
                           document.querySelector('#description').classList.add('errhighlight');
                           document.querySelector('#poster').classList.remove('errhighlight');
                           document.querySelector('#title').classList.remove('errhighlight');
                       }
                       if(fields.includes("poster") && !fields.includes("description") && !fields.includes("title")){
                           document.querySelector('#poster').classList.add('errhighlight');
                           document.querySelector('#description').classList.remove('errhighlight');
                           document.querySelector('#title').classList.remove('errhighlight');
                       }
                       if (fields.includes("description") && fields.includes("poster") && !fields.includes("title")){
                           document.querySelector('#description').classList.add('errhighlight');
                           document.querySelector('#poster').classList.add('errhighlight');
                           document.querySelector('#title').classList.remove('errhighlight');
                       }
                      
                   }
                   else{
                    console.log("hey man");
                        document.querySelector('#title').classList.remove('errhighlight');
                       document.querySelector('#description').classList.remove('errhighlight');
                       document.querySelector('#poster').classList.remove('errhighlight');
                       alertcontainer.classList.add('alert-success');
                       alertcontainer.classList.remove('alert-danger');
                       alertcontainer.innerHTML= data.message;
                   } 
                   console.log(data);
               })
               .catch(function (error) {
                   console.log(error);
               });
           }
           
           
    function getCsrfToken() {
               fetch('/api/v1/csrf-token')
               .then((response) => response.json())
               .then((data) => {
                   console.log(data);
                   csrf_token.value = data.csrf_token;
               })
           
           }

</script>
<style>
form *{
   margin-bottom: 1em;
}
.errhighlight{
   box-shadow: #F8D7DA 0px 3px 6px, #F8D7DA 0px 3px 6px;
}
</style>