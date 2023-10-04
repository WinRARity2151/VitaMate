        document.getElementById('showFormButton').addEventListener('click', function() {
            var form = document.getElementById('popupForm');
            form.style.display = 'block';
        });

        document.getElementById('closeFormButton').addEventListener('click', function() {
            var form = document.getElementById('popupForm');
            form.style.display = 'none';
        });
