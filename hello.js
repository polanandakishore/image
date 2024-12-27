document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.gallery-image');
    
    images.forEach(image => {
        image.addEventListener('click', function() {
            const src = image.src;
            const modal = document.createElement('div');
            modal.classList.add('modal');
            const modalImage = document.createElement('img');
            modalImage.src = src;
            modal.appendChild(modalImage);

            document.body.appendChild(modal);

            modal.addEventListener('click', function() {
                modal.remove();
            });
        });
    });
});