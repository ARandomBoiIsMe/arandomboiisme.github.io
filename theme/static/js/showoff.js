const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const masonryItems = document.querySelectorAll('.masonry-item img');

masonryItems.forEach(img => {
    img.addEventListener('click', e => {
        lightbox.style.display = 'flex';
        lightboxImg.src = e.target.src;
    });
});

lightbox.addEventListener('click', () => {
    lightbox.style.display = 'none';
});