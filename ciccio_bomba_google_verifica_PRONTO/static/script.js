const filterBtns = document.querySelectorAll('.filter-btn');
const menuCards = document.querySelectorAll('.menu-card');
const modal = document.getElementById('item-modal');
const modalClose = document.getElementById('modal-close');

// Modal Elements
const modalImg = document.getElementById('modal-img');
const modalCategory = document.getElementById('modal-category');
const modalTitle = document.getElementById('modal-title');
const modalPrice = document.getElementById('modal-price');
const modalDesc = document.getElementById('modal-description');
const modalIngredients = document.getElementById('modal-ingredients');
const modalNotes = document.getElementById('modal-notes');

// Filtering
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const filter = btn.getAttribute('data-filter');
        menuCards.forEach(card => {
            const category = card.getAttribute('data-category');
            if (filter === 'all' || category === filter) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

// Modal function
function openModal(item) {
    modalImg.src = item.image;
    modalCategory.textContent = item.category.toUpperCase();
    modalTitle.textContent = item.title;
    modalPrice.textContent = item.price;
    modalDesc.textContent = item.description;
    modalIngredients.textContent = item.ingredients;
    modalNotes.textContent = item.notes;

    modal.style.display = 'flex';
}

modalClose.addEventListener('click', () => {
    modal.style.display = 'none';
});

window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
