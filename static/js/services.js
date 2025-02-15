document.querySelectorAll('.grid-item').forEach(item => {
    item.addEventListener('click', function () {
        const sectionId = this.getAttribute('data-scroll-to');
        const targetSection = document.getElementById(sectionId);

        if (targetSection) {
            targetSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
