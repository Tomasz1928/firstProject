document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('update_task_button').addEventListener('click', openModal);
});


function openModal() {
    const createModal = document.getElementById('createTaskModal');
    const radio = document.querySelectorAll('.form-check-input:checked');
    const setTaskIdToUpdate = document.getElementById('update_task_input_id');

    if(radio.length > 0){
    setTaskIdToUpdate.value = radio[0].getAttribute('data-id');
    createModal.classList.remove('fade');
    createModal.style.display = 'block';
    }


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