// Main JavaScript functionality for the moodboard creator

// Image preview functionality
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('images');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const files = e.target.files;
            if (files.length > 0) {
                // You could add image preview functionality here
                console.log(`${files.length} images selected`);
            }
        });
    }
});

// Theme switcher functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeRadios = document.querySelectorAll('input[name="theme"]');
    themeRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            document.body.setAttribute('data-theme', this.value);
        });
    });
});

// Print functionality
function printMoodboard() {
    window.print();
}

// Download functionality (to be implemented with backend)
function downloadMoodboard() {
    // This would need to be implemented with a proper backend endpoint
    alert('Download functionality will be implemented soon!');
} 