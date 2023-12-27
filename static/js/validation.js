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

set_Like = (user_id, answer_id) => {
  var csrftoken = Cookies.get('csrftoken')

  $.ajax({
    headers: { "X-CSRFToken": csrftoken },
    url: 'set_like/',
    data: {
      'user_id' : user_id,
      'obj_id': answer_id
    },
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        alert(data.error_message);
      }
    }
  });
}