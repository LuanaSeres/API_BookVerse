document.addEventListener('DOMContentLoaded', function() {
    var deleteBtns = document.querySelectorAll('.delete-btn');
    var popup = document.getElementById('confirmation-popup');
    var confirmBtn = document.getElementById('confirm-delete-btn');
    var cancelBtn = document.getElementById('cancel-delete-btn');
    var currentForm = null;
    var returnUrl = null;

    deleteBtns.forEach(function(deleteBtn) {
        deleteBtn.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the form from submitting
            currentForm = deleteBtn.closest('form'); // Get the current form
            returnUrl = currentForm.getAttribute('data-return-url'); // Get the return URL
            popup.style.display = 'flex'; // Show the popup
        });
    });

    confirmBtn.addEventListener('click', function() {
        popup.style.display = 'none'; // Hide the popup
        if (currentForm) {
            currentForm.submit(); // Submit the form
        }

        // Redirect to the return URL after a short delay
        if (returnUrl) {
            setTimeout(function() {
                window.location.href = returnUrl;
            }, 1000); // Adjust the delay time as needed
        }
    });

    cancelBtn.addEventListener('click', function() {
        popup.style.display = 'none'; // Hide the popup
    });
});
