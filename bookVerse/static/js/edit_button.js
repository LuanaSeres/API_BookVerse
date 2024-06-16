document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.editar').forEach(function(button) {
      button.addEventListener('click', function() {
          window.location.href = button.getAttribute('data-url');
      });
  });
});
