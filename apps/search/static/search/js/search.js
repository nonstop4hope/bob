window.addEventListener('DOMContentLoaded', event=>{


const sendBtn = document.querySelector('#button-search'),
    searchInput = document.querySelector('#search-input')
     datatablesSimple = document.getElementById('datatablesSimple');
     errorModal = document.getElementById('error-modal');



let dataTable = new simpleDatatables.DataTable(datatablesSimple)

  function renderYesNo(data, cell, row) {
        if (data == 'true') {
            return row.classList.add("yes"),
            `<b>Yes</b>`;
        } else if (data == 'false') {
            return row.classList.add("no"),
            `<input type="checkbox">`;
        }
    }

function sendRequests() {

    if (searchInput.value.trim() == '') {
    showErrorModal('Пустая строка запроса')
    return;}

    let data = {search_term:searchInput.value}

    fetch('/api/v1/search/google', {
        method: 'POST',
        headers: {
    'Content-Type': 'application/json;charset=utf-8'
  },
        body: JSON.stringify(data)
    }).then(response=>response.json()).then(data=>{
        if (!data.results.length) {
            return
        }

        if (datatablesSimple) {

            let headings = Object.keys(data.results[0])
            headings.unshift('<input type="checkbox">')
            data = data.results.map(item=>Object.values(item))

            data.forEach(item => {item.unshift('false')})

            dataTable.destroy()

            dataTable = new simpleDatatables.DataTable(datatablesSimple,{
                data: {
                    headings: headings,
                    data: data
                },
                fixedHeight: true,
                columns: [{
                    select: 0,
                    render: renderYesNo,
                    sortable: false
                }]
            });

            dataTable.headings[0].addEventListener('click', () => {

                Array.from(dataTable.data).forEach(item =>
                {
                    item.cells[0].childNodes[0].checked = true
                });

            });


        }
    }
    )

}

sendBtn.addEventListener('click', () => sendRequests());

function showErrorModal(error) {

    const modal = document.createElement('div');
    modal.classList.add('hide');
    modal.innerHTML = `
    <div class="modal fade" id="modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">\
<div class="modal-dialog" role="document"> \
        <div class="modal-content"> \
            <div class="modal-header"> \
                <h5 class="modal-title" id="exampleModalLabel">Внимание</h5> \
                <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button> \
            </div> \
            <div class="modal-body"> \
                Подтверждаете обработку данных ? \
            </div> \
            <div class="modal-footer"> \
                <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Отменить</button> \
                <button class="btn btn-primary" type="button">Подтвердить</button> \
            </div> \
        </div> \
</div>
</div>
`

$('#error-modal').modal()

}
}
);
