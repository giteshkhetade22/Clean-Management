// script1.js
document.addEventListener("DOMContentLoaded", function () {
    const bookingForm = document.getElementById('bookingForm');
    const summaryDiv = document.getElementById('summary');

    bookingForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const formData = new FormData(bookingForm);

        // Construct booking summary
        let summaryHTML = '<h3>Booking Details</h3>';
        formData.forEach((value, key) => {
            summaryHTML += `<p><strong>${key}:</strong> ${value}</p>`;
        });

        // Display booking summary
        summaryDiv.innerHTML = summaryHTML;
    });
});
