// Theme toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    
    // Check for saved theme preference or default to light mode
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.classList.toggle('dark', savedTheme === 'dark');
        updateToggleButton();
    }
    
    // Add click event listener to theme toggle button
    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark');
        
        // Save theme preference to localStorage
        const isDark = body.classList.contains('dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        
        updateToggleButton();
    });
    
    // Update button text and icon based on current theme
    function updateToggleButton() {
        const isDark = body.classList.contains('dark');
        themeToggle.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    }
});

// Tab switching functionality for portfolio projects
function showTab(tabId, buttonElement) {
    // Get the parent project container
    const projectContainer = buttonElement.closest('.project');

    // Hide all tab contents in this project
    const tabContents = projectContainer.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
        content.style.display = 'none';
    });

    // Remove active class from all tab buttons in this project
    const tabButtons = projectContainer.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.classList.remove('active');
    });

    // Show the selected tab content
    const selectedTab = document.getElementById(tabId);
    if (selectedTab) {
        selectedTab.style.display = 'block';
    }

    // Add active class to the clicked button
    buttonElement.classList.add('active');
}

// Copy code functionality
function copyCode(elementId) {
    const codeElement = document.getElementById(elementId);
    if (codeElement) {
        const text = codeElement.textContent || codeElement.innerText;

        // Use the modern clipboard API if available
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(text).then(() => {
                showCopyFeedback();
            }).catch(err => {
                console.error('Failed to copy text: ', err);
                fallbackCopyText(text);
            });
        } else {
            // Fallback for older browsers
            fallbackCopyText(text);
        }
    }
}

// Fallback copy method for older browsers
function fallbackCopyText(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
        document.execCommand('copy');
        showCopyFeedback();
    } catch (err) {
        console.error('Fallback: Oops, unable to copy', err);
    }

    document.body.removeChild(textArea);
}

// Show copy feedback
function showCopyFeedback() {
    // Create a temporary feedback element
    const feedback = document.createElement('div');
    feedback.textContent = 'Code copied to clipboard!';
    feedback.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #10b981;
        color: white;
        padding: 10px 20px;
        border-radius: 6px;
        z-index: 1000;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transition: opacity 0.3s ease;
    `;

    document.body.appendChild(feedback);

    // Remove the feedback after 3 seconds
    setTimeout(() => {
        feedback.style.opacity = '0';
        setTimeout(() => {
            if (feedback.parentNode) {
                document.body.removeChild(feedback);
            }
        }, 300);
    }, 3000);
}
