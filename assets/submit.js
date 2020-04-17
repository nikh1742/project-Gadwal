class HTTP {
    post(submitForm) {
        const url = submitForm.getAttribute('action');
        fetch(url, {
            method: 'POST',
            body: new FormData(submitForm)
        })
            .then(res => res.text())
            .then(data => {
                document.querySelector('.modal-body').innerHTML = `<p class="text-center">${data}</p>`;
                submitForm.reset();
            })

    }
}

function submitListner(form) {
    const http = new HTTP();
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!form.checkValidity()) {
            document.getElementById('resonseMsg').innerHTML = `<p class="text-danger">Please enter valid details</p>`;
        } else {
            document.getElementById('modalToggler').click();
            http.post(form);
        }
    })
}

const customer = document.getElementById("customerContact");

submitListner(customer);
