window.addEventListener('DOMContentLoaded', event=>{


const sendBtn = document.querySelector('#button-search'),
    searchInput = document.querySelector('#search-input')


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

    if (searchInput.value.trim() == '') return;

    let data = {search_term:searchInput.value}

    fetch('/api/v1/search/google', {
        method: 'POST',
        headers: {
    'Content-Type': 'application/json;charset=utf-8'
  },
        body: JSON.stringify(data)
    }).then(response=>response.json()).then(data=>{
        if (!data.response.length) {
            return
        }

        const datatablesSimple = document.getElementById('datatablesSimple');

        if (datatablesSimple) {

            let headings = Object.keys(data.response[0])
            headings.unshift('select')
            data = data.response.map(item=>Object.values(item))

            data.forEach(item => {item.unshift('false')})

            let dataTable = new simpleDatatables.DataTable(datatablesSimple,{
                data: {
                    headings: headings,
                    data: data
                },
                paging: false,
                columns: [{
                    select: 0,
                    render: renderYesNo
                }]
            });


        }
    }
    )

}

sendBtn.addEventListener('click', () => sendRequests());


}
);
