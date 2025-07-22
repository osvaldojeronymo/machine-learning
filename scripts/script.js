document.addEventListener('DOMContentLoaded', function () {
  function showSection(id, event) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('nav ul li').forEach(li => li.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    if (event) event.target.classList.add('active');
  }

  // Attach event listeners
  document.querySelectorAll('nav ul li').forEach(li => {
    li.addEventListener('click', function (event) {
      const id = li.textContent.includes('Tabela') ? 'parte1' : 'parte2';
      showSection(id, event);
    });
  });
});
