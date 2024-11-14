<script>
    document.addEventListener("DOMContentLoaded", function() {
        // Set expiration period for license acceptance in days
        const EXPIRATION_DAYS = 90;

        // Check if license has been accepted and if it's within the expiration period
        function isLicenseStillValid() {
            const agreedTime = localStorage.getItem("licenseAgreedTime");
            if (!agreedTime) return false;  // No agreement found, show modal

            const agreedDate = new Date(parseInt(agreedTime, 10));
            const currentDate = new Date();

            // Calculate the difference in days
            const differenceInDays = Math.floor((currentDate - agreedDate) / (1000 * 60 * 60 * 24));
            return differenceInDays < EXPIRATION_DAYS;
        }

        // Display the modal if the license is not valid
        if (!isLicenseStillValid()) {
            document.getElementById("agreementModal").style.display = "flex";
            document.body.classList.add("modal-active");  // Prevents scrolling
        } else {
            document.getElementById("mainContent").style.display = "block";
        }

        // Handle the "I Agree" button click
        document.getElementById("agreeButton").onclick = function() {
            // Store the acceptance timestamp
            localStorage.setItem("licenseAgreedTime", Date.now().toString());
            document.getElementById("agreementModal").style.display = "none";
            document.getElementById("mainContent").style.display = "block";
            document.body.classList.remove("modal-active");  // Re-enables scrolling
        };
    });
</script>
