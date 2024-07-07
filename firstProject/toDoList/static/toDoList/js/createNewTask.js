document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('create_button').addEventListener('click', openModal);
});


function openModal() {
    const createModal = document.getElementById('createTaskModal');
    createModal.classList.remove('fade');
    createModal.style.display = 'block';
    document.getElementById('dismiss_modal').addEventListener('click', closeModal);
    document.getElementById('close_modal').addEventListener('click', closeModal);
}

function closeModal() {
    const createModal = document.getElementById('createTaskModal');
    createModal.classList.add('fade');
    createModal.style.display = 'none';
    document.getElementById('dismiss_modal').removeEventListener('click', closeModal);
    document.getElementById('close_modal').removeEventListener('click', closeModal);
}