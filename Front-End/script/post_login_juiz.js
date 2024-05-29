document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
  
    const loginData = {
      email: email,
      password: senha
    };
  
    fetch('http://ec2-44-201-200-110.compute-1.amazonaws.com/login', { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        document.getElementById('error-message').innerText = data.error;
      } else {
        alert('Login realizado com sucesso!');
        
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      document.getElementById('error-message').innerText = 'Ocorreu um erro ao fazer login.';
    });
  });
  