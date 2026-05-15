document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.querySelector('form');
    const selects = filterForm.querySelectorAll('select');

    // Hacer que el formulario se envíe automáticamente al cambiar una opción
    selects.forEach(select => {
        select.addEventListener('change', () => {
            filterForm.submit();
        });
    });
});