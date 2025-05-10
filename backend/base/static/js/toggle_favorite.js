document.addEventListener('DOMContentLoaded', function() {
    // Handle favorite buttons in both detail and list views
    document.querySelectorAll('.favorite-btn').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            
            const icon = this.querySelector('i');
            const url = this.getAttribute('data-favorite-url');
            
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.favorite) {
                    icon.classList.remove('far');
                    icon.classList.add('fas', 'text-red-500');
                } else {
                    icon.classList.remove('fas', 'text-red-500');
                    icon.classList.add('far');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});