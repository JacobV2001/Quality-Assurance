// Simple form validation for login
document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    
    if (email !== "test@example.com" || password !== "password123") {
        document.getElementById("error-message").style.display = "block";
    } else {
        alert("Login successful!");
        window.location.href = "catalog.html"; // Redirect to catalog page on success
    }
});

// Simple form submission for contact form
document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Message sent successfully!");
});
