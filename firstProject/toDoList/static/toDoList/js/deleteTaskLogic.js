document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('delete_button').addEventListener('click', deleteTask);
});

function deleteTask() {
    const checkboxes = document.querySelectorAll('.btn-check:checked');
    const form = document.getElementById('delete_form');

    document.querySelectorAll('.hidden-task-id').forEach(field => field.remove());

    checkboxes.forEach(checkbox => {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = 'task_ids';
        hiddenField.value = checkbox.getAttribute('data-id');
        hiddenField.className = 'hidden-task-id';
        form.appendChild(hiddenField);
    });
    if(checkboxes.length > 0){form.submit()}
}