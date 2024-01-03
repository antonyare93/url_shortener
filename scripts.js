fetch(`/api/shortener/${id}`)
   .then(response => response.json())
   .then(data => {
       // Redirect to the received URL
       window.location.href = data;
   });