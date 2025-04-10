function sendMessage() {
  const userInput = document.getElementById("userInput");
  const chatBox = document.getElementById("chat");
  const message = userInput.value;
  if (!message.trim()) return;

  chatBox.innerHTML += `<div class="text-gray-800">👤 You: ${message}</div>`;
  userInput.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: message })
  })
  .then(res => res.json())
  .then(data => {
    chatBox.innerHTML += `<div class="text-pink-500">🤖 PetBot: ${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}

function endChat() {
  const chatBox = document.getElementById("chat");
  chatBox.innerHTML += `<div class="text-pink-500">🐾 PetBot: Chat ended. Take care of your furry friend! 🐶</div>`;
  document.getElementById("userInput").disabled = true;
}

// Enable full-screen chat on "Chat" click
document.querySelector('a[href="#chat-section"]').addEventListener('click', function (e) {
  e.preventDefault();
  document.getElementById('chat-section').classList.add('fullscreen');
  document.querySelector('nav').classList.add('hide-main');
  document.getElementById('suggestions').classList.add('hide-main');
  document.querySelector('footer').classList.add('hide-main');
}); 