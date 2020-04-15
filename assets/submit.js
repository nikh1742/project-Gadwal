const form = document.getElementById('customerContact');
url = form.getAttribute('action');
const myModal = document.querySelector('.modal-body')


form.addEventListener('submit', function (e) {
    e.preventDefault();
    fetch(url,
        {
            method: 'POST',
            body: new FormData(form)
        })
        .then(res => res.text())
        .then(data => {
            myModal.innerHTML = `<P>${data}</p>`;
        })
})
