

window.addEventListener('DOMContentLoaded', event => {


let data = [
    {
        "prop1": "value1",
        "prop2": "value2",
        "prop3": "value3"
    },
    {
        "prop1": "value4",
        "prop2": "value5",
        "prop3": "value6"
    }
];

let obj = {
    headings: Object.keys(data[0]),
    data: []
};

for ( let i = 0; i < data.length; i++ ) {

    obj.data[i] = [];

    for (let p in data[i]) {
        if( data[i].hasOwnProperty(p) ) {
            obj.data[i].push(data[i][p]);
        }
    }
}


    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        let dataTable = new simpleDatatables.DataTable(datatablesSimple, {
            data: obj,
        });
    }

});
