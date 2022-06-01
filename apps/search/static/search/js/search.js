window.addEventListener('DOMContentLoaded', event=>{

    fetch('/api/v1/search/google', {
        method: 'POST'
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

    function renderYesNo(data, cell, row) {
        if (data == 'true') {
            return row.classList.add("yes"),
            `<b>Yes</b>`;
        } else if (data == 'false') {
            return row.classList.add("no"),
            `<input type="checkbox">`;
        }
    }
}
);
