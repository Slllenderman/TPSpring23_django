initValidation = () => {
    'use strict'
    const forms = document.querySelectorAll('.needs-validation')
  
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
        const helpers = document.querySelectorAll('.helper')
        Array.from(helpers).forEach(helper => {
            helper.style.display = "none"
        })
      }, false)
    })
}