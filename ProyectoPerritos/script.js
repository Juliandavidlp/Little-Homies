document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.querySelector('form');
    formulario.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const nombre = document.getElementById('nombreapellido').value;
      const correo = document.getElementById('correoelectronico').value;
      const telefono = document.getElementById('telefono').value;
      const mensaje = document.getElementById('mensaje').value;
  
      if (!nombre || !correo || !telefono || !mensaje) {
        alert('Por favor, complete todos los campos del formulario.');
      } else if (!validateEmail(correo)) {
        alert('Por favor, ingrese una dirección de correo electrónico válida.');
      } else {
 
  
        alert('¡Formulario enviado con éxito!');
        formulario.reset();
      }
    });
  
    // Función para validar una dirección de correo electrónico
    function validateEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
    }
  });