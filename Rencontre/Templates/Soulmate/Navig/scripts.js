document.addEventListener('DOMContentLoaded', function () {
    const profiles = [
        {
            img: 'user1.jpg',
            name: 'Jane Doe',
            age: 25,
            interests: 'Traveling, Cooking, Reading'
        },
        {
            img: 'user2.jpg',
            name: 'John Smith',
            age: 30,
            interests: 'Hiking, Music, Gaming'
        },
        {
            img: 'user3.jpg',
            name: 'Emily Johnson',
            age: 28,
            interests: 'Fitness, Art, Cooking'
        }
    ];

    let currentProfileIndex = 0;

    function displayProfile(index) {
        const profile = profiles[index];
        document.getElementById('profileImage').src = profile.img;
        document.getElementById('userName').textContent = `${profile.name}, ${profile.age}`;
        document.getElementById('userInterests').textContent = `Likes: ${profile.interests}`;
    }

    displayProfile(currentProfileIndex);

    const likeButton = document.querySelector('.like');
    const dislikeButton = document.querySelector('.dislike');

    likeButton.addEventListener('click', function () {
        currentProfileIndex = (currentProfileIndex + 1) % profiles.length;
        displayProfile(currentProfileIndex);
        window.location.href = 'chat.html';
    });

    dislikeButton.addEventListener('click', function () {
        currentProfileIndex = (currentProfileIndex + 1) % profiles.length;
        displayProfile(currentProfileIndex);
    });

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

    const profileForm = document.querySelector('.profile-settings');
    profileForm.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Profile changes saved!');
    });

    document.getElementById('profileCard').addEventListener('click', function () {
        window.location.href = 'chat.html';
    });
});
