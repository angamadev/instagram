
    const likeButton = document.getElementById('likeButton');
    const nLikesSpan = document.getElementById('nLikes');

    let nLikes = parseInt(nLikesSpan.innerHtml);
    likeButton.addEventListener('click',(event) => {
        // Prevenimos el comportamiento por defecto del boton
        event.preventDefault();
        // Hacemos una peticion GET al href del boton
        fetch(likeButton.href)
            .then(response => response.json())
            .then(data => {
                // Si la peticion fue exitosa, cambiamos el contenido del boton
                if (data.liked) {
                    likeButton.innerHtml = '<i class="bi bi-suit-heart-fill"></i>';
                    nLikes += 1;
                    nLikesSpan.innerHtml = nLikes;

                // Si la peticion fue Falsa, cambiamos el contenido del boton
                } else {
                    likeButton.innerHtml = '<i class="bi bi-heart"></i>';
                    nLikes -= 1;
                    nLikesSpan.innerHtml = nLikes;
                }
            });
    })
