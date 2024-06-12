
document.addEventListener('DOMContentLoaded', function () {
    // Like button functionality
    const likeButtons = document.querySelectorAll('.like');
    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            alert('You liked this profile!');
        });
    });

    // Dislike button functionality
    const dislikeButtons = document.querySelectorAll('.dislike');
    dislikeButtons.forEach(button => {
        button.addEventListener('click', function () {
            alert('You disliked this profile.');
        });
    });

    // Send message functionality
    const sendButton = document.querySelector('.send');
    sendButton.addEventListener('click', function () {
        const input = document.querySelector('.chat-input input');
        const message = input.value.trim();
        if (message) {
            const chatWindow = document.querySelector('.chat-window');
            const newMessage = document.createElement('div');
            newMessage.classList.add('message', 'sent');
            newMessage.innerHTML = `<p>${message}</p><span class="timestamp">Just now</span>`;
            chatWindow.appendChild(newMessage);
            input.value = '';
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
    });

    // Save profile changes
    const profileForm = document.querySelector('.profile-settings');
    profileForm.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Profile changes saved!');
    });
});
