<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enlightened Core AI License Agreement</title>
    <style>
        /* Modal styling */
        #agreementModal {
            display: none; /* Hidden by default */
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        #modalContent {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
            text-align: left;
        }
        #agreeButton {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            margin-top: 15px;
        }
        #agreeButton:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <!-- Modal for License Agreement -->
    <div id="agreementModal">
        <div id="modalContent">
            <h2>Enlightened Core AI License Agreement</h2>
            <p>Please review the licensing terms below carefully.</p>

            <h3>1. Ownership and Intellectual Property Rights</h3>
            <p>All rights, title, and interest in and to the model, including its algorithms, code, architecture, updates, modifications, and improvements, are exclusively owned by Licensor. Licensee is granted limited access rights under this Agreement and does not gain any ownership or proprietary rights in the model.</p>

            <!-- Additional license content here as needed -->

            <h3>5. General Terms</h3>
            <p>Licensor provides the model “as-is” with no warranties, express or implied, regarding accuracy, completeness, or reliability of outputs. Licensee assumes all risks for any decisions made based on the model’s outputs.</p>

            <p><strong>By clicking "I Agree," you confirm acceptance of these terms.</strong></p>

            <button id="agreeButton">I Agree</button>
        </div>
    </div>

    <!-- Main Page Content -->
    <div id="mainContent" style="display: none;">
        <h1>Welcome to NLP Projects - Enlightened Core</h1>
        <p>This is the main content of the site, visible only after agreement.</p>
    </div>

    <script>
        // Show modal on page load if agreement not previously accepted
        document.addEventListener("DOMContentLoaded", function() {
            if (!localStorage.getItem("licenseAgreed")) {
                document.getElementById("agreementModal").style.display = "flex";
            } else {
                document.getElementById("mainContent").style.display = "block";
            }
        });

        // Handle "I Agree" button click
        document.getElementById("agreeButton").onclick = function() {
            localStorage.setItem("licenseAgreed", "true");
            document.getElementById("agreementModal").style.display = "none";
            document.getElementById("mainContent").style.display = "block";
        };
    </script>
</body>
</html>
